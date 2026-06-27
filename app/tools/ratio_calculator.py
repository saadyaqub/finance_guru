# This file contains functions to calculate financial ratios.


# Defining a function to calculate the current ratio

def current_ratio(current_assets:float, current_liabilities:float)-> float:
    """
    Calculate the current ratio.

    Args:
        current_assets (float): The total current assets.
        current_liabilities (float): The total current liabilities.

    Returns:
        float: The current ratio, calculated as current assets divided by current liabilities.
    """
    if current_liabilities == 0:
        raise ValueError("Current liabilities cannot be zero.")
    
    if current_assets == 0 or current_assets == None:
        raise ValueError ("Please check the value for the current assets")
    
    return current_assets / current_liabilities

# Defining a function to calculate the debt to equity ratio

def debt_to_equity_ratio(total_liabilities:float, total_equity:float)-> float:
    """
    Calculate the debt to equity ratio.

    Args:
        total_liabilities (float): The total liabilities.
        total_equity (float): The total equity.

    Returns:
        float: The debt to equity ratio, calculated as total liabilities divided by total equity.
    """
    if total_equity == 0:
        raise ValueError("Total equity cannot be zero.")
    
    return total_liabilities / total_equity

def return_on_assets(net_income:float, total_assets:float)-> float:
    """
    This function/ ratio calculates the return on the assests

    Args:
        net_income (float): the income after deducting the expenses
        total_assets (float): Total assests owned

    Returns:
        float: return on assets, which is calculated by dividing the net income by the total assets
    """
    if total_assets ==0:
        raise ValueError("Total assets cannot be 0. Please check")
    
    return net_income/total_assets

    