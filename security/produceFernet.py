import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC #(Password Based Key Derivation Function 2)

def produceFernet(aKey, prime5dig):
    ##
    ## This function is called with the parameter aKey and uses it 
    ## to produce the Fernet function that will later be used to 
    ## encryption and decryption
    ##
    
    try:
    
        # prime5dig This is a constant used to produce the salt
        salt = prime5dig.to_bytes(16, 'big')                                     #I do not use random salt, because then I would have to save the salt value somewhere, 
                                                                                     #in order to be able to decrypt the encrypted message at any time
    
        password = aKey.encode('UTF-8')                                          #converts the key from string to binary
    
        
        kdf = PBKDF2HMAC(
            algorithm = hashes.SHA256(),
            length = 32,
            salt = salt,
            iterations = 100000
            )                                                                    #used to derive a cryptographic key from the password
               
        key = base64.urlsafe_b64encode(kdf.derive(password))                     #encodes the derived cryptographic key (from string to binary)
           
        f = Fernet(key)                                                          #initializes the algorithm using the key
            
        return f                                                                 #returns the produced Fernet function
    
    except Exception as e: 
        
        raise e

#end of produceFernet
