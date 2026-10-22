# This file contains functions to calculate financial ratios.

####################################################################
#                       LIQUIDITY RATIOS                           #
####################################################################

# Current Ratio


def current_ratio(current_assets: float, current_liabilities: float) -> float:
    """Calculate the current ratio.

    Args:
        current_assets (float): The total current assets.
        current_liabilities (float): The total current liabilities.

    Returns:
        float: The current ratio, calculated as current assets divided by current liabilities.

    Raises:
        ValueError: If current liabilities are zero,
    """
    if current_liabilities == 0:
        raise ValueError("Current liabilities cannot be zero.")

    return current_assets / current_liabilities


# Quick Ratio (Acid-Test Ratio)


def quick_ratio(
    current_assets: float, inventory: float, current_liabilities: float
) -> float:
    """Measures short-term liquidity excluding inventory, which is harder to convert to cash quickly.

    Args:
        current_assets (float): Total current assets including inventory.
        inventory (float): Inventory value that's excluded from this ratio.
        current_liabilities (float): Total current liabilities.
    Returns:
        float: Quick ratio calculated as (current_assets - inventory) / current_liabilities.

    Raises:
        ValueError: ValueError: If current_liabilities is zero.
        ValueError: If inventory is negative.
        ValueError: If inventory exceeds current_assets.
    """
    if current_liabilities == 0:
        raise ValueError("Current liabilities cannot be zero.")

    if inventory < 0:
        raise ValueError("Inventory value cannot be negative.")

    if inventory > current_assets:
        raise ValueError("Inventory value cannot be greater than current assets.")

    return (current_assets - inventory) / current_liabilities


# Cash Ratio


def cash_ratio(cash_and_cash_equivalents: float, current_liabilities: float) -> float:
    """Measures a company's ability to pay off its short-term obligations using only its cash and cash
    equivalents.

    Args:
       cash_and_cash_equivalents (float): Total cash and cash equivalents of the company.
       current_liabilities (float): Total current liabilities

    Returns:
      float: Cash Ratio calculated as cash_and_cash equivalents/current_liabilities

    Raises:
      ValueError: If current_liabilities is zero.
    """

    if current_liabilities == 0:
        raise ValueError("Current liabilities cannot be zero.")

    return cash_and_cash_equivalents / current_liabilities


# working capital


def working_capital(current_assets: float, current_liabilities: float) -> float:
    """Calculate the working capital of a company. Working capital represents the difference between a company's current assets and its current liabilities.

    Args:
    current_assets (float): Total current assets of the company.
    current_liabilities (float): Total current liabilities of the company.

    Returns:
    float: Working capital calculated as current_assets - current_liabilities.
    """

    return current_assets - current_liabilities


############################################################################
#                        Leverage/Solvency Ratios                          #
############################################################################

# Debt to Equity Ratio


def debt_to_equity_ratio(total_liabilities: float, total_equity: float) -> float:
    """Calculate the debt to equity ratio.

    Args:
        total_liabilities (float): Total liabilities of the company.
        total_equity (float): Total shareholder equity.

    Returns:
        float: Debt to equity ratio calculated as total liabilities / total equity.

    Raises:
        ValueError: If total_equity is zero.
    """
    if total_equity == 0:
        raise ValueError("Total equity cannot be zero.")

    return total_liabilities / total_equity


# Debt to Asset Ratio


def debt_to_asset_ratio(total_liabilities: float, total_assets: float) -> float:
    """Calculate the debt to asset ratio.
    Args:
       total_liabilities (float): Total liabilities of the company.
       total_assets (float): Total assets owned by the company.

    Returns:
       float: Debt to asset ratio calculated as total liabilities / total assets.

    Raises:
       ValueError: If total_assets is zero
    """
    if total_assets <= 0:
        raise ValueError("Total assets cannot be zero")

    return total_liabilities / total_assets


