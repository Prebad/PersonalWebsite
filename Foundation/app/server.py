from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='/Users/yifeil/git/PersonalWebsite/Foundation/assets',
            template_folder='../templates')


@app.route('/hello')
def hello_world():
    return '吼吼吼田小桐'

@app.route('/2019')
def new_year():
    return render_template('2019.html')

@app.route('/y')
def trick():
    return render_template('trick.html')


@app.route('/')
def index():
    return render_template('statistic.html')


app.run(host='0.0.0.0')