
import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''

Calculate returns

'''


#numpy array return
print("numpy array return\n")
p_a = np.array([8.70, 8.91, 8.81])
r_a = p_a[1:]/p_a[0:2] - 1
print("return of portfolio a: ", r_a)


print()
print("pandas dataframe return\n")
prices = pd.read_csv("data_pm/sample_prices.csv")
print("\nprices: \n")
print(prices)
returns = prices.pct_change()
print("\nreturns: \n")
print(returns)

returns_annual = np.prod(1+returns) - 1
print("\nreturns annual: ", returns_annual)


print("\n")

#simple and log return
q_returns = np.array([0.05, -0.04, 0.10, -0.02])

simple_returns_annual = np.prod(1+q_returns) - 1
log_returns_annual = np.sum(np.log(1+q_returns))

print("simple quaterly returns: ", q_returns)
print("simple returns annual: ", simple_returns_annual)
print("log quaterly returns: ", np.log(1+q_returns))
print("log returns annual: ", log_returns_annual)
print("std returns: \n", returns.std())
print("mean returns: \n", returns.mean())

#daily and monthly returns annualization
rm = 0.01
rd = 0.0005
print("monthly annualized returns: ", (1+rm)**12-1)
print("daily annualized returns: ", (1+rd)**252-1)












