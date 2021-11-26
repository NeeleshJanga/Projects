#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("Advertising.csv")


# In[3]:


df.head()


# In[6]:


sales = df['sales']
newspaper = df['newspaper']
tv = df['TV']
radio = df['radio']


# In[4]:


X = df.drop('sales', axis = 1)


# In[7]:


X.head()


# In[15]:


y = sales


# In[9]:


from sklearn.preprocessing import PolynomialFeatures


# In[11]:


help(PolynomialFeatures)


# In[13]:


# polynomial_converter = PolynomialFeatures()
polynomial_converter = PolynomialFeatures(degree = 2, include_bias = False)


# In[27]:


polynomial_converter.fit(X)


# In[28]:


X.shape


# In[30]:


poly_features = polynomial_converter.transform(X)
poly_features


# In[33]:


poly_features.shape


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




