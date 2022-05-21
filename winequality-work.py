#first_work
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

filename='winequality-red.csv'
wine_quality_profile=pd.read_csv(filename)


np_wine_quality_profile=np.array(wine_quality_profile)
print (np_wine_quality_profile.shape)
mask_of_chlorides=(wine_quality_profile['chlorides'].round(1))
mask_of_quality=(wine_quality_profile['quality'])
print(len(mask_of_chlorides))
print(len(mask_of_quality))
plt.style.use('ggplot')

figure=plt.figure()
ax=plt.axes()
plt.plot(mask_of_chlorides , mask_of_quality)
# plt.plot(x, np.sin(x), label='sin (x)', color='r', linestyle='dotted')
# plt.plot(x, np.cos(x), color='k', linestyle='--', label='cos(x)')
# # plt.plot(x, np.log(x), color='b', linestyle='-', label='log(x)')
# to label the x axis of the graph
plt.ylabel('Quality')
# to label the y axis of the graph
plt.xlabel('Chlorides')

plt.title("Scatter Plot of Chlorides and Quality")
# plt.legend()
plt.show()
