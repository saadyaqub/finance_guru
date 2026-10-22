

import os
import re
import unicodedata
import pandas as pd
from typing import Dict, List, Optional, Tuple
from app.data_extraction.data_model import RawExtractedItems

# All active ISO 4217 3-letter currency codes -- single source of truth,
# used both for cell-level currency detection and header/period-area scanning.
ISO_CURRENCY_REGEX = re.compile(
    r"\b(AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|"
    r"BND|BOB|BRL|BSD|BTN|BWP|BYN|BZD|CAD|CDF|CHF|CLP|CNY|COP|CRC|CUP|CVE|CZK|"
    r"DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GHS|GIP|GMD|GNF|GTQ|GYD|"
    r"HKD|HNL|HRK|HTG|HUF|IDR|ILS|INR|IQD|IRR|ISK|JMD|JOD|JPY|KES|KGS|KHR|KMF|"
    r"KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|"
    r"MRU|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|"
    r"PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SRD|"
    r"SSP|STN|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TWD|TZS|UAH|UGX|USD|UYU|"
    r"UZS|VES|VND|VUV|WST|XAF|XCD|XOF|XPF|YER|ZAR|ZMW|ZWL)\b"
)

CURRENCY_SYMBOL_REGEX = re.compile(r"[\$€£¥₹]")

PERIOD_REGEX = re.compile(
    r"("
    r"\b(?:19|20)\d{2}\b"  # 19xx or 20xx years
    r"|FY\s?\d{2,4}"  # FY2024, FY 24
    r"|Q[1-4]\s?\d{2,4}"  # Q1 2024, Q324
    r"|(?:H[12]|1H|2H|9M|YTD)\s?\d{2,4}"  # Half-years/YTD: H1 2024, 1H24, YTD 2024
    r"|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+(?:19|20)\d{2}"  # Any Month Day, Year
    r"|\b\d{1,2}[/-]\d{1,2}[/-](?:19|20)?\d{2}\b"  # Date slashes/dashes: 12/31/2024, 2024-12-31
    r")",
    re.IGNORECASE,
)


def _clean_cell_string(raw: str) -> str:
    """Normalizes whitespace and removes non-breaking or zero-width spaces."""
    return (
        raw.replace("\xa0", " ")
        .replace("\u200b", "")
        .replace("\ufeff", "")
        .strip()
    )


def _extract_currency_and_clean(text: str) -> Tuple[Optional[str], str]:
    """Detects and strips a currency symbol or ISO 3-letter code from text."""
    symbol_match = CURRENCY_SYMBOL_REGEX.search(text)
    if symbol_match:
        currency = symbol_match.group(0)
        text = CURRENCY_SYMBOL_REGEX.sub("", text)
        return currency, text.strip()

    iso_match = ISO_CURRENCY_REGEX.search(text)
    if iso_match:
        currency = iso_match.group(1).upper()
        text = ISO_CURRENCY_REGEX.sub("", text)
        return currency, text.strip()

    return None, text.strip()


def parse_accounting_cell(cell) -> Tuple[Optional[str], Optional[str], Optional[float]]:
    """Parses a single cell. Returns (balance_type, currency, numeric_value)."""
    if isinstance(cell, (int, float)) and not pd.isna(cell):
        return None, None, float(cell)

    if not isinstance(cell, str):
        return None, None, None

    raw = _clean_cell_string(cell)
    if raw in ("---", "-", "", "N/A", "n/a"):
        return None, None, None

    currency, raw_clean = _extract_currency_and_clean(raw)

    paren_match = re.match(r"^\(([\d,]+\.?\d*)\)$", raw_clean)
    if paren_match:
        return None, currency, -float(paren_match.group(1).replace(",", ""))

    signed_match = re.match(r"^-([\d,]+\.?\d*)$", raw_clean)
    if signed_match:
        return None, currency, -float(signed_match.group(1).replace(",", ""))

    side_match = re.match(
        r"^([\d,]+\.?\d*)\s*(Dr\.?|Cr\.?|Debit|Credit)?$", raw_clean, re.IGNORECASE
    )
    if side_match:
        number_part, side_part = side_match.groups()
        try:
            val = float(number_part.replace(",", ""))
        except ValueError:
            return None, None, None

        balance_type = None
        if side_part:
            side_lower = side_part.lower()
            if side_lower.startswith("dr") or side_lower.startswith("debit"):
                balance_type = "Dr"
            elif side_lower.startswith("cr") or side_lower.startswith("credit"):
                balance_type = "Cr"

        return balance_type, currency, val

    return None, None, None


