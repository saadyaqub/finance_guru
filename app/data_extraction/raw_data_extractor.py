import re
import pandas as pd
from app.data_extraction.data_model import RawExtractedItems


def parse_accounting_cell(cell) -> float | None:
    """This functions extracts numerical data from a excel sheet cells row-wise.
    Any value with the a positive or negative sign will be returned as is.
    If the value is within parenthesis, it will be considered a negative value
    If the value is Dr, it will be considered as postivie and if it is credit, it will be considered as negative. This will later be adjusted taking the accounting principles into consideration.
    

    Args:
        cell (Any): The cell can be of any type.

    Returns:
        float | None: The returned value is either a float or none.
    """
# When the value is a number or float, it is returned as is.
    if isinstance(cell, (int, float)) and not pd.isna(cell):
        return float(cell)

    if not isinstance(cell, str):
        return None

    raw = cell.strip()
    if raw in ("---", "-", ""):
        return None


    paren_match = re.match(r"^\(([\d,]+\.?\d*)\)$", raw)
    if paren_match:
        return -float(paren_match.group(1).replace(",", ""))

    signed_match = re.match(r"^-([\d,]+\.?\d*)$", raw)
    if signed_match:
        return -float(signed_match.group(1).replace(",", ""))

    side_match = re.match(
        r"^([\d,]+\.?\d*)\s*(Dr\.?|Cr\.?|Debit|Credit)?$", raw, re.IGNORECASE
    )
    if side_match:
        number_part, side_part = side_match.groups()
        try:
            value = float(number_part.replace(",", ""))
        except ValueError:
            return None
        if side_part is None:
            return value  # no marker -> assume positive
        side_lower = side_part.lower()
        if side_lower.startswith("dr") or side_lower.startswith("debit"):
            return value
        else:
            return -value

    return None


def extract_pairs(df: pd.DataFrame) -> list[RawExtractedItems]:
    """This function will extract the label and value pair.

    Args:
        df (pd.DataFrame): Df is the excel spreadsheet converted to a pandas dataframe

    Returns:
        list[RawExtractedItems]: Retruned data is a list of object of class RawExtractedItems. Pleas check data_model.py for more information.
    """
    results = []
    for _, row in df.iterrows():
        label = None
        value = None
        for cell in row:
            if pd.isna(cell):
                continue
            if label is None:
                if isinstance(cell, str) and cell.strip():
                    label = cell.strip()
                continue
            value = parse_accounting_cell(cell)
            if value is not None:
                break
        if label is not None and value is not None:
            results.append(RawExtractedItems(label=label, value=value))
    return results


if __name__ == "__main__":
    import os
    filepath = os.path.expanduser("~/Projects/finance_guru/app/sample_data/income_statement.xlsx")
    df = pd.read_excel(filepath, header=None, sheet_name=0)
    for item in extract_pairs(df):
        print(item)