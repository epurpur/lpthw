from sys import argv
from os.path import exists

script, from_file, to_file = argv
print (f"Copying from {from_file} to {to_file}")

open(from_file)
print (f"Here is what the existing file looks like: {from_file}")
#print (f"The input file is {len(from_file)} bytes long")
print (from_file.read())
