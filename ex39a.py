countries_ive_visited = {
    'Canada': 'CA',
    'Mexico': 'MX',
    'Norway': 'NO',
    'South Africa': 'SA',
    'Greece' : 'GR',
    'Spain' : 'SP',
    'Honduras': 'HON' #you can define it anything, 3 letters here
}

capital_cities = {
    'CA': 'Ottawa',
    'MX': 'Mexico City',
    'NO': 'Oslo',
}

capital_cities['GR'] = 'Athens'
capital_cities['SP'] = 'Madrid'
capital_cities['HON'] = 'Tegucigalpa'
capital_cities['SA'] = 'Cape Town', 'Pretoria', 'Bloemfontain'
"""
print ('-' * 10)
print (capital_cities['SA']) #prints them as string
print (capital_cities['HON'])

print ('-' * 10)
print ("Canada's abbreviation is: ", countries_ive_visited['Canada'])
print ("Norway's abbreviation is: ", countries_ive_visited['Norway'])

print ('-' * 10)
print ("Spain has: ", capital_cities[countries_ive_visited['Spain']])
print ("Mexico has: ", capital_cities[countries_ive_visited['Mexico']])

print ('-' * 10)
for x, y in list(capital_cities.items()):
    print (f"country {x} has {y} as a capital city.")

print ('-' * 10)
for x, y in list(countries_ive_visited.items()):
    print (f"{x} has the abbreviation {y}")

print ('-' * 10)
for x, y in list(capital_cities.items()):
    print (f"{y} is the capital city of {x}")
    print (f"and has capital city {capital_cities[x]}")
"""
print ('-' * 10)
countries_ive_visited = countries_ive_visited.get('Japan')
if not countries_ive_visited:
    print (f"Sorry, that country doesn't exist.")

capital_cities = capital_cities.get('Tokyo', 'Does not exist')
print (f"The food for city 'Tokyo' is : {capital_cities}")
