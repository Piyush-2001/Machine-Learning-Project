# **IMPORTING LIBRARIES**

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from matplotlib import pyplot
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

# **READING CSV FILE**

df = pd.read_csv("/content/drive/My Drive/filename.csv")
df.head()

df.describe()

# **CREATING ID_rx AND ID_tx DUMMIES**

dumies_tx = pd.get_dummies(df.ID_tx)
dumies_tx

dumies_tx = dumies_tx.drop([48], axis = 'columns')

dumies_rx = pd.get_dummies(df.ID_rx)
dumies_rx

dumies_rx = dumies_rx.drop([48], axis = 'columns')#number of dumies=no of categorical variables-1

# **CREATING INDEPENDENT FRAME ind**

merged= pd.concat([df,dumies_tx,dumies_rx], axis='columns')
ind =merged.drop(['ID_rx','ID_tx','X_rx','Y_rx','RSSI'] ,axis = 'columns')
ind

# **CREATING DEPENDENDENT FRAMES dep1 AND dep2**

dep1 = df['X_rx']
dep1

dep2= df['Y_rx']
dep2

#**GRAPHS**

data = df[['ID_tx']]
sns.distplot(data, hist=True, rug=True);

data = df[['ID_rx']]
sns.distplot(data, hist=True, rug=True);

data = df[['X_tx']]
sns.distplot(data, hist=True, rug=True);

data = df[['Y_tx']]
sns.distplot(data, hist=True, rug=True);

data = df[['X_rx']]
sns.distplot(data, hist=True, rug=True);

data = df[['Y_rx']]
sns.distplot(data, hist=True, rug=True);

data = df[['Pr']]
sns.distplot(data, hist=True, rug=True);

data = df[['LQI']]
sns.distplot(data, hist=True, rug=True);

data = df['ID_tx']
data.plot(kind= 'box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

data = df['ID_rx']
data.plot(kind= 'box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

data = df['X_tx']
data.plot(kind= 'box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

data = df['Y_tx']
data.plot(kind= 'box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

data = df['X_rx']
data.plot(kind= 'box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

data = df['Y_rx']
data.plot(kind= 'box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

data = df['Pr']
data.plot(kind= 'box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

data = df['LQI']
data.plot(kind= 'box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

correlations = df.corr()
# plot correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(df)
ax.set_yticklabels(df)
pyplot.show()

# **TRAIN TEST SPLIT APPLIED**

ind_train1, ind_test1, dep1_train, dep1_test = train_test_split(ind,dep1,test_size = 0.33, random_state = 0 )
ind_train2, ind_test2, dep2_train, dep2_test = train_test_split(ind,dep2,test_size = 0.33, random_state = 0 )

# **APPLYING REGRESSION FOR FITTING**"""

regressor_1 = DecisionTreeRegressor(random_state=0,max_depth=30)
regressor_1.fit(ind_train1,dep1_train)

regressor_2 = DecisionTreeRegressor(random_state=0,max_depth=30)
regressor_2.fit(ind_train2,dep2_train)

# **PREDICTION AND PRINTING OF SCORES** 

dep_pred1 = regressor_1.predict(ind_test1)
dep_pred1

score1 = r2_score(dep1_test,dep_pred1)
print(score1)
# 0.9432620651349661
dep_pred2 = regressor_2.predict(ind_test2)
dep_pred2

score2 = r2_score(dep2_test, dep_pred2)
print(score2)
# 0.942480689510909

