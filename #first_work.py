#first_work
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
arr=[2,3,5,6,87,2,]
np_arr=np.array(arr)
np_arr_mask=np_arr>5
# print(np_arr.reshape(2,-1))
# print ('these are true:')
# print(np_arr[np_arr_mask])
filename='winequality-red.csv'
wine_quality_profile=pd.read_csv(filename)
# wine_quality_profile=np.lload(filename)

print(wine_quality_profile[['fixed acidity','citric acid']].describe())
x=np.linspace(0,10,1000)
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
# plt.xlabel('sin x')
# plt.title("Sine and Cosine curve")
# plt.show()
