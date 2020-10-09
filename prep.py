#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
See this website where I have gotten the data from:
https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
    
Created on Wed Aug 26 11:10:23 2020

@author: martin

A file to prepare a model for deployment.  
"""

import pandas as pd
import numpy as np

from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

import gzip
import dill

X_train = pd.read_csv('data/train.csv')
y_train = X_train.pop('SalePrice').values

model = Pipeline([
        ('features', ColumnTransformer([
                ('categorical', OneHotEncoder(handle_unknown='ignore'), 
                     ['MSZoning']),
                ('numeric', StandardScaler(), ['MSSubClass', 'LotArea'])])),
        ('estimator', GridSearchCV(Ridge(), 
                    param_grid={'alpha': np.logspace(-2, 3, 20)}, 
                                   cv=5, n_jobs=2, verbose=1))
])

print(X_train['MSZoning'].unique())

model.fit(X_train[['MSZoning','MSSubClass','LotArea']], y_train)
print(model.score(X_train[['MSZoning','MSSubClass','LotArea']], y_train))

with gzip.open('models/model.dill.gzip', 'wb') as f:
    dill.dump(model, f, recurse=True)
    