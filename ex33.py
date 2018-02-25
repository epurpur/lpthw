i = 1
numbers = []

while i < 30:
    print (f"At the top i is {i}")
    numbers.append(i)

    i = i * 3
    print ("Numbers now: ", numbers)
    print (f"At the bottom i is {i}")

print ("The numbers: ")

for numb in numbers:
    print (numb)
