# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 07:50:18 2021

@author: Θόδωρος
"""

##links 
##https://cryptography.io/en/latest/fernet/
##https://bigprimes.org/
##https://stackoverflow.com/questions/60912944/unable-to-except-cryptography-fernet-invalidtoken-error-in-python

import cryptography
from produceFernet import produceFernet

class textSecurity:
    
    # private attribute
    __prime5dig = 47543
    
    def encrypt(self, clearText, aKey=''):
        ##
        ## This function is called with 3 parameters.
        ##      - aKey      : the password that the user wants to use
        ##      - clearText : the text the user wants to encrypt
        ##      - self      : python keyword (has the same use as "this" in Java). It is used to pass the item itself as a parameter, so that the item's attributes and methods can be used
        ##
        ## When called, after making the nessasery convertions, uses the Fernet function to produce the ciphertext that matches the cleartext
        ##
       
        try: 
            
           f = produceFernet(aKey, self.__prime5dig)                                    # calls the function to produce a Fernet function using the given key
           
           token = f.encrypt(clearText.encode('UTF-8'))                                 # uses the initialized algorithm to encrypt the cleartext. (first the cleartext is encoded using UTF-8)
           
           return token
       
        except:
            return 15                                                                   # 15 : Error While Encrypting
            
   
   #end of encrypt
   
    
    def decrypt(self, cipherText, aKey=''):
        ##
        ## This function is called with 3 parameters.
        ##      - aKey      : the password that the user wants to use
        ##      - clearText : the text the user wants to encrypt
        ##      - self      : python keyword (has the same use as "this" in Java). It is used to pass the item as a parameter, so that the item's attributes can be used
        ##
        ## When called, after making the nessasery convertions, uses the Fernet function to produce the ciphertext that matches the cleartext
        ## 
        ## Returns clearText if password -> correct 
        ## Returns None if password -> incorrect
        ##
        
        try:
        
            f = produceFernet(aKey, self.__prime5dig)                                  # calls the method to produce a Fernet function using the given key
            
            try:
                
                clearText = f.decrypt(cipherText)
                return clearText
            
            except (cryptography.fernet.InvalidToken, TypeError):
                
                return 17                                                              # 17 : Error Wrong Password
            
        except:
            return 16                                                                  # 16 : Error While Dencrypting
    
    #end of decrypt 
   
#end of textSecurity
