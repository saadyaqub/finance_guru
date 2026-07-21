# This file contains functions to calculate financial ratios.

####################################################################
#                       LIQUIDITY RATIOS                           #
####################################################################

# Current Ratio

def current_ratio(current_assets:float, current_liabilities:float)-> float:
    """Calculate the current ratio.

    Args:
        current_assets (float): The total current assets.
        current_liabilities (float): The total current liabilities.

    Returns:
        float: The current ratio, calculated as current assets divided by current liabilities.
    """
    if current_liabilities == 0:
        raise ValueError("Current liabilities cannot be zero.")
    
    return current_assets / current_liabilities

# Quick Ratio (Acid-Test Ratio)

def quick_ratio(current_assets:float, inventory:float, current_liabilities:float)-> float:
    """Measures short-term liquidity excluding inventory, which is harder to convert to cash quickly.

    Args:
        current_assets (float): Total current assets including inventory.
        inventory (float): Inventory value that's excluded from this ratio.
        current_liabilities (float): Total current liabilities.
    Returns:
        float: Quick ratio calculated as (current_assets - inventory) / current_liabilities.

    Raises:
        ValueError: If current_liabilities is zero.
    """
    if current_liabilities == 0:
        raise ValueError("Current liabilities cannot be zero.")

    return (current_assets - inventory) / current_liabilities

# Cash Ratio

def cash_ratio(cash_and_cash_equivalents:float, current_liabilities:float)-> float:
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
    
    return cash_and_cash_equivalents/ current_liabilities

# working capital

def working_capital(current_assets:float, current_liabilities:float)-> float:
    """Calculate the working capital of a company. Working capital represents the difference between a company's current assets and its current liabilities.

    Args:
    current_assets (float): Total current assets of the company.
    current_liabilities (float): Total current liabilities of the company.

    Returns: 
    float: Working capital calculated as current_assets - current_liabilities.
    """

############################################################################
#                        Leverage/Solvency Ratios                          #
############################################################################

# Debt to Equity Ratio

def debt_to_equity_ratio(total_liabilities:float, total_equity:float)-> float:
    """Calculate the debt to equity ratio.

    Args:
        total_liabilities (float): Total liabilities of the company.
        total_equity (float): Total shareholder equity.

    Returns:
        float: Debt to equity ratio calculated as total liabilities / total equity.

    Raises:
        ValueError: If total_equity is zero.
    """
    if total_equity ==0:
        raise ValueError("Total equity cannot be zero.")
    
    return total_liabilities / total_equity

# Debt to Asset Ratio

def debt_to_asset_ratio(total_liabilities:float, total_assets:float)-> float:
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
def interest_coverage_ratio(ebit:float,interest_expenses:float)-> float:
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

def equity_multiplier(total_equity:float, total_assets:float)-> float:
    """Calculate the equity multiplier ratio. 
    Args: 
        total_equity  (float): Total liabilities of the company.    
        total_assets (float): Total assets of the company.  
    Returns:  
        float: Equity multiplier ratio calculated as total liabilities / total assets.  
    Raises:   
        ValueError: If total_assets is zero. 
    """ 
    if total_assets == 0: 
        raise ValueError("Total assets cannot be zero")
    return total_assets/ total_equity


############################################################################
#                        Profatibility Ratios                              #
############################################################################

# Return on Assets (ROA)

def return_on_assets(net_income:float, total_assets:float)-> float:
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

def return_on_equity(net_income:float ,total_equity:float)-> float:
    """Calculate the return on equity ratio.   
    Args:    
        net_income (float): Income after deduct all expenses.    
        total_equity (float): Total equity owned by the company.    
    Returns:       
        float: Return on equity ratio calculated as net_income / total_equity.   
        Raises:       
        ValueError: If total_equity is zero.
        """ 
    if total_equity == 0:
        raise   ValueError("Total equity cannot be zero")
    return net_income / total_equity

# Net Profit Margin

def net_profit_margin(net_income:float ,total_revenue:float)-> float:
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

def gross_profit_margin(total_revenue:float ,cogs:float) -> float:
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

def operating_margin(operating_income:float ,total_revenue:float) -> float:
    """ Profit from core operations, before interest/tax

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


