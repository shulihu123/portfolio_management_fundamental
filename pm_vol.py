
import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''

Calculate volatility

'''

prices = pd.read_csv("data_pm/sample_prices.csv")
returns = prices.pct_change().dropna()

print("\nprices: \n", prices)
print("\nreturns: \n", returns)

deviations = returns -returns.mean()
variance = (deviations**2).sum()/(returns.shape[0]-1)
std = np.sqrt(variance)

#dataframe std() and std() functions 
print("\nvariance: \n", variance, "\n", returns.var())
print("\nstd: \n", std, "\n", returns.std())

print(type(returns.std()))

#annualize volatility
annual_volatility = returns.std() * np.sqrt(12)
print("\nannual volatility: \n", annual_volatility)














