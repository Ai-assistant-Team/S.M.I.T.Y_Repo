"""
Created on Sat May 8 
@author: Δημήτρης Σούμπασης
"""

from forex_python.converter import CurrencyRates

c = CurrencyRates()
#c1 = 'USD'  #Currency you are converting from 
#c2 = 'EUR'  #Currency you are converting to
#amount= the amount you are converting

def cconvert(c1, c2, amount):       #Converts the amount from currency 1 to currency 2
    try:
        fin=(c.convert(c1, c2, amount)) 
        return fin
    except:
        return 1
