# Put your app in here.
from flask import Flask,request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/math/add')
def doadd():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a+b)
    return str(result)

@app.route('/math/sub')
def dosub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a+b)
    return str(result)

@app.route('/math/mult')
def domult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a+b)
    return str(result)

@app.route('/math/div')
def dodiv():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a+b)
    return str(result)

operators = {
    "add"=add,
    "sub"=sub,
    "mult"=mult,
    "div"=div
}

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)