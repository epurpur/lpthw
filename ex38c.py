classic_areas = 'Linville Gorge  Rocktown  Fontainebleau  Horseshoe Canyon Ranch  Kalymnos  Siurana'
split_areas = classic_areas.split('  ')
other_classic_areas = ['Rifle', 'Red River Gorge', 'Joshua Tree', 'Red Rocks', 'Devils Lake', 'Horse Pens 40']

if len(split_areas) < 10: #if/else loop doesn't work like this because it only pops off 1 area
    next_area = other_classic_areas.pop()
    split_areas.append(next_area)
else:
    print ("List Full")
print (split_areas)
