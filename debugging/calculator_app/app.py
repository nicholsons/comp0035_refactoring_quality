from flask import Flask, render_template, request
from flask_testing import LiveServerTestCase

from calculator import Calculator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('calculator.html')


@app.route('/result', methods=['POST'])
def result():
    first_term = request.form.get("first_term", type=int)
    second_term = request.form.get("second_term", type=int)
    operation = request.form.get("operation")
    c = Calculator(first_term, second_term)
    if operation == 'Add':
        result = c.add()
    elif operation == 'Subtract':
        result = c.subtract()
    elif operation == 'Multiply':
        result = c.multiply()
    elif operation == 'Divide':
        result = c.divide()
    else:
        result = 'INVALID CHOICE'
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
