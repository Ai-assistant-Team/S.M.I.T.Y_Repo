#https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
import pathlib
import requests
from bs4 import BeautifulSoup

def create_txt_with_links():
   urls = 'https://www.news.gr/'
   grab = requests.get(urls)
   soup = BeautifulSoup(grab.text, 'html.parser')

   # opening a file in write mode
   f = open("links.txt", "w")
   # traverse paragraphs from soup
   for link in soup.find_all("a"):
      data = link.get('href')
      f.write(data)
      f.write("\n")

   f.close()

def update_txt(list_of_links):

    location = pathlib.Path(__file__).parent.absolute()
    file = open('%s\\links.txt'%(location),'w')
    for link in list_of_links:
        file.write(link)
    # Closing file
    file.close


def clear_the_txt_of_links():
    #open file
    location = pathlib.Path(__file__).parent.absolute()
    file = open('%s\\links.txt'%(location))

    list_of_links = []
    new_list_of_links = []
    new_list_of_links2 = []

    get_list_from_txt(list_of_links)
    # Closing file
    file.close()
    #check for double links
    for link in list_of_links:
        count = 0
        a = link
        for new_link in new_list_of_links:
            b = new_link
            if a == b :
                count= count + 1
        #if the link is not already in the list put it 
        if count == 0 :
            new_list_of_links.append(link)
    for link in new_list_of_links:
        #temporary veriable
        a = link
        # if the link contains https://www.news.gr/ and bigger than https://www.news.gr/\n
        # to bee sure that the links are leading to ta sites articles only
        if(a.__contains__("https://www.news.gr/") and a > "https://www.news.gr/\n" and a.__contains__("/article/")):
            new_list_of_links2.append(a)
    #open file
    file = open('%s\\links.txt'%(location),'w')
    file.write(str(len(new_list_of_links2)))
    file.write('\n')
    file.write('0\n')
    for link in new_list_of_links2:
        file.write(link)
    # Closing file
    file.close

def get_list_from_txt(list_of_links):
    location = pathlib.Path(__file__).parent.absolute()
    file = open('%s\\links.txt'%(location))
    for line in file:
        list_of_links.append(line)
    return list_of_links

