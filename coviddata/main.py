from flask import Flask,render_template,request
from flask import request
import csv
app = Flask(__name__)
 
@app.route('/')
def form():
    return render_template('form.html')
@app.route('/submitted', methods = ['POST', 'GET'])
def appenddata():
    
    name=request.form['theName']
    bloodgroup=request.form['bloodgroup']
    age=request.form['age']
    hospital=request.form['hospital']
    phnumber=request.form['phnumber']
    relationship=request.form['relationshipwithpatient']
    spo2=request.form['spo2']
    requirement=request.form['requirement']
    state=request.form['state']
    city=request.form['city']
    strings=f"{name},{bloodgroup},{age},{hospital},{state},{city},{phnumber},{relationship},{requirement},{spo2}"
    if request.method == 'POST':
        with open('nopol.txt', 'a+') as f:
            f.write(f"\n{str(strings)}" )
            # f.seek(0)
            # line=f.read()
    return render_template('try.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    # name=request.form['theName']
    # bloodgroup=request.form['bloodgroup']
    # age=request.form['age']
    # hospital=request.form['hospital']
    # phnumber=request.form['phnumber']
    # relationship=request.form['relationshipwithpatient']
    # spo2=request.form['spo2']
    # requirement=request.form['requirement']
    # state=request.form['state']
    # city=request.form['city']
    # strings=f"{name},{bloodgroup},{age},{hospital},{state},{city},{phnumber},{relationship},{requirement},{spo2}"
    if request.method == 'GET' or request.method=='POST':
        with open('nopol.txt', 'a+') as f:
            # f.write(f"\n{str(strings)}" )
            f.seek(0)
            line=f.read()
        results = []
        
        user_csv = line.split('\n')
        reader = csv.DictReader(user_csv)
        
        for row in reader:
            results.append(dict(row))

        fieldnames = [key for key in results[0].keys()]

        return render_template('data.html', results=results, fieldnames=fieldnames, len=len)   

    # return render_template('data.html', name=strings)




 
 
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)