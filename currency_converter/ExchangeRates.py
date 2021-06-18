"""
Created on Sat May 8 
@author: Δημήτρης Σούμπασης
"""

from forex_python.converter import CurrencyRates

c = CurrencyRates()
#c1 = 'USD'  Currency you are converting from 
#c3= 'EUR'  Currency you are converting to
#c2= 'Euros'         c2 = Full name of the currency that the user wants to conver to 
#amount= the amount you are converting

def cconvert(c1, c2, amount):       #Converts the amount from currency 1 to currency 2
    try:
        fin=(c.convert(c1, c2, amount)) 
        fin= str(fin) + ' ' + c2
        return fin
    except:
        return 1
