import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


returns = pd.read_csv("data_pm/Portfolios_Formed_on_ME_monthly_EW.csv", header=0, index_col=0, na_values=-99.99)

col = ["Lo 10", "Hi 10"]
returns = returns[col] #pandas column selection
returns.columns = ["Small Cap", "Large Cap"] #pandas column renaming
returns = returns/100
returns.index = pd.to_datetime(returns.index,format="%Y%m")
returns.index = returns.index.to_period('M')


#volatility
annual_vol = returns.std()*np.sqrt(12)
# print("monthly returns std: \n", returns.std())
# print("annualized volatility: \n", annual_vol)

#average return
n_months = returns.shape[0]
annual_return = (returns+1).prod()**(12/n_months)-1
# print("annual_return: \n", annual_return)

rfr = 0
sharp_ratio = (annual_return - rfr) / annual_vol        
# print("Sharp ratio: ", sharp_ratio)


"""

calcualte max drawdown

"""

# wealth_index = 1000*(1+returns).cumprod()
# previous_peaks = wealth_index["Large Cap"].cummax()
# drawdown = (wealth_index["Large Cap"] - previous_peaks)/previous_peaks
# print("Worst drawdown: ", drawdown.idxmin(), drawdown.min()) #returns the max drawdown and when it happened


def max_drawdown(returns_pd: pd.DataFrame):
    wealth_index = 1000*(1+returns_pd).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdown = (wealth_index-previous_peaks)/previous_peaks

    return pd.DataFrame([drawdown.idxmin(), drawdown.min()], index=["year-month", "max drawdown"])


print(max_drawdown(returns))            










