
def fizz_buzz(input):
    # print(input)
    output = []
    for i in range(1,input+1):
        if i % 5 == 0 and i % 3 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(i)
            
    # print(output)
    return output
    



















# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing your Answer:")
if len(fizz_buzz(5)) == 5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Fizz:")
if fizz_buzz(20).count('Fizz') == 5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Buzz:")
if fizz_buzz(33).count('Buzz') == 4:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your FizzBuzz:")
if fizz_buzz(50).count('FizzBuzz') == 3:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")