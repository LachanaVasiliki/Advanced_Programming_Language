#Giorgos Christodoulou  icsd19245
#Lachana Vasiliki       icsd19110

import requests
import matplotlib.pyplot as plt



import pandas as pd
fromfile = pd.read_excel('sneakers.xlsx')
 
print(fromfile)

fromfile.isna().sum() #metrisi null timon

#ypologismos mesis timis kai mesoy arithmoy reviews
meanprice = fromfile['Prices'].mean()
print('meanprice:'+str(meanprice))
meanreviews = fromfile['Reviews'].mean()
print('meanreviews:'+str(meanreviews))

#antikatastasi null timon
fromfile['Prices'].fillna(meanprice)
fromfile['Reviews'].fillna(meanreviews)
print(fromfile)
npprices = fromfile['Prices'].to_numpy()
npreviews = fromfile['Reviews'].to_numpy()
plt.scatter(npprices, npreviews)
plt.show()