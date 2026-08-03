
import numpy as np
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

print(2+2)

p_a = np.array([8.70, 8.91, 8.81])
r_a = p_a[1:]/p_a[0:2] - 1

prices = pd.DataFrame({"BLUE":[1,2,3,4,5,6,7,8,9]
                      ,
                      "ORANGE":[4,5,6,7,8,9,10,11,12]
})


r_prices = prices / prices.shift(1) - 1
print(prices.pct_change())


