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
    return render_template("index.html")

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template("form.html")

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template("form.html")



## create entry point of the code ie. main function
if __name__=="__main__":
    app.run(debug=True)