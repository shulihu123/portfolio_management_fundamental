
import numpy as np
import pandas as pd
from scipy.stats import norm
import scipy as sp
import matplotlib.pyplot as plt
from pm_vol_func import *
from pm_hfi import *


hfi = get_hfi_returns()

def var_historic(r, level=5):
    """
    VaR Historic
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level = level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else: 
        raise TypeError("Expected r to be Series or DataFrame")

print(var_historic(hfi).sort_values())


def var_gaussian(r, level=5):
    """
    Returns the parametric Gaussian VaR of a Series or DataFrame
    """
    #compute z score
    z = norm.ppf(level/100)
    return -(r.mean()+z*r.std(ddof=0))

print(var_gaussian(hfi).sort_values())

var_list = [var_historic(hfi), var_gaussian(hfi)]
comparison = pd.concat(var_list, axis=1)
comparison.columns = ["Historical VaR","Gaussian VaR"]
comparison.plot.bar()
# plt.show()


def cvar_historic(r, level=5):
    """
    Computes the Conditional VaR or Expected Shortfall of Series or DataFrame
    """

    if isinstance(r, pd.Series):
        is_beyond = r<= -var_historic(r, level=level)
        return -r[is_beyond].mean()
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TypeError("Expected r to be a Series or DataFrame")


print("\nExpected Shortfall: \n", cvar_historic(hfi))
    

with pd.ExcelWriter("output/portfolio_VaR.xlsx", engine="openpyxl") as writer:
    var_historic(hfi).to_excel(writer, sheet_name="VaR Historic")
    var_gaussian(hfi).to_excel(writer, sheet_name="VaR Gaussian")
    cvar_historic(hfi).to_excel(writer, sheet_name="Expected Shortfall")
    
