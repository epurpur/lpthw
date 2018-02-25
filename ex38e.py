list1 = 'one two three four five six'
newlist = list1.split(' ')
print (newlist)
list2 = ['seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

for number in list2:
    print ("Adding number ", number)
    newlist.append(number)
