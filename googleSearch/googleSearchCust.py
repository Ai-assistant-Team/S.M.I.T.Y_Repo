
#made by Giorgos

from googlesearch import search       # import the parts of the googlesearch that are needed

from urllib.request import urlopen

def searching(query=''):
    try:
        for i in search(query, num_results=3):    #By default, googlesearch returns 10 results,this can be changed by using the variable num_reseult
            print(i)                 # printing top three results
        
            return 0

    except:
        if internet_on():
            return 10
            


        
        
def internet_on():                                                  #this function checks the internet connection locally
   try:
        urlopen('https://www.google.com/', timeout=10)
        return False
   except:
        return True
