
import numpy as np
import pandas as pd
import scipy as sp
from numpy import random
import matplotlib.pyplot as plt
from pm_vol_func import *

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

hfi = get_hfi_returns()

def basic_info(returns: pd.DataFrame):
    ret = returns.agg(["mean", "median", "skew", "kurt"])
    return ret

print("\nBasic info\n", basic_info(hfi))


#manual skew calc
def skew(returns: pd.DataFrame):
    dev_return = returns - returns.mean()
    sigma_r = returns.std(ddof=0) #population std
    skew = ((dev_return**3).mean())/ (sigma_r**3)

    return skew

print("\nSkewness of hfi: \n", skew(hfi).sort_values())
print("\nSkewness of hfi: \n", sp.stats.skew(hfi)) #sp function for skew
print("\nSkewness of hfi: \n", hfi.skew()) #panda built-in function for skew 


#manual kurtosis calc
def kurtosis(returns: pd.DataFrame):
    dev_return = returns - returns.mean()
    sigma_r = returns.std(ddof=0) #population std
    kurtosis = ((dev_return**4).mean())/ (sigma_r**4)

    return kurtosis

print("\nKurtosis of hfi: \n", kurtosis(hfi).sort_values())
print("\nKurtosis of hfi: \n", (hfi.kurt().sort_values()+3)) #panda built-in function for kurtosis


def is_normal(returns, level = 0.05):
    statistic, p_value = sp.stats.jarque_bera(returns)
    return p_value >level


