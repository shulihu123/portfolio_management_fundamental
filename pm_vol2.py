import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


returns = pd.read_csv("data_pm/Portfolios_Formed_on_ME_monthly_EW.csv", header=0, index_col=0, parse_dates=True, na_values=-99.99)

col = ["Lo 10", "Hi 10"]
returns = returns[col] #pandas column selection
returns.columns = ["Small Cap", "Large Cap"] #pandas column renaming
returns = returns/100
# returns.plot.line()

#volatility
annual_vol = returns.std()*np.sqrt(12)
# print("monthly returns std: \n", returns.std())
print("annualized volatility: \n", annual_vol)

#average return
n_months = returns.shape[0]
annual_return = (returns+1).prod()**(12/n_months)-1
print("annual_return: \n", annual_return)

rfr = 0
sharp_ratio = (annual_return - rfr) / annual_vol        
print(sharp_ratio)

