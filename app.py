#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:04:55 2021
Last updated Tue July 26, 2022.

@author: martin
"""

import gzip
import dill
import pandas as pd

from flask import Flask, render_template, request
from categories import MSSubClass_types, MSZoning_types, Neighborhood_types

app = Flask(__name__)

@app.route('/')
def index():
    """Show the main webpage."""
    return render_template('index.html',
                           MSSubClass_types=MSSubClass_types,
                           MSZoning_types=MSZoning_types,
                           Neighborhood_types=Neighborhood_types)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Provide prediction to user based on supplied values."""
    if request.method == 'GET':
        user_inputs = request.args
    elif request.method == 'POST':
        user_inputs = request.form

    #  Note:  It looks like column names must be in the
    # same *order* they were in during the training step.
    categorical = ['MSSubClass', 'MSZoning', 'Neighborhood']
    numeric = ['LotArea']
    data = {}
    try:
        for c in categorical:
            data[c] = [user_inputs.get(c, 'None')]
        for c in numeric:
            data[c] = [float(user_inputs.get(c, 0))]

    #  Get the right data type to match the training data
    # as strings and numbers are different data types and
    # will be treated differently by the OneHotEncoder
    # in the ML pipeline.
        data['MSSubClass'] = [int(d) for d in data['MSSubClass']]
    except ValueError:
        return 'One or more numeric values received non-numeric input!'

    data = pd.DataFrame(data)
    with gzip.open('models/model.dill.gzip', 'rb') as f:
        model = dill.load(f)

    return str(model.predict(data)[0])

if __name__ == '__main__':
    app.run()
