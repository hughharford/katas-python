# Implement your simple_calculator function below
def simple_calculator(input):
    output = 9999

    if len(input) != 3:
        return 'Please enter valid format: [Operand, Operator, Operand]'
    else:
        op1 = input[0]
        oper = input[1]
        op2 = input[2]
        
    if not oper in '+-*/%':
        return 'Please enter a valid operator [ +, -, /, *, % ]'
    if op1 != '' and op2 != '':
        opa = float(op1)
        opb = float(op2)
        if oper == '+':
            output = opa + opb
        elif oper == '-':
            output = opa - opb
        elif oper == '*':
            output = opa * opb
        elif oper == '/':
            output = opa / opb
        elif oper == '%':
            output = opa % opb

    return output









# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing your function's addition:")
if simple_calculator(['5', '+', '5']) == 10:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's subtraction:")
if simple_calculator(['10.5', '-', '5']) == 5.5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's multiplication:")
if simple_calculator(['8', '*', '8']) == 64:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your function's division:")
if simple_calculator(['1', '/', '4']) == 0.25:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your function's modulo:")
if simple_calculator(['9', '%', '2']) == 1:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's error handling:")
if simple_calculator(['1', '4']) == 'Please enter valid format: [Operand, Operator, Operand]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
if simple_calculator(['1', '4', '5', '+']) == 'Please enter valid format: [Operand, Operator, Operand]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
if simple_calculator(['1', '&', '5']) == 'Please enter a valid operator [ +, -, /, *, % ]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    