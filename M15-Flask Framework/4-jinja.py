## Building Dynamic URL
## Variable Rule
## jinja2 templet Engine

from flask import Flask, render_template, request

### jinja2 Templet Engine
"""
1. {{ varivle_name }}
2. {%...%} conditions, for loop
3. {#...#} this is for single line comment
"""

### WSGI Application 
app = Flask(__name__)

@app.route('/')
def welcome():
    return "this is landing page your welcome"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/form', methods=['GET','POST'])


@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template("form.html")

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template("result.html", results=res)


    ## Variable Rule
@app.route('/successRes/<int:score>')
def successRes(score):
    res = ""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp = {'score':score, 'result':res}
    return render_template("result1.html", results=exp)

## condtitions
@app.route('/successif/<int:score>')
def successif(score):
    return render_template("result2.html", results=score)

## create entry point of the code ie. main function
if __name__=="__main__":
    app.run(debug=True)