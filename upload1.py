import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'your_secret_key_here'

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="forza"
)
cursor = db_connection.cursor()

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    return render_template('login.html')




@app.route('/upload', endpoint='upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    finally:
        db_connection.close()
