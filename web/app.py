from datetime import datetime

import flask
from flask import jsonify, request

app = flask.Flask(__name__)
results = []

@app.route("/operate", methods=["GET"])
def operate():

    if "operation" and "a" and "b" in request.args:
        try:
            operation = request.args["operation"]
            if operation not in "+-/**":
                raise ValueError()
            a = int(request.args["a"])
            b = int(request.args["b"])
        except ValueError as e:
            return dict(error="Entered operation values are not valid", message="Review operation parameters and try again"), 400
    else:
        return dict(error="Calculation Error", message="Invalid operation parameters"), 400
    result = 0
    # Check for the operation type and get the result
    try:
        if "+" in operation:
            result = a + b
        if "-" in operation:
            result = a - b
        if "*" in operation:
            result = a * b
        if "/" in operation:
            result = a / b
        if "**" in operation:
            result = a ** b
        response = {"updated_date": datetime.now(), "result": result, "a": a, "operation": operation, "b": b}
        results.append(response)
        return response, 200
    except Exception as e:
        return dict(error="Calculation Error, don't break me", exception=str(e), message="Review operation parameters and try again"), 400


@app.errorhandler(404)
def page_not_found(error):
    return dict(response="Welcome to the calculator, to use it add operator and a and b, you can use (+,-,/,*,**) (%2B,-,%2F,%2A,%2A%2A), exemple: operate?operation=%2b&a=2&b=2"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")
