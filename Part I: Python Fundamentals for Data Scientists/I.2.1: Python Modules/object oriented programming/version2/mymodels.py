#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[111]:


class myregression:
    def __init__(self):
        self.b_0=None
        self.b_1=None
    
    def __repr__(self):
        return 'my personal linear regression'
    
    def fit(self,X,Y):
        """
        This functions calculates the coefficients 
        of a linear regression with an intercept
        Y = b_0 + b_1 x
        """
        X_ones = np.ones(X.shape)
        X = np.vstack([ X_ones,X]).T
        Y = Y.T
        b = np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T),Y)
        b = b.reshape(-1,)
        self.b_0 = b[0]
        self.b_1 = b[1]
    
    def predict(self,X):
        """
        This function makes predictions
        """
        return X*self.b_1+self.b_0

