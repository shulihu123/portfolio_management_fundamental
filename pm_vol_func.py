import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt


def read_me_returns():
    returns = pd.read_csv("data_pm/Portfolios_Formed_on_ME_monthly_EW.csv", header=0, index_col=0, na_values=-99.99)
    col = ["Lo 10", "Hi 10"]
    returns = returns[col] #pandas column selection
    returns.columns = ["Small Cap", "Large Cap"] #pandas column renaming
    returns = returns/100
    returns.index = pd.to_datetime(returns.index,format="%Y%m").to_period("M")
    return returns


def volatility(returns: pd.DataFrame):
    annual_vol = returns.std()*np.sqrt(12)
    return annual_vol


def annual_return(returns: pd.DataFrame):
    n_month = returns.shape[0]
    annual_return = (returns+1).prod()**(12/n_month)-1
    return annual_return

def sharpe_ratio(returns: pd.DataFrame, rfr: float):
    annual_ret = annual_return(returns)
    annual_vol = volatility(returns)
    sharpe_ratio = (annual_ret - rfr) / annual_vol
    return sharpe_ratio


"""

calcualte drawdown and max drawdown

"""

def drawdown(returns: pd.DataFrame):
    wealth_index = (1+returns).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdown = (wealth_index - previous_peaks) / previous_peaks
    return drawdown

def max_drawdown(returns: pd.DataFrame):
    return drawdown(returns).min()

def max_drawdown_y(returns: pd.DataFrame):
    return drawdown(returns).idxmin()

if __name__ == "__main__":
    returns = read_me_returns()
 
    print(returns.agg(["mean", "median", "std", "skew", "kurt"]))

    perform_stats = pd.DataFrame({
        "Annual Return": annual_return(returns),
        "Annual Volatility": volatility(returns),
        "Max Drawdown": max_drawdown(returns),
        "Max Drawdown Year": max_drawdown_y(returns),
        "Sharpe Ratio": sharpe_ratio(returns, 0.03)
    })

    print("\nPerformance Summary: \n", perform_stats.T)
    drawdown(returns).plot(title="Portfolio Drawdown")










   










