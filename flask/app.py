from flask import Flask,render_template,request

# Create a Flask application instance
app = Flask(__name__)
print("Checking name",__name__)

# Define a route and a view function
@app.route('/')
def main():
    return render_template('index.html',name = 'Rani',colgname = 'VIET',passout = 2010)

@app.route('/a')
def Flaskconcept():
    return render_template('index.html',name = 'Elayamani',colgname = 'CEG',passout = 2011)

@app.route('/b')
def friend():
    return '<p>Name Elayamani</p>'

@app.route('/si')
def calculation():
    return render_template('si.html')


@app.route('/calculator', methods=['POST'])
def calc():
    print("checking", request.form)
    principal = int(request.form['principal'])
    rate_of_interest =float(request.form['Rate_Of_Interest'])
    year = int(request.form['Year'])
    si = (principal * rate_of_interest * year)/100
    return f'Simple Interest is: {si}'
 


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True,port=1987)
