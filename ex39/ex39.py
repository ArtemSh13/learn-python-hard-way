# the scheme of relations of abbreviations with the names of countries
states = {
    'Russia': 'RU',
    'Germany': 'DE',
    'Uzbekistan': 'UZ',
    'Zimbabwe': 'ZW',
    'Turkey': 'TR'
}

# creating of base set of states and their several cities
cities = {'UZ': 'Gazli', 'TR': 'Sarigerme', 'DE': 'Munich', 'ZW': 'Gweru', 'RU': 'Moscow'}

# adding some cities

# output of some cities
print('-' * 10)
print("There is the next city in the ZW country: ", cities['ZW'])
print("There is the next city in the RU country: ", cities['RU'])

# output of some states
print('-' * 10)
print("The abbreviation of Turkey: ", states['Turkey'])
print("The abbreviation of Germany: ", states['Germany'])

# it is performed taking into account the country and the dictionary of cities
print('-' * 10)
print("There is the next city in Turkey: ", cities[states['Turkey']])
print("There is the next city in Germany: ", cities[states['Germany']])

# output of all state abbreviations
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} has the {abbrev} abbreviation')

# output of all cities
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'The {abbrev} state has the {city} city')

# and now both types of data at once
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} has the {abbrev} abbreviation')
    print(f'and has the {cities[abbrev]} city')

print('-' * 10)
# secure getting of a state abbreviation that doesn't exist
state = states.get('USA')

if not state:
    print('I\'m sorry, USA doesn\'t exist or destroyed.')

# getting of a city with default value
city = cities.get('US', 'not exist')
print(f'There is the next city in the \'US\' country: {city}')
