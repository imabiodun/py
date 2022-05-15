#first_work
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

filename='winequality-red.csv'
wine_quality_profile=pd.read_csv(filename)
# print(f' here is the wine profile: {wine_quality_profile.columns}' )
print(type(wine_quality_profile))
quality_less_5= wine_quality_profile['quality' ]==4.0 
print(wine_quality_profile[quality_less_5].round(2))
print('described :')
print(wine_quality_profile[quality_less_5].round(2).describe())
print("The total length is: ")
print(len(wine_quality_profile[quality_less_5].round(2)))

# print(wine_quality_profile.describe().round(2))
x=np.linspace(0,10,1000)
#what's happening. why are you not responding?

# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
# plt.xlabel('sin x')
# plt.title("Sine and Cosine curve")
# plt.show()
