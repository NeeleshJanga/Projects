#!/usr/bin/env python
# coding: utf-8

# # <span style="color:#5C3D2E;">Boston House Price Prediction</span>

# ### <span style="color:Green;">For a given area of land (in square feet) the corresponding price will be predicted</span>

# ### Loading Libraries & Dataset

# In[1]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv('dataset.csv')


# In[3]:


dataset.shape


# In[4]:


dataset.head(5)


# ### Visualizing the data

# In[5]:


plt.xlabel('Price')
plt.ylabel('Area')
plt.scatter(dataset.price,dataset.area,color='red')


# ### Segregating dataset into Input/Feature as X and Output/Label as y

# In[6]:


X = dataset.drop('price',axis='columns')
X


# In[7]:


y = dataset.price
y


# ### Training Dataset using Linear Regression

# In[8]:


model = LinearRegression()
model.fit(X,y);


# In[9]:


sns.regplot(data=dataset, x='price', y='area')


# ### Predicted Price for Land sq.Feet of custom values

# In[10]:


x=40000
LandAreainSqFt=[[x]]
PredictedmodelResult = model.predict(LandAreainSqFt)
print(PredictedmodelResult)


# ### Let's check is our model is Right ? using Theory Calculation<br><br>Y = m * X + b (m is coefficient and b is intercept)

# In[11]:


# Coefficient m
m = model.coef_
m


# In[12]:


# Intercept b
b = model.intercept_
b


# In[13]:


# Equation
y = m*x + b
print("The Price of {0} Square feet Land is: {1}".format(x,round(y[0], 2)))

