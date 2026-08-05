
import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''

Calculate volatility manually

'''

prices = pd.read_csv("data_pm/sample_prices.csv")
returns = prices.pct_change().dropna()

print("\nprices: \n", prices)
print("\nreturns: \n", returns)

deviations = returns -returns.mean()
variance = (deviations**2).sum()/(returns.shape[0]-1)
std = np.sqrt(variance)

#dataframe std() and std() functions 
print("\nvariance manual: \n", variance, "\n"
      "\nvariance built-in \n", returns.var())
print("\nstd manual: \n", std, "\n"
      "\nstd built-in\n", returns.std())


#annualize volatility
annual_volatility = returns.std() * np.sqrt(12)
print("\nannual volatility: \n", annual_volatility)














