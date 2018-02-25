# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:40:18 2016

@author: lpa2a
"""

class Jedi:     #creates class, Jedi

    def __init__(self,lc='blue',m='Yoda',a='light'):   #initiates class with self, lc, m, a as arguments
        self.lightsabre_color = lc   #lightsaber color
        self.master = m       #master's name
        self.alignment = a        #alignment

    def use_force_lightning(self):
        if self.alignment == 'light':
            return 'I refuse, that is the way of the dark side.'
        else:
            return 'with pleasure!'

ObiWan = Jedi('blue','Yoda','light')  #defines ObiWan as Jedi with blue, Yoda, light as arguments for lightsabre_color, master, alignment
print (ObiWan.use_force_lightning()) #ObiWan uses use_force_lightning.  Because he is "light", prints "I refuse, that is the way of the dark side."
DarthVader = Jedi('red','obiWan','dark')  #defines DarthVader as Jedi with red, ObiWan, Dark as arguments
print (DarthVader.use_force_lightning())  #DarthVader use_force_lightning. should return "with pleasure"
rando=Jedi() #defines rando as class Jedi
print (rando.lightsabre_color)
print (rando.use_force_lightning())
