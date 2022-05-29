import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

wine_reg={'rot_wein':[3,2,1,8,4,8,3,8,5,6], 
'weiss_wein':[4,3,8,2,9,4,2,5,1,9]}
pd_wine_reg= pd.DataFrame(wine_reg)
np_wine_reg=np.array(pd_wine_reg)
# np_wine_reg[1,1]=7

blau_wein=[2,5,8]
# pd_wine_reg=pd_wine_reg.append(blau_wein)
# pd_wine_reg.columns[2]='blau_wein'
print(pd_wine_reg)
print(pd_wine_reg.describe())
print(pd_wine_reg.value_counts())

# print(f'Here is the output of the wine in the cellar: {np_wine_reg[:,1]}')
print(f'The mean is:\n {pd_wine_reg["rot_wein"]}')
print(f'The median is: \n{pd_wine_reg.median()}')
plt.style.use('classic')

fig=plt.figure()
ax=plt.axes()
z=pd_wine_reg['rot_wein']
y=pd_wine_reg['weiss_wein']
# plt.scatter(z,y, marker='*', color='r')
# pd_wine_reg['rot_wein'].plot(kind='hist', title='rot wein',bins=2)
pd_wine_reg.boxplot(column='rot_wein')
plt.legend()
plt.show()
print(pd_wine_reg.columns)