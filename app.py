from flask import Flask
### WSGI Application
app = Flask(__name__)   #app name

@app.route('/')    #decorater     syntax: @app.route(url passed as string,options)
def welcome():
    return "Welcome Vennela. I am Flask!"     # whenever we go to the parricular page specified in the approute url, this method gets executed

@app.route('/members')                     # run url/members to execute this
def members():
    return "Welcome to all the members of Flask"

if __name__ == '__main__':      #name parameter passed on to app requires this
    app.run(debug=True)     # automatically updates as we modfiy the code


#There should be no ambiguity in function/method names