from flask  import Flask,render_template,url_for,request
import joblib
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib


import requests

from sklearn.feature_extraction.text import CountVectorizer
from gensim.summarization import summarize
app=Flask(__name__)
from text_sum import text_sumarize

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":

        message=request.form["message"]
        final_sumary=text_sumarize(message)
        #final_sumary=summarize(message)
    return render_template('result.html',ctext=message,final_sumary=final_sumary)

if __name__ == '__main__':
	app.run(debug=True)
