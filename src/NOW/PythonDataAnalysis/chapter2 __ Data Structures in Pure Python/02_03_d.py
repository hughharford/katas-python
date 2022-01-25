print("DICTS")
capitals = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
print(capitals)

capitals['Spain'] = 'Madrid'
morecapitals = {'Germany': 'Berlin', 'United Kingdom': 'London'}
capitals.update(morecapitals)
print(capitals)

del capitals['United Kingdom']
print(capitals)

for country in capitals:
    print(country)
    
for country, capitals in capitals.items():
    print(country, capitals)