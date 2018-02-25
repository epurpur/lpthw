
def functiontocallforlist(x):
    i = 1
    numbers = []

    while i < 30:
        print (f"At the top i is {i}")
        numbers.append(i)

        i = i * 3
        print ("Numbers now: ", numbers)
        print (f"At the bottom i is {i}")



functiontocallforlist(1)


i = 1
newvar = 40
numbers = []
while i < newvar: #compares i to newvar. While i < newvar...
    print (f"At the top i is {i}")
    numbers.append(i)

    i = i * 5
    print ("Numbers now: ", numbers)
    print (f"At the bottom i is {i}")

print ("The numbers: ")
for num in numbers:
    print(num)

i = 1
newvar = 40
twovar = 5
numbers = []
while i < newvar: #compares i to newvar. While i < newvar...
    print (f"At the top i is {i}")
    numbers.append(i)

    i = i * twovar #does math with variable instead of number (twovar in this case)
    print ("Numbers now: ", numbers)
    print (f"At the bottom i is {i}")

print ("The numbers: ")
for num in numbers:
    print(num)
