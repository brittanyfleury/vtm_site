from cmath import pi
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance ')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Vertical Tank Maintenance')

@app.route('/estimate', methods=['POST'])
def estimate():
    estimate= " "
    if request.method=="POST" and 'tank_radius' in request.form and 'tank_height' in request.form:
        radius=float(request.form.get('tank_radius'))
        height=float(request.form.get('tank_height'))
        area_tank_top= pi* radius^2
        area_sides=2(pi(radius*height))
        total_area= area_tank_top + area_sides
        square_feet= total_area/144
        material_cost= square_feet*25
        labor_cost= square_feet*15
        total_estimate= material_cost+ labor_cost
    return render_template('estimate.html', pageTitle=' VTM Estimator', estimate=total_estimate)
   


if __name__ == '__main__':
    app.run(debug=True)