# Interest Coverage
def interest_coverage_ratio(ebit: float, interest_expenses: float) -> float:
    """Calculate the interest coverage ratio.
    Args:
        ebit (float): Earnings before interest and taxes.
        interest_expenses (float): Interest expenses of the company.
    Returns:
        float: Interest coverage ratio calculated as EBIT / interest expenses.
    Raises:
        ValueError: If interest_expenses is zero.
    """
    if interest_expenses == 0:
        raise ValueError("Interest expenses cannot be zero")
    return ebit / interest_expenses


# Equity Multiplier


def equity_multiplier(total_equity: float, total_assets: float) -> float:
    """Calculate the equity multiplier ratio.
    Args:
        total_equity  (float): Total equity of the company.
        total_assets (float): Total assets of the company.
    Returns:
        float: Equity multiplier ratio calculated as total liabilities / total assets.
    Raises:
        ValueError: If total_assets is zero.
    """
    if total_assets == 0:
        raise ValueError("Total assets cannot be zero")
    return total_assets / total_equity


############################################################################
#                        Profitability Ratios                              #
############################################################################

# Return on Assets (ROA)


def return_on_assets(net_income: float, total_assets: float) -> float:
    """Calculate the return on assets ratio.
    Args:
        net_income (float): Income after deduct all expenses.
        total_assets (float): Total assets owned by the company.
    Returns:
        float: Return on assets ratio calculated as net_income / total_assets.
    Raises:
        ValueError: If total_assets is zero.
    """
    if total_assets == 0:
        raise ValueError("Total assets cannot be zero")

    return net_income / total_assets


# Return on Equity (ROE)


def return_on_equity(net_income: float, total_equity: float) -> float:
    """Calculate the return on equity ratio.
    Args:
        net_income (float): Income after deducting all expenses.
        total_equity (float): Total equity owned by the company.
    Returns:
        float: Return on equity ratio calculated as net_income / total_equity.
    Raises:
        ValueError: If total_equity is zero.
    """
    if total_equity == 0:
        raise ValueError("Total equity cannot be zero")
    return net_income / total_equity


# Net Profit Margin


def net_profit_margin(net_income: float, total_revenue: float) -> float:
    """Calculates the net profit margin ratio.
    Args:
        net_income (float): Income after deduct all expenses.
        total_revenue (float): Total revenue generated by the company.
    Returns:
        float: Net profit margin ratio calculated as net_income / total_revenue.
    Raises:
        ValueError: If total_revenue is zero.
    """
    if total_revenue == 0:
        raise ValueError("Total revenue cannot be zero")
    return net_income / total_revenue


# Gross profit margin


def gross_profit_margin(total_revenue: float, cogs: float) -> float:
    """Calculates the gross profit margin.
    Args:
        total_revenue (float): Total revenue generated by the company.
        cogs (float): Cost of goods sold.
    Returns:
        float: Gross profit margin ratio calculated as (total_revenue - cogs) / total_revenue.
    Raises:
        ValueError: If total_revenue is zero or less.
    """
    if total_revenue <= 0:
        raise ValueError("Total revenue must be greater than zero.")
    return (total_revenue - cogs) / total_revenue


# Operating Margin


def operating_margin(operating_income: float, total_revenue: float) -> float:
    """Profit from core operations, before interest/tax

    Args:
        operating_income (float): Operating income generated by the company.
        total_revenue (float): Total revenue generated by the company.

    Raises:
        ValueError: If total_revenue is zero or less.

    Returns:
        float: Operating margin calculated as operating_income / total_revenue.
    """
    if total_revenue <= 0:
        raise ValueError("Total revenue must be greater than zero.")
    return operating_income / total_revenue

############################################################################
#                        Efficiency Ratios                                 #
############################################################################

# Inventory Turnover (average balance method - preferred)

def inventory_turnover(cogs: float, opening_inventory: float, closing_inventory: float) -> float:
    """Measures how many times a company sells and replaces its inventory over a period,
    using the average of opening and closing inventory balances.

    Args:
        cogs (float): Cost of goods sold for the period.
        opening_inventory (float): Inventory value at the start of the period.
        closing_inventory (float): Inventory value at the end of the period.

    Returns:
        float: Inventory turnover calculated as cogs / average inventory.

    Raises:
        ValueError: If opening_inventory or closing_inventory is negative.
        ValueError: If average inventory is zero.
    """
    if opening_inventory < 0 or closing_inventory < 0:
        raise ValueError("Inventory values cannot be negative.")

    average_inventory = (opening_inventory + closing_inventory) / 2

    if average_inventory == 0:
        raise ValueError("Average inventory cannot be zero.")

    return cogs / average_inventory


