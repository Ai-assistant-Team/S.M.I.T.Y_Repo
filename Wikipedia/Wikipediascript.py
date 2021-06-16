import wikipedia                                            # importing wikipedia module

##
## This function is searching wikipedia the thing you want to learn about
##

def Wiki_Search(toSearch):                                              # declaring a function
        try:                                                            # incase something goes wrong
            return(wikipedia.WikipediaPage(toSearch).summary)           # returns wikipedia info
        except Exception:                                               # 1 : Undefined Error
            return 1

#end of Wikipediascript
