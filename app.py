#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
See this website where I have gotten the data from:
https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data

Created on Wed Aug 26 11:11:36 2020

@author: martin
"""

from flask import Flask, render_template, request

import pandas as pd
import gzip
import dill

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')  

@app.route("/about/")
def about():
    return "This website is to demonstrate my cool machine learning prediction method.  Isn't this great?"

@app.route("/predict/", methods=["GET"])
def predict():
    try:
        MSZoning = request.args.get('mszoning')
        MSSubClass = float(request.args.get('mssubclass'))
        LotArea = float(request.args.get('lotarea'))
    except ValueError:
        return 'One or more values are non-numeric!'
    
    data = pd.DataFrame({'MSZoning': [MSZoning],
                         'MSSubClass': [MSSubClass],
                         'LotArea': [LotArea]})
    with gzip.open('models/model.dill.gzip', 'rb') as f:
        model = dill.load(f)
        
    prediction = str(model.predict(data)[0])
    
    return prediction

#http://127.0.0.1:5000/predict/?mszoning=123.45fhjdhjfdhj&mssubclass=something

if __name__ == "__main__":
    app.run()
    