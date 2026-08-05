
import numpy as np
import pandas as pd
import scipy as sp
from numpy import random
import matplotlib.pyplot as plt
from pm_vol_func import *

ret = read_me_returns()

def track_error(returns: pd.DataFrame, bmk=0.05):
    active_return = returns - bmk/12
    return active_return.std()*np.sqrt(12)

def info_ratio(returns: pd.DataFrame, bmk=0.05):
    active_return = returns - bmk/12
    active_return_mean = active_return.mean() * 12
    return active_return_mean / track_error(returns)

print("\nTracking Error: \n", track_error(ret))
print("\nInformation Ratio: \n", info_ratio(ret))