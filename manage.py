# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:23:43 2021

@author: MARKALA MANASWINI
"""
import numpy as np
import joblib
import pandas as pd
from flask import Flask ,render_template,request
import os
from gevent.pywsgi import WSGIServer
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
port=os.getenv('VCAP_APP_PORT','8080')
if __name__ == '__main__':
    app.secret_key=os.urandom(12)
    app.run(debug = True,host='0.0.0.0',port=port)
    
      