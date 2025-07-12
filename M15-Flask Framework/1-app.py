from flask import Flask
'''
it  create a instance of the Flask class,
which will be your WSGI(Wb Server Get Interface) application
'''

### WSGI Application 
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to this Flask Course"

@app.route("/index")
def index():
    return "welcome to the index page"

@app.route('/about')
def about():
    return "Welcome to about flask my self Amit Vishwakarma"



## create entry point of the code ie. main function

if __name__=="__main__":
    app.run(debug=True)