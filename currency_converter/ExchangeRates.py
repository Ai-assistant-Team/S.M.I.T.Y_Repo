"""
Created on Sat May 8 
@author: Δημήτρης Σούμπασης
"""

from forex_python.converter import CurrencyRates

c = CurrencyRates()
currency1 = 'USD'  #Currency you are converting from 
currency2 = 'EUR'  #Currency you are converting to



def currencyconverter(currency1, currency2):
    print(c.get_rate(currency1, currency2))

currencyconverter(currency1, currency2)