from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def view_homepage():
  return render_template('index.html')
  
@app.route('/about')
def view_aboutpage():
  return render_template('about.html')
