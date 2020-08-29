# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:35:16 2020

@author: Smizzy
"""


from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'));



@app.route('/',methods=['GET'])
def Home():
                                  return render_template('ins.html')
                                    



@app.route("/predict", methods=['POST'])
def predict():
                                       
                                        if request.method == 'POST':
                                                    
                                                    age=int(request.form['Age'])
                                                    bmi=float(request.form['BMI'])
                                                    ch = int(request.form['Number of Dependents'])
                                                    sex= str(request.form['Sex'])
                                                    if sex == 'Male':
                                                                    s = 0
                                                    else:
                                                            s=1
                                                    smoker=str(request.form['Smoking Habit'])
                                                    if smoker == 'yes':
                                                                s1 = 0
                                                    else:
                                                           s1=1
                                                    reg=str(request.form['Region'])
                                                    if reg == 'Northeast':
                                                                    r = 0
                                                    elif reg == 'Northwest':
                                                                    r = 1
                                                    elif reg == 'Southeast':
                                                                    r = 2
                                                    else:
                                                            r=3
                                                    
                                                    prediction= model.predict([[age,bmi,ch,s,s1,r]])              
                                                                                                                 
                                                    return render_template('ins.html',output=('The estimated premium is ${}').format(prediction[0].round(2)))
                                                 
        
       

if __name__=="__main__":
    app.run(debug=True)
