#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:04:55 2021

@author: martin
"""

from flask import Flask, render_template, request

import pandas as pd
import gzip
import dill

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    user_inputs = request.args

    #  Note:  It looks like column names must be in the same *order* they
    #  were in during the training step, as well as having the same number
    #  of columns as was present during training.  
    categorical = ['MSSubClass', 'MSZoning', 'Neighborhood']
    numeric = ['LotArea']
    data = {}
    for c in categorical:
        data[c] = [user_inputs.get(c.lower(), 'None')]
    for c in numeric:
        data[c] = [float(user_inputs.get(c.lower(), 0))]
    
    #  Get the right data type to match the training data as strings
    # and numbers are different data types
    data['MSSubClass'] = int(data['MSSubClass'])
    
    print(data)
    data = pd.DataFrame(data)

    with gzip.open('models/model.dill.gzip', 'rb') as f:
        model = dill.load(f)
    
    return str(model.predict(data)[0])


if __name__ == '__main__':
    app.run()