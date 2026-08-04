
import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

'''

Calculate returns

'''

#numpy array return
p_a = np.array([8.70, 8.91, 8.81])
r_a = p_a[1:]/p_a[0:2] - 1
print("return of portfolio a: ", r_a)

#annualized return
prices = pd.read_csv("data_pm/sample_prices.csv")
returns = prices.pct_change()
returns_annual = np.prod(1+returns) - 1
print("\nreturns annual: ", returns_annual.round(2))


#simple and log return
q_returns = np.array([0.05, -0.04, 0.10, -0.02])

simple_returns_annual = np.prod(1+q_returns) - 1
log_returns_annual = np.sum(np.log(1+q_returns))

print("simple annual returns: ", simple_returns_annual.round(2))
print("log annual returns: ", log_returns_annual.round(2))


#daily and monthly returns annualization
rm = 0.01
rd = 0.0005
print("monthly annualized returns: ", round((1+rm)**12-1, 4))
print("daily annualized returns: ", round((1+rd)**252-1, 4))










