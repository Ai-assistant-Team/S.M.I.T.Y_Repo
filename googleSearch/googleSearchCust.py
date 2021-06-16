
#made by Giorgos

from googlesearch import search       # import the parts of the googlesearch that are needed

from urllib.request import urlopen

def searching(query=''):
    try:
        for i in search(query):
        print(i)                 # printing top ten results
        
        return 0

    except:
        if internet_on():
            return 10
            


        
        
def internet_on():
   try:
        response = urlopen('https://www.google.com/', timeout=10)
        return False
    except: 
        return True
