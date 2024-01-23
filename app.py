from flask import Flask, render_template, request
import pickle
import sklearn
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer , TfidfVectorizer 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/plot')
def second_page():
    return render_template('bar.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    input_text = str(request.form.get('input_text'))
    with open('models.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
    with open('vectors.pkl', 'rb') as file:
        loaded_vector = pickle.load(file)
    vector=loaded_vector['Vector']
    df=pd.DataFrame([input_text],columns=["Message"])
    input_data_spam=vector.transform(df["Message"])
    result = loaded_data['nb'].predict(input_data_spam)[0]
    return render_template('page.html', input_text=input_text, result=result)

app.run(debug=True)
