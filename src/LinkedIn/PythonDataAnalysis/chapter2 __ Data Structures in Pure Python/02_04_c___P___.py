# ___PYTHONIC___ (___P___)) COMPREHENSIONS

#simplest thing, but can be very powerful:

# list of the squares from 1^2 to 10^2; note power is ** in Python
squares = [i**2 for i in range(1, 11)]
print(f"list: {squares}")

# list of the squares from 1^2 to 10^2, including only those divisible by 4
squares_by_four = [i**2 for i in range(1, 11) if i**2 % 4 == 0]
print(f"list: {squares_by_four}")

# dict of the squares from 1^2 to 10^2, where the keys are the unsquared numbers
squares_dict = {i: i**2 for i in range(1, 11)}
print(f"dict: {squares_dict}")

# dict by key, values:
capitals_by_country = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
countries_by_capital = {capital: country for country, capital in capitals_by_country.items()}
print(f"dict: {countries_by_capital}")

# sum across comprehensions too
x = sum(i**2 for i in range(1, 11))
print(f"sum is: {x}")

# nested comprehensions:
counting1 = []
for i in range(1, 11):
    for j in range(1, i+1):
        counting1.append(j)
counting2 = [j for i in range(1, 11) for j in range(1, i+1)]
print(f"counting1 via nested for loops: {counting1}")
print(f"counting2 via nested comprehension: {counting2}")

# hsth attempt 1
cut1 = [i for i in counting1 if i*2 not in counting2]
print(f"cut1 via comprehension: {cut1}")

# hsth attempt 2
cut2 = {i: j for i, j in capitals_by_country.items() if j != "Washington, DC"}
print(f"cut2 via comprehension?: {cut2}")
