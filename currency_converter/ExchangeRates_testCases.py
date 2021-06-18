from os import time
from ExchangeRates import cconvert


def cctest():
  
    #made by Δημήτριος Σούμπασης
    
    print (cctestCase1())
    time.sleep(1)
    print (cctestCase2())
    time.sleep(1)   
    print (cctestCase3())
    time.sleep(1)
    print (cctestCase4())
    time.sleep(1)
    print (cctestCase5())
    time.sleep(1)
    print (cctestCase6())
    time.sleep(1)
    print (cctestCase7())
    time.sleep(1)
    print (cctestCase8())
    time.sleep(1)
    print (cctestCase9())



def cctestCase1():
    #made by Δημήτριος Σούμπασης

    #Should try to use the function without giving any feedback
    return cconvert()


def cctestCase2():
    #made by Δημήτριος Σούμπασης
    #Should try to use the script with only the c1 parameter filled 
    return cconvert('USD')

def cctestCase3():
    #made by Δημήτριος Σούμπασης

    #Should try to use the script with only the c1 parameter filled 
    return cconvert('USD','EUR')

def cctestCase4():
    #made by Δημήτριος Σούμπασης

    #Should try to use the script with all parameters filled correctly
    return cconvert('EUR', 'USD', amount)

#end of cctestCase4

def cctestCase5():
    #made by Δημήτριος Σούμπασης

    #Should try to use the script with only the amount parameter filled correctly
    return cconvert('', '', amount)

#end of cctestCase5

def cctestCase6():
    #made by Δημήτριος Σούμπασης

    #Should try to use the script with the c1 and amount parameters filled correctly
    return cconvert('USD', '', amount)

#end of cctestCase6

def cctestCase7():
    #made by Δημήτριος Σούμπασης

    #Should try to use the script with the c2 and amount parameters filled correctly
    return cconvert('', 'AUD', amount)

#end of cctestCase7

def cctestCase8():
    #made by Δημήτριος Σούμπασης

    #Should try to use the script with the c1 and c2 parameters filled correctly and not giving the amount
    return cconvert('USD','EUR')

#end of cctestCase8

def cctestCase9():
    #made by Δημήτριος Σούμπασης

    #Should try to use the script with only the c1 parameter filled correctly
    return cconvert('AUD', '', '')

#end of cctestCase9

##Execution

cctest()
