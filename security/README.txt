---------- 09/06/2021 ----------
text.py:
	encrypt : 
		Accepts two parameters. These are a cleartext (text to be encrypted) and a password (to be used for encryption)
		If successful, returns the ciphertext (str) that is derived from the cleartext
		If not successful, returns a programStateCode (int) that describes what went wrong

	decrypt :
		Accepts two parameters. These are a ciphertext (text to be decrypted) and a password (that was used for encryption)
		If successful, returns the cleartext (str) that is derived from the ciphertext
		If not successful, returns a programStateCode (int) that describes what went wrong

file.py:
	encrypt : 
		Accepts two parameters. These are the name of a file (file to be encrypted) and a password (to be used for encryption)
		If successful, returns a programStateCode (int) which indicates that the proccess has been successfully executed
		If not successful, returns a programStateCode (int) that describes what went wrong

	decrypt :
		Accepts two parameters. These are the name of a file (file to be decrypted) and a password (that was used for encryption)
		If successful, returns a programStateCode (int) which indicates that the proccess has been successfully executed
		If not successful, returns a programStateCode (int) that describes what went wrong