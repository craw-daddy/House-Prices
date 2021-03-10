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

mszoning_types = [('A','Agriculture'), 
                  ('C','Commercial'),
                  ('FV', 'Floating Village Residential'),
                  ('I', 'Industrial'), 
                  ('RH', 'Residential High Density'),
                  ('RL', 'Residential Low Density'),
                  ('RP', 'Residential Low Density Park'), 
                  ('RM', 'Residential Medium Density')]

@app.route('/')
def index():
    return render_template('index-advanced.html', mszoning_types=mszoning_types)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        user_inputs = request.args
    elif request.method == 'POST':
        user_inputs = request.form

    #  Note:  It looks like column names must be in the same *order* they
    #  were in during the training step, as well as having the same number
    #  of columns as was present during training.  
    categorical = ['MSSubClass', 'MSZoning', 'Neighborhood']
    numeric = ['LotArea']
    data = {}
    try:
        for c in categorical:
            data[c] = [user_inputs.get(c.lower(), 'None')]
        for c in numeric:
            data[c] = [float(user_inputs.get(c.lower(), 0))]
    
    #  Get the right data type to match the training data as strings
    # and numbers are different data types and will be treated differently
    # by the OneHotEncoder in the ML pipeline. 
        data['MSSubClass'] = [int(d) for d in data['MSSubClass']]
    except ValueError:
        return 'One or more numeric values received non-numeric input!'
    
    print(data)
    data = pd.DataFrame(data)

    with gzip.open('models/model.dill.gzip', 'rb') as f:
        model = dill.load(f)
    
    return str(model.predict(data)[0])


if __name__ == '__main__':
    app.run()