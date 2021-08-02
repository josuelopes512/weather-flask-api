from flask import Flask, render_template, request

import requests, os

app = Flask(__name__)

API_KEY=os.getenv('API_KEY')

@app.route('/')
def index():
    '''show index

    args: 
        name (string) \n
        id (int)
    
    
    notes: 
        function to return a index
    '''


    return render_template('index')

@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
        if 'cidade' in request.form:
            cidade = request.form['cidade']
        else:
            raise 'ERRO'
        URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade, API_KEY)