# Inventory Turnover (closing balance only - explicit fallback)

def inventory_turnover_closing_only(cogs: float, closing_inventory: float) -> float:
    """Measures inventory turnover using only the closing inventory balance.
    Use only when opening balance data is unavailable - less accurate than the
    average-balance method, especially for seasonal businesses.

    Args:
        cogs (float): Cost of goods sold for the period.
        closing_inventory (float): Inventory value at the end of the period.

    Returns:
        float: Inventory turnover calculated as cogs / closing_inventory.

    Raises:
        ValueError: If closing_inventory is negative or zero.
    """
    if closing_inventory <= 0:
        raise ValueError("Closing inventory must be greater than zero.")

    return cogs / closing_inventory


# Receivables Turnover (average balance method - preferred)

def receivables_turnover(revenue: float, opening_accounts_receivable: float, closing_accounts_receivable: float) -> float:
    """Measures how efficiently a company collects payment from customers,
    using the average of opening and closing accounts receivable balances.

    Args:
        revenue (float): Total revenue for the period.
        opening_accounts_receivable (float): Accounts receivable at the start of the period.
        closing_accounts_receivable (float): Accounts receivable at the end of the period.

    Returns:
        float: Receivables turnover calculated as revenue / average accounts receivable.

    Raises:
        ValueError: If opening_accounts_receivable or closing_accounts_receivable is negative.
        ValueError: If average accounts receivable is zero.
    """
    if opening_accounts_receivable < 0 or closing_accounts_receivable < 0:
        raise ValueError("Accounts receivable values cannot be negative.")

    average_receivables = (opening_accounts_receivable + closing_accounts_receivable) / 2

    if average_receivables == 0:
        raise ValueError("Average accounts receivable cannot be zero.")

    return revenue / average_receivables


# Receivables Turnover (closing balance only - explicit fallback)

def receivables_turnover_closing_only(revenue: float, closing_accounts_receivable: float) -> float:
    """Measures receivables turnover using only the closing accounts receivable balance.
    Use only when opening balance data is unavailable.

    Args:
        revenue (float): Total revenue for the period.
        closing_accounts_receivable (float): Accounts receivable at the end of the period.

    Returns:
        float: Receivables turnover calculated as revenue / closing_accounts_receivable.

    Raises:
        ValueError: If closing_accounts_receivable is negative or zero.
    """
    if closing_accounts_receivable <= 0:
        raise ValueError("Closing accounts receivable must be greater than zero.")

    return revenue / closing_accounts_receivable


# Days Sales Outstanding

def days_sales_outstanding(receivables_turnover_value: float) -> float:
    """Calculates the average number of days it takes to collect payment after a sale.

    Args:
        receivables_turnover_value (float): A pre-computed receivables turnover value,
            from either receivables_turnover() or receivables_turnover_closing_only().

    Returns:
        float: Days sales outstanding calculated as 365 / receivables_turnover_value.

    Raises:
        ValueError: If receivables_turnover_value is zero or negative.
    """
    if receivables_turnover_value <= 0:
        raise ValueError("Receivables turnover value must be greater than zero.")

    return 365 / receivables_turnover_value


# Asset Turnover

def asset_turnover(revenue: float, total_assets: float) -> float:
    """Measures how efficiently a company uses its assets to generate revenue.

    Args:
        revenue (float): Total revenue for the period.
        total_assets (float): Total assets (closing balance, or average if available).

    Returns:
        float: Asset turnover calculated as revenue / total_assets.

    Raises:
        ValueError: If total_assets is zero or negative.
    """
    if total_assets <= 0:
        raise ValueError("Total assets must be greater than zero.")

    return revenue / total_assets

