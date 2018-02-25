# rules say that you can only date within a certain age range.
#Low end is half your age plus 7
#high end is twice your age minus 13

user_age = int(input('How old are you? '))

low_end = int((user_age / 2) + 7)
high_end = int((user_age * 2) - 13)

#low_end = ("Your low range is", int((user_age/2) + 7))
#high_end = ("Your high range is", int((user_age * 2) - 13))

print (f"You can date people between {low_end} and {high_end} years old.")
