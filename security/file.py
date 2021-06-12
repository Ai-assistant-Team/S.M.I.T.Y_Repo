# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:15:17 2021

@author: Θόδωρος
"""

##links 
##https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
##https://bigprimes.org/

import cryptography

from produceFernet import produceFernet

class fileSecurity:
    
    # private attribute
    __prime5dig = 21187
   
    def encrypt(self, filename, aKey=''):
        ##
        ## This function is called with 3 parameters.
        ##      - aKey      : the password that the user wants to use
        ##      - filename  : the name of the file the user wants to encrypt
        ##      - self      : python keyword (has the same use as "this" in Java). It is used to pass the item itself as a parameter, so that the item's attributes and methods can be used
        ##
        ## When called, after making the nessasery convertions, uses the Fernet function to produce the ciphertext that matches the cleartext
        ##
        ##  Returns False if an error occures (usually fileNotFound)
        ##  Returns True if everything works as planned
        ##
        
        try:
            # opening the original file (not encrypted)
            try:
                with open(filename, 'rb') as file:
                    original = file.read()
                    
            except FileNotFoundError:
                return 3                                                            # 3 : File Not Found.
            except:
                return 8                                                            # 8 : Problem while reading file.
            
            f = produceFernet(aKey, self.__prime5dig)                               # calls the method to produce a Fernet function using the given key
            encrypted = f.encrypt(original)                                         # encrypting the file
            
             
            # opening the original file in write mode and writting the encrypted data
            try:
                with open(filename, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
            except:
                return 9                                                            # 9 : Problem while writing file.
            
            return 0                                                                # 0 : Successfully Executed.
        
        except Exception:
            return 1                                                                # 1 : Error. Something went wrong.
        
    #end of encrypt
    
    
    def decrypt(self, filename, aKey=''):
        
        try: 
            # opening encrypted file
            try:
                with open(filename, 'rb') as encrypted_file:
                    encrypted = encrypted_file.read()
                    
            except FileNotFoundError:
                return 3                                                                # 3 : File Not Found.
            except:
                return 8                                                                # 8 : Problem while reading file.
    
            try:
                f = produceFernet(aKey, self.__prime5dig)                               # calls the method to produce a Fernet function using the given key
                decrypted = f.decrypt(encrypted)                                        # decrypting file contents
                
            except (cryptography.fernet.InvalidToken, TypeError):
                return 17                                                               # 17 : Error. Wrong Password.
                
            # opening the encrypted file in write mode and writting the decrypted data
            try:
                with open(filename, 'wb') as decrypted_file:
                   decrypted_file.write(decrypted)
            
            except:
                return 16                                                               # 16 : Error While Dencrypting.
            
            
            return 0                                                                    # 0 : Successfully Executed.
        
        except:
            return 1                                                                    # 1 : Error. Something went wrong.
    
    #end of decrypt
    
#end of fileSecurity