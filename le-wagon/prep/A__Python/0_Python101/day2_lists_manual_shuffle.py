import random
def  manual_shuffle(input):
    # print(len(input))

    A = input.copy()
    B = []
    
    counter = 0
    while (True in [ind != None for ind in A]):
        counter += 1
        randint = random.randint(0,len(A)-1)
        try:
            other = (A[randint])
        except:
            print('ERROR HERE: ' + str(randint))
        B.append(A[randint])
        temp = A[randint]
        A.remove(temp)
        # print(f'{counter} {randint}: {temp}')
    
    # print(B)
    return B

















# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import os

print("Testing your Shuffle's length:")
if len(manual_shuffle(list(range(20)))) == 20:
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's randomness:")
if manual_shuffle(list(range(100))) != manual_shuffle(list(range(100))):
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Shuffle's content vs. the original:")
if set(manual_shuffle(list(range(100)))) == set(range(100)):
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's destructiveness:")
test_list = list(range(10))
manual_shuffle(test_list)
if len(test_list) == 10:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's helper methods")
import dis
def list_method_calls(fn):
    methods = []
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for ix, instr in enumerate(instrs):
        if instr.opname=="CALL_METHOD":
            load_method_instr = instrs[ix + instr.arg + 1]
            methods.append(load_method_instr.argval)
    return methods

if "shuffle" not in list_method_calls(manual_shuffle):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

if "sort" not in list_method_calls(manual_shuffle):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    


