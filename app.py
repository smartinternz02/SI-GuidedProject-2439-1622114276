# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:07:33 2021

@author: MARKALA MANASWINI
"""

import numpy as np
import joblib
import pandas as pd
from flask import Flask ,render_template,request
model=joblib.load('sales.sav')
app = Flask(__name__)
@app.route('/') 
def home():
    return render_template("predict.html")
@app.route('/predict',methods = ['POST'])
def predict():
    if request.method=="POST":
       ds = request.form["date"]
       a = {"ds":[ds]}
       ds=pd.DataFrame(a)
       pred=model.predict(ds)
       print(pred)
       output=round(pred.iloc[0,15])
       print(output)
       return render_template("predict.html",output="The sale value on selected date is {} thousands".format(output))

if __name__ == '__main__':
    app.run(debug = True)