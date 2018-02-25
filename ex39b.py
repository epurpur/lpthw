climbing_areas = {
    'Blowing Rock': 'Classic Boulder',
    'Grandmother': 'Engine Block'
}

other_areas = {
    'Lost Cove': 'Patio Boulder'
}

#adds boulder problems to patio boulder in other_areas. overwrites if there is something already in dictionary
other_areas['Lost Cove'] = 'Kratos', 'Patio Arete', 'Matts Prow', 'Heinous Crimper', 'Crockers Crack', 'Stems and Caps'
#print (climbing_areas)

#print ("Blowing Rock has", climbing_areas['Blowing Rock'])
#for area, boulders in list(other_areas.items()):
#    print (f"{boulders} are in {area}.")

climbing_areas = climbing_areas.get('Grandmother')
if climbing_areas:
    print (climbing_areas)
if not climbing_areas:
    print (f"Sorry, that area doesn't exist")
