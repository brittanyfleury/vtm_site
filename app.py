from cmath import pi
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance ')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Vertical Tank Maintenance')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html', pageTitle=' VTM Estimator')
   


if __name__ == '__main__':
    app.run(debug=True)
