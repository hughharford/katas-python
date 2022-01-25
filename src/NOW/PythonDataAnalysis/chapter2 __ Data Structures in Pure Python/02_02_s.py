
print("LISTS")

nephews = ["Huey", "Dewey", "Louie"]
for i in range(len(nephews)):
    nephews[i] = nephews[i] + ' Duck'
nephews.append('April Duck')
ducks = nephews + ['Daisy Duck','Donald Duck']
ducks.sort()
print(ducks)
reverse_ducks = sorted(ducks, reverse=True)
print(reverse_ducks)
# print("\n")

print("SLICING")
squares = [1,4,9,16,25,36,49]
print(squares[3:])
print(squares[-3:])
print(squares[-3:-1])

print("TUPLE UNPACKING (pythonic)")
def three_args(a, b, c):
    print(a, b, c)
    
my_args = (1,2,3)
three_args(*my_args)