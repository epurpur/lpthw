classic_areas = 'Linville Gorge  Rocktown  Fontainebleau  Horseshoe Canyon Ranch  Kalymnos  Siurana'
split_areas = classic_areas.split('  ')
#print (split_areas)

other_classic_areas = ['Rifle', 'Red River Gorge', 'Joshua Tree', 'Red Rocks', 'Devils Lake', 'Horse Pens 40']


for area in other_classic_areas:
    print ("Adding ", area)
    split_areas.append(area)

print (split_areas)

#total_areas = split_areas + other_classic_areas
#print (total_areas)
