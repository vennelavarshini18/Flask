# Building URL Dynamically
# Flask variable rules and URL Building

from flask import Flask,redirect,url_for
# redirect will make sure that it will redirect to some success page or some fail page
# url_for : To create that particular url dynamically
app=Flask(__name__)

@app.route('/')   #decorator
def welcome():
    return 'Welcome Vennela!'

#Building URL dynamically
@app.route('/success/<int:score>')   # fetches score from url
def success(score):
    return "The Person has passed and the marks is "+ str(score)
#   return "<html><body><h1>The Result is passed</h1></body></html>"   # Can be used with html files or code also
@app.route('/failure/<int:score>')   # fetches score from url
def failure(score):
    return "The Person has failed and the marks is "+ str(score)

##Result checker
@app.route('/results/<int:marks>')   # fetches marks from url
def results(marks):
   result=""
   if marks<30:
       result='failure'
   else:
       result='success'
   return redirect(url_for(result,score=marks))  #redirect(url_for())  # It calls the specific results method


if __name__ == '__main__':
    app.run(debug=True)