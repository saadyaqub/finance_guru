# This file has the synonyms for all the financial terms used in 
# ratio_calculator.py. 

# This file has the synonyms for all the financial terms used in
# ratio_calculator.py.
#
# Design notes (from review):
# - "ebit" and "operating_income" are kept as separate canonical fields,
#   but their synonym lists must NOT overlap -- a label like "Operating Profit"
#   needs to resolve to exactly one field, not both. If your source documents
#   only ever report one of the two, the mapping/report-building step (not
#   this file) can decide whether it's acceptable to fill the other from the
#   same figure -- that's a deliberate business-logic decision, not something
#   to bury silently in the synonym list.
# - Removed "total liabilities and equity" and "total assets and liabilities"
#   from total_liabilities/total_assets -- these refer to the COMBINED total
#   of both sides of the balance sheet, not one side alone. Including them
#   would silently make total_liabilities == total_assets.
# - Removed "total debt" from total_liabilities -- "total debt" conventionally
#   means interest-bearing borrowings only, a subset of total liabilities,
#   not the full figure.
# - Bare abbreviations ("ca", "cl") are kept but are the highest false-positive
#   risk in this file if fuzzy matching is ever added on top -- worth watching.

SYNONYM_MAP = {
    "current_assets": [
        "current assets",
        "total current assets",
        "current assets total",
        "ca",
        "current assets (total)",
        "total ca",
    ],
    "current_liabilities": [
        "current liabilities",
        "total current liabilities",
        "current liabilities total",
        "cl",
        "current liabilities (total)",
        "total cl",
    ],
    "inventory": [
        "inventory",
        "inventories",
        "stock",
        "inventory (net)",
        "inventory net",
        "closing inventory",
        "inventory balance",
    ],
    "cash_and_cash_equivalents": [
        "cash and cash equivalents",
        "cash & cash equivalents",
        "cash and cash equivalents (total)",
        "cash & bank balances",
        "cash and bank",
        "cash equivalents",
        "cce",
    ],
    "total_liabilities": [
        "total liabilities",
        "liabilities",
        "total liabilities (total)",
        "liabilities total",
    ],
    "total_equity": [
        "total equity",
        "equity",
        "shareholders equity",
        "shareholder's equity",
        "shareholders' equity",
        "stockholders equity",
        "total shareholders equity",
        "equity total",
        "net worth",
    ],
    "total_assets": [
        "total assets",
        "assets",
        "total assets (total)",
        "assets total",
    ],
    "net_income": [
        "net income",
        "net profit",
        "profit after tax",
        "pat",
        "net earnings",
        "net income (loss)",
        "net profit (loss)",
        "bottom line",
    ],
    "total_revenue": [
        "total revenue",
        "revenue",
        "sales",
        "total sales",
        "revenue from operations",
        "net sales",
        "gross sales",
        "turnover",
        "total turnover",
        "operating revenue",
    ],
    "cogs": [
        "cost of goods sold",
        "cogs",
        "cost of sales",
        "cost of goods sold (cogs)",
        "direct costs",
        "cost of revenue",
    ],
    "ebit": [
        "ebit",
        "earnings before interest and tax",
        "profit before interest and tax",
        "pbit",
    ],
    "interest_expenses": [
        "interest expenses",
        "interest expense",
        "finance costs",
        "interest and finance charges",
        "borrowing costs",
        "interest cost",
        "financial expenses",
    ],
    "operating_income": [
        "operating income",
        "operating profit",
        "income from operations",
        "operating earnings",
        "profit from operations",
    ],
    "opening_inventory": [
        "opening inventory",
        "beginning inventory",
        "inventory at start",
        "opening stock",
        "beginning stock",
        "inventory opening balance",
    ],
    "closing_inventory": [
        "closing inventory",
        "ending inventory",
        "inventory at end",
        "closing stock",
        "ending stock",
        "inventory closing balance",
    ],
    "opening_accounts_receivable": [
        "opening accounts receivable",
        "beginning accounts receivable",
        "accounts receivable at start",
        "opening debtors",
        "beginning debtors",
        "trade receivables opening",
    ],
    "closing_accounts_receivable": [
        "closing accounts receivable",
        "ending accounts receivable",
        "accounts receivable at end",
        "closing debtors",
        "ending debtors",
        "trade receivables closing",
    ],
}