def detect_sheet_currency_and_period(df: pd.DataFrame, max_rows: int = 10) -> Tuple[Optional[str], Optional[str]]:
    """
    Scans the top rows of the sheet for ONE sheet-wide currency and ONE
    sheet-wide period, applied to every extracted item.

    This assumes a single-period statement (the layout seen in every real
    sample file so far) rather than side-by-side multi-year columns. If
    multi-period support is needed later, this is the function to extend
    -- deliberately, with real sample files to test against, not upfront.
    """
    currency = None
    period = None

    for row_idx in range(min(max_rows, len(df))):
        row = df.iloc[row_idx]
        for cell in row:
            if pd.isna(cell):
                continue

            if isinstance(cell, float) and cell.is_integer():
                cell_str = str(int(cell))
            else:
                cell_str = _clean_cell_string(str(cell))

            if currency is None:
                symbol_match = CURRENCY_SYMBOL_REGEX.search(cell_str)
                if symbol_match:
                    currency = symbol_match.group(0)
                else:
                    iso_match = ISO_CURRENCY_REGEX.search(cell_str)
                    if iso_match:
                        currency = iso_match.group(1).upper()

            if period is None:
                p_match = PERIOD_REGEX.search(cell_str)
                if p_match:
                    period = p_match.group(1)

    return currency, period


def extract_pairs(df: pd.DataFrame, source_file: str = "", source_sheet: str = "") -> List[RawExtractedItems]:
    """
    Scans each row left to right: first text cell found = label, first
    parseable value found after it = the value (scanning stops there --
    any further numeric cells in the same row are ignored). Rows with no
    label or no value are skipped (headers, section titles, blank rows).
    """
    sheet_currency, sheet_period = detect_sheet_currency_and_period(df)

    results: List[RawExtractedItems] = []

    for row_idx, row in df.iterrows():
        excel_row_number = row_idx + 1  # 1-based, for auditing
        label = None
        label_col = None

        for col_idx, cell in enumerate(row):
            if pd.isna(cell):
                continue

            if label is None:
                if isinstance(cell, str) and cell.strip():
                    label = _clean_cell_string(cell)
                    label_col = f"Col_{col_idx + 1}"
                continue

            bal_type, cell_currency, parsed_val = parse_accounting_cell(cell)
            if parsed_val is not None:
                results.append(
                    RawExtractedItems(
                        label=label,
                        value=parsed_val,
                        source_file=source_file,
                        source_sheet=source_sheet,
                        row_index=excel_row_number,
                        label_column=label_col,
                        value_column=f"Col_{col_idx + 1}",
                        balance_type=bal_type,
                        currency=cell_currency or sheet_currency,
                        period=sheet_period,
                    )
                )
                break  # stop scanning this row once a value is found

        # (no else needed: if the loop finishes with no value found,
        # nothing is appended -- correctly skips headers/blank rows)

    return results


def extract_pairs_from_file(file_path: str, sheet_name: Optional[str] = None) -> List[RawExtractedItems]:
    """Thin wrapper: loads a file from disk, then delegates to extract_pairs.
    Kept separate so extract_pairs itself can be tested with in-memory
    DataFrames, no file I/O required."""
    excel_file = pd.ExcelFile(file_path)
    target_sheet = sheet_name if sheet_name is not None else excel_file.sheet_names[0]
    df = pd.read_excel(excel_file, sheet_name=target_sheet, header=None)
    file_name = os.path.basename(file_path)
    return extract_pairs(df, source_file=file_name, source_sheet=target_sheet)


if __name__ == "__main__":
    filepath = os.path.expanduser("~/Projects/finance_guru/app/sample_data/income_statement.xlsx")
    for item in extract_pairs_from_file(filepath):
        print(item.model_dump_json(indent=2))