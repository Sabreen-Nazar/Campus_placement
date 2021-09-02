# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:54:07 2021

@author: AFNAN AFSHEEN
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:54:34 2021

@author: AFNAN AFSHEEN
"""

from flask import Flask,request
import joblib

algo1=joblib.load(r'C:\\Users\\AFNAN AFSHEEN\\OneDrive\\Desktop\\ineuron\\project2\\dtc.pkl')
pre1=joblib.load(r'C:\\Users\\AFNAN AFSHEEN\\OneDrive\\Desktop\\ineuron\\project2\\pre.pkl')

app=Flask(__name__)
@app.route('/',methods=['POST'])

def model2():
    data=request.get_json(force=True)
    data=[[data['gender'],
           data['ssc_p'],
           data['hsc_p'],
           data['hsc_s'],
           data['degree_p'],
           data['degree_t'],
           data['workex'],
           data['etest_p'],
           data['specialisation'],
           data['mba_p'],
           data['salary']]]
    

    print(data)
    data=pre1.transform(data)
    out=algo1.predict(data)
    return str(out)
 

app.run()

