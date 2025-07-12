from flask import Flask, render_template, request
'''
it  create a instance of the Flask class,
which will be your WSGI(Wb Server Get Interface) application
'''

### WSGI Application 
app = Flask(__name__)

@app.route('/')
def welcome():
    return "this is landing page your welcome"

@app.route("/index")
def index():
    return "<html><h1> Welcome to the 'Flask framework' cource </h1></html>"

@app.route('/about')
def about():
    return render_template("about.html") ## separate htlm
    ## creat a templates folder to contain about.html file



## create entry point of the code ie. main function
if __name__=="__main__":
    app.run(debug=True)