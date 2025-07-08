# Integrating HTML with Flask
# HTTP verb GET and POST

from flask import Flask,redirect,url_for,render_template,request
# render_template helps to actually render html page
# request helps to actually read the posted values
app=Flask(__name__)

@app.route('/')   #decorator  # Can be termed as routes
def welcome():
    return render_template('index3.html')    # we need to have particular folder structure

@app.route('/success/<int:score>')   
def success(score):
    res=""
    if score>=30:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)
"""
@app.route('/failure/<int:score>')   
def failure(score):
    return "The Person has failed and the marks is "+ str(score)

##Result checker
@app.route('/results/<int:marks>')   
def results(marks):
   result=""
   if marks<30:
       result='failure'
   else:
       result='success'
   return redirect(url_for(result,score=marks))  
"""
##Result checker submit html page
@app.route('/submit',methods=['POST','GET'])   # /submit should match with action specifiedin html page
def submit():
    total_avg_score=0
    if request.method=='POST':   # method 
        science=float(request.form['science'])   # name form html page
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_avg_score=(science+maths+c+datascience)/4

    return redirect(url_for('success',score=total_avg_score))  

if __name__ == '__main__':
    app.run(debug=True)