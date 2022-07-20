#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:59:05 2021
Last edited:  Wed July 20, 2022

@author: martin

Idea:
    1. Build a ML model using the House Price data.
       https://www.kaggle.com/c/house-prices-advanced-regression-techniques
    2. Build a Flask app that can take input from a user and make predictions.
    3. Deploy to Heroku.
"""

import dill
import gzip
import pandas as pd
import numpy as np

from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

X_train = pd.read_csv('data/train.csv')
y_train = X_train.pop('SalePrice').values

print(X_train.info())

categorical = ['MSSubClass', 'MSZoning', 'Neighborhood']
numeric = ['LotArea']

model = Pipeline([
        ('features', ColumnTransformer([
            ('categorical', OneHotEncoder(handle_unknown='ignore'),
             categorical),
            ('numeric', StandardScaler(), numeric)])),
        ('estimator', GridSearchCV(Ridge(),
                        param_grid={'alpha': np.logspace(-1,0.5,20)},
                        cv=5, verbose=1))
        ])

model.fit(X_train[categorical+numeric], y_train)
print(f'R^2 on training data: {model.score(X_train[categorical+numeric], y_train)}')
print(model.named_steps['estimator'].best_params_)

with gzip.open('models/model.dill.gzip', 'wb') as f:
    dill.dump(model, f, recurse=True)
