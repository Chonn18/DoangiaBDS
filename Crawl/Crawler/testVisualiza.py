import numpy as np
import pandas as pd
from CleanData import clean_data
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("DataScience/data.csv")
data = clean_data(data)
print(data)
#d = data["Quận-Huyện"].sort_values()
#plt.figure(figsize = (15, 12))
#plt.show()



