
#made by Giorgos

from googlesearch import search  # import the parts of the googlesearch that are needed


def searching(query=""):

    for i in search(query):
        print(i)                 # printing top ten results





def test():
    query = input("Enter your search: ")
    searching(query)
