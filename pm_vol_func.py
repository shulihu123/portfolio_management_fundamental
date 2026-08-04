import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
from pm_hfi import *

def read_me_returns():
    returns = pd.read_csv("data_pm/Portfolios_Formed_on_ME_monthly_EW.csv", header=0, index_col=0, na_values=-99.99)
    col = ["Lo 10", "Hi 10"]
    returns = returns[col] #pandas column selection
    returns.columns = ["Small Cap", "Large Cap"] #pandas column renaming
    returns = returns/100
    returns.index = pd.to_datetime(returns.index,format="%Y%m").to_period("M")
    return returns

returns = read_me_returns()

def volatility(returns: pd.DataFrame):
    annual_vol = returns.std()*np.sqrt(12)
    return annual_vol

print("\nAnnual volatility: ", volatility(returns))

def annual_return(returns: pd.DataFrame):
    n_month = returns.shape[0]
    annual_return = (returns+1).prod()**(12/n_month)-1
    return annual_return

print("\nAnnual Return: \n", annual_return(returns))

def sharpe_ratio(returns: pd.DataFrame, rfr: float):
    annual_ret = annual_return(returns)
    annual_vol = volatility(returns)
    sharpe_ratio = (annual_ret - rfr) / annual_vol
    return sharpe_ratio

print("\nSharpe Ratio: \n", sharpe_ratio(returns, 0.03))

"""

calcualte drawdown and max drawdown

"""

def max_drawdown(returns_pd: pd.DataFrame):
    wealth_index = 1000*(1+returns_pd).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdown = (wealth_index-previous_peaks)/previous_peaks

    return pd.DataFrame([drawdown.idxmin(), drawdown.min()], index=["year-month", "max drawdown"])

print("\nmax drawdown: \n", max_drawdown(returns))            

"""
Analyze on Hedge Fund Index returns
"""

def get_hfi_returns():
    """
    Load and format the Hedge Fund Index Returns
    """

    hfi = pd.read_csv("data_pm/edhec-hedgefundindices.csv", 
                      header=0, index_col=0, parse_dates=True)
    hfi = hfi/100
    hfi.index = hfi.index.to_period('M')
    return hfi


print(returns.agg(["mean", "median", "std", "skew", "kurt"]))








