
#tells python we want to make a function using def for "define"
#this one is like your scripts with argv
def print_two(*args): #gives function a name (print_two). *args- python takes arguments to the function and puts them in args as a list
    arg1, arg2 = args #everything in indention is attached to print_two
    print (f"arg1: {arg1}, arg2: {arg2}")

#Ok, that *args is actually pointless, we can just do this
def print_2_again(arg1, arg2):
    print (f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print (f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print ("I got nothin'.")

print_two("Zed", "Shaw")
print_2_again("Zed", "Shaw")
print_one("First!")
print_none()
