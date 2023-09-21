from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)  # Print the parameter to the console
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    # Create a list of numbers as strings
    numbers = [str(num) for num in range(parameter)]
    
    # Join the numbers with '\n' to produce the correct newline format
    result = '\n'.join(numbers)
    
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
