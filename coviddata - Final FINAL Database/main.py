from flask import Flask,render_template,request,redirect
from flask import request
import csv
import random
from flask_pymongo import PyMongo
import flask
from get_png import getpngstr
app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb+srv://user:alpharomeo123@coviddata.89ulw.mongodb.net/coviddata?retryWrites=true&w=majority"
mongo = PyMongo(app)
db = mongo.db

datalist=[]


@app.route('/')#choose between volunteer, join team, and patien registration
def land():
    return render_template('landing.html')

def getlinks(state):#to get links to display(of resources) from database in @app.route('/resources')
    link_collection=db.statewiselinks
    for  y in link_collection.find({}, {f'{state}': True,"_id":False}):
            collections=(y[f"{state}"])
    return(collections)   


def appenddata(name,bloodgroup,age,hospital,state,city,phnumber,relationship,requirement,spo2):#append data to mongodb
    user_collection = db.users#append data to mongodb
    user_collection.insert({"Patient's Name":f"{name}",'Blood Group':f"{bloodgroup}",'Age':f"{age}",'Hospital':f"{hospital}",'State':f"{state}",'City':f"{city}",'Relationship with Patient':f"{relationship}",'Phone Number':f"{phnumber}",'Requirements':f"{requirement}",'Spo2 level':f"{spo2}"})


@app.route('/auth', methods = ['POST'])
def auth():
    return render_template('auth.html')

    
@app.route('/form',methods = ['POST'])#render the form
def form():
    return render_template('form.html')



@app.route('/resources', methods = ['POST'])# display all links and display a thank you note
def displaylinks():
    
    name=request.form['name']
    bloodgroup=request.form['bloodgroup']
    age=request.form['age']
    hospital=request.form['hospital']
    phnumber=request.form['phnumber']
    relationship=request.form['relationshipwithpatient']
    spo2=request.form['spo2']
    requirement=request.form['requirement']
    state=request.form['state']
    city=request.form['city']
    global datalist
    datalist=[name, bloodgroup, age, hospital, city, relationship, phnumber, requirement, spo2]
    appenddata(name, bloodgroup, age, hospital, state, city, phnumber, relationship, requirement, spo2)#append data to mongodb

    return render_template('submit.html',links=getlinks(state))


@app.route('/sharepost', methods=["POST"])
def image():
    global datalist
    return render_template("share.html", img_data=getpngstr(datalist))



@app.route('/data', methods = ['POST'])
def data():

    if flask.request.method == 'POST': #else return a page
        collection=[]
        user_collection=db.users
        for  y in user_collection.find({}, {'_id': False}):
            collection.append(y)
        fieldnames = [key for key in collection[0].keys()]
    return render_template('data.html', collection=collection, fieldnames=fieldnames, len=len)    




@app.route('/jointeam',methods=['POST'])
def jointeam():
    #redirect to form
    return redirect("http://www.example.com/")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
