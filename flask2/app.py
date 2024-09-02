
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    username = ''
    password = ''
    if request.method == 'POST':
        username = request.form['username']
        print(f'Username: {username}')
        password = request.form['password']
        print(f'Password: {password}')
    return render_template('login.html', username=username, password=password)

@app.route('/forgetpassword', methods=['GET', 'POST'])
def forgetpassword():
    emailid = ''
    
    if request.method == 'POST':
        emailid = request.form['emailid']
       
    return render_template('forgetpassword.html',emailid = emailid)

if __name__ == '__main__':
    app.run(debug=True)



