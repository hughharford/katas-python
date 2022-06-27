le_wagon_team = [
    {'name': 'ben', 'age': 31, 'country': 'france', 'hobbies': ['coding', 'biking']},
    {'name': 'quinn', 'age': 26, 'country': 'ireland', 'hobbies': ['skiing']},
    {'name': 'sasha', 'age': 24, 'country': 'lebanon', 'hobbies': ['sports']},
    {'name': 'alex', 'age': 28, 'country': 'austria', 'hobbies': []}
    ]
    
it = {'name': 'ben', 'age': 31, 'country': 'france', 'hobbies': ['coding', 'biking']}

# Print the type of `le_wagon_team` below
print(type(le_wagon_team))

# Print the type of one of the element inside `le_wagon_team` below
print(le_wagon_team[1])

print(len(le_wagon_team[1]))

print(le_wagon_team[0]['age'])

le_wagon_team[-1].update({'hobbies': ['video games']})
print(le_wagon_team[-1])


addition =	{
  'name': 'Rebecca',
  'age': 27,
  'country': 'Scotland',
  'hobbies': 'travel'
}

le_wagon_team.append(addition)

for i in range(len(le_wagon_team)):
    print(le_wagon_team[i]['name'] + ' (' + str(le_wagon_team[i]['age']) + ' years old)')
          

for i in range(len(le_wagon_team)):
    print(f"- {le_wagon_team[i]['name']} ({le_wagon_team[i]['age']} years old)") 
          
#({str(le_wagon_team[i]['age'])} years old))

def concatenate_strings(string_one, string_two):
    # TODO: Code the rest of the method below
	return f"{string_one} {string_two}"
	
print(concatenate_strings(a, b))

def longer_than_five(string):
    # TODO: Code the rest of the function below
    if len(string) > 5:
        return False
    else:
        return True

print(f"data: {longer_than_five('data')}")
print(f"science: {longer_than_five('science')}")

def pizza_time(number):
    # TODO: Code the rest of the function below
    for x in range(1, number+1):
        if x % 3 == 0 and x % 5 == 0:
            print('PizzaTime')
        elif x % 3 == 0:
            print('Pizza')
        elif x % 5 == 0:
            print('Time')
        else:
            print(x)
		
pizza_time(31)