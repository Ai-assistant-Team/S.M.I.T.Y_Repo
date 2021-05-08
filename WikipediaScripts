import wikipedia                                            # importing wikipedia module

##
## This function is searching wikipedia the thing you want to learn about
##

def Wiki_Search():                                          # declaring a function
    wiki = input('Please enter the wiki search: ')          # Type your search
    result = wikipedia.search(wiki)                         # recognizing wikipedia info

    for search in result:
        print(search)                                        # printing search
        print(wikipedia.page(search).summary)                # printing search

Wiki_Search()                                               # running Wiki_Search
