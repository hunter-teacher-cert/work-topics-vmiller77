from flask import Flask, render_template
from flask import Flask, request,session 

import random
import re

app = Flask(__name__)
app.secret_key="something"

@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  return render_template("lucky.html",number = i)

@app.route("/")
def index():
  return "<h1>Hello World from my computer !</h1>"

@app.route("/mainPage")
def mainPage():
  user = { "username" : "Miguel"}
  return render_template("mainPage.html", title = "Home", user = user)

@app.route("/cond")
def conditionals():
  user = { "username" : "Maya"}
  return render_template("conditionals.html", title = "Home", user = user, myTitle ="Maya's Page")

@app.route("/loops")
def loops():
  user = {'username': 'Miguel'}
  posts = [
       {
           'author': {'username': 'John'},
           'body': 'Beautiful day in Portland!'
       },
       {
           'author': {'username': 'Susan'},
           'body': 'The Avengers movie was so cool!'
       }
  ]   
  return render_template('loops.html', title='Home', user=user, posts=posts)
  

@app.route("/inher")
def inher():
    user = {'username': 'Vic'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]   
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route("/form_demo",methods=['GET','POST'])
def form_demo():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("form_demo.html")
  else:
    # here we clicked the button
    # so we can check the form data
    name = request.form['username']
    pw = request.form['password']
    print(name,pw)
    if pw != "12345":
      error = "BAD PASSWORD"
      name=""
    else: 
      error = ""
      
    return render_template("form_demo.html",error=error, name=name)

      
    return render_template("homepage.html", name = name)

#At least 2 routes
#1 form you can submit (code should do something when you submit GET + POST in same route)
#Flask template with substitutions
#Some CSS
#At least one image
#1 ex of using flask session
#Readme to explain how to use your website + run app

# example of static content
# like an image or including css
@app.route("/image_css")
def image_css():
  idea = "Canned Bread"

  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1
    
  return render_template("image_css.html", idea = idea, count = session['count'])
    
@app.route("/kickstart",methods=['GET','POST'])
def kickstart():
  email = ""
  # GET is when we just load the page in our browser
  # POST is when we click the button
  idea = "Canned Bread"
  if request.method=="GET":
    return render_template("kickstart.html", idea = idea)
  else:
    # here we clicked the button
    # so we can check the form data
    email = request.form['email']
    #Checking to see if it is a match
    matched = re.match("[a-z]*[1-9]*@*[a-z]*\.[a-z]{2,}", email)
    is_match = bool(matched)
    
    if not is_match:
      confirm = "BAD EMAIL"
      name=""
    else: 
      confirm = "Nice! Speak to you soon!"
      
    return render_template("kickstart.html",confirm=confirm, idea = idea)

      
    return render_template("homepage.html", name = name)

@app.route("/session_demo")
def session_demo():

  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1

  return render_template('session_demo.html',count = session['count'])
  
app.run(host="0.0.0.0",port=5000,debug=True)