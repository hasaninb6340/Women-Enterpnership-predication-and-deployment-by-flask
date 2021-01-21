# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:20:28 2020

@author: M.Hasnain Baloch
"""


  
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def prediction():
     if request.method == 'POST':
        if(request.form['entrepreneurship']==""):
            Index=0
        else:    
            Index=float(request.form['entrepreneurship'])
        if(request.form['inflation']==""):
            rate=0
        else:
            rate=float(request.form['inflation'])
        Developement=0
        country=request.form['country']
        Developement=request.form['country_developed']
        if(Developement=='undereveloped'):
            Developement=1
        else:
            Developement=0
        Member=0
        Member=request.form['europe']
        if(Member=='notmember'):
            Member=1
        else:
            Member=0
      
        model = pickle.load(open('model.pkl', 'rb'))
        prediction=model.predict([[Index,rate,Developement,Member]])
        output=round(prediction[0],2)
        if(output>67):
            newtext="high force labor rate"
        else:
            newtext="not too high force labor rate"
        return render_template('index.html',prediction_text="The Women force labor rate is "+str(output)+" for "+str(country),prediction_text2=newtext)

if __name__=="__main__":
    app.run(debug=True)


