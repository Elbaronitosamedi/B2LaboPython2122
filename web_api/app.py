from flask import Flask,render_template,request,session,redirect
import requests
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "Yes"


@app.route('/', methods=['GET','POST'])		
def index():
    params = {
        'access_key': 'e2f8989e7bf04e428b2e4e865cb621b4',
        'query': 'Bordeaux'
    }
    if  request.method == 'POST':
        params['query'] = request.form['city']
    
    response = requests.get('http://api.weatherstack.com/current', params)
    data = response.json()
    print(data)
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)