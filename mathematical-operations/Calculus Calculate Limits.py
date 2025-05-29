#Create a code that can solve for calculus tasks.
#It can calculate the limit of a polynomial function, as well as some trigonometric functions

#Import the necessary libraries. For that, install sympy on PyCharm if you haven't already.
#In order to install, type 'pip install sympy' into the terminal
from sympy import symbols, sympify, limit, oo
from sympy import symbols, sympify, limit, oo, sin, cos, tan
# add other functions as needed
print("\nCalculate limits of polynomial functions as well as trigonometric functions.")
print("Please be aware that Euler's Number (e) won't work.\n\n")

#Define all symbols used in the expression
x = symbols('x')

#Get the numerator and denominator. User gets to decide the values
#'input' function enables input
num_input = input("Enter the value of the numerator (In terms of x): ")
den_input = input("Enter the value of the denominator (In terms of x): ")

try:
    numerator = sympify(num_input)
    denominator = sympify(den_input)
    expression = numerator / denominator
except Exception as e:
    print("Invalid expression.\n", e)
    exit()

#Get a limit point, which is the value x approaches
limit_point_value = input("Enter limit here: ")

#What to do if input of limit is infinity
if limit_point_value.lower() in ['inf', 'infinity']:
    limit_point = oo
elif limit_point_value.lower() in ['-inf', '-infinity']:
    limit_point = -oo
else:
    try:
        limit_point = float(limit_point_value)
    except ValueError:
        print("Invalid limit point.")
        exit()
#Direction for one-sided limits:
direction = input("Enter direction (default is both sides) [+ or -]: ")
direction = direction if direction in ['+', '-'] else None

#Compute the limit
try:
    result = limit(expression, x, limit_point, dir=direction)
    print("Limit of the function is:", result)
except Exception as e:
    print("Couldn't find the limit.", e)

