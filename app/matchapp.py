from flask import Flask, render_template, url_for

app = Flask(__name__) #name of module

#what we type into our browser to go to different pages
@app.route("/") #home page
def welcome():
    return render_template('index.html') #name of home html file --> will change as front end is developed