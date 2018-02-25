def creepy(firstage, secondage):
    if firstage < secondage:
        low_end_younger = int((firstage / 2) + 7)
        high_end_younger = int((firstage * 2) - 13)
        print (secondage >= low_end_younger and secondage <= high_end_younger)
    elif secondage < firstage:
        low_end_younger = int((secondage / 2) + 7)
        high_end_younger = int((secondage * 2) - 13)
        print (firstage >= low_end_younger and firstage <= high_end_younger)
    else:
        print ("Equal ages")
        print (firstage == secondage)

#if dating is not creepy, returns True. If dating is creepy, returns False
#Think about this as: can they date?  If True, they can date. If False, they cannot.
creepy(18, 20)
