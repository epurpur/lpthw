#We are going to practice with strings, variables, functions, math, etc
print ("Let's practice everything.")
print ('You\'d need to know \'bout escapes with \\ that do:')
print ('\n newlines and \t tabs.')#skips line, indents with tab
#everything inside """ is string
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print ("-----------")
print (poem) #calls poem, which is string inside triple quotes
print ("-----------")

five = 10 - 2 + 3 - 6 #defines variable 5 as this math formula
print (f"This should be five: {five}") #calls variable 5 in script
#defines function secret_formula with argument started
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates #returns values for jelly_beans, jars, crates

start_point = 10000 #starting point for secret_formula defined as start_point
beans, jars, crates = secret_formula(start_point) #arguments beans, jars, crates = this function with argument start_point

#remember this is another way to format a string
print ("With a starting point of: {}".format(start_point))
#it's just like with an f"" string
print (f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
#now defines start_point as start_point / 10 (defined as 10000 earlier). You can redefine variables as script continues
start_point = start_point / 10

print ("We can also do that this way:")
formula = secret_formula(start_point) #defines formula as secret_formula with argument start_point
# this is an easy way to apply a list to a format string
print ("We'd have {} beans, {} jars, and {} crates.".format(*formula))
