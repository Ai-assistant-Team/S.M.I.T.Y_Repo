#https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
import pathlib
import requests
from bs4 import BeautifulSoup
from SMITY.definePATH import RESOURCES_PATH
import os

#add libraries

#difine costans
DIRNAME = 'News'
record_file = 'links.txt'

def create_txt_with_links():
    #creates links.txt with all the links from https://www.news.gr/
    try:
        #set url
        urls = 'https://www.news.gr/'
        #request urls
        grab = requests.get(urls)
        soup = BeautifulSoup(grab.text, 'html.parser')
        try:
            #find file
            filename = os.path.join(RESOURCES_PATH, DIRNAME, record_file)
            # opening a file in write mode
            f = open(filename, 'w')
            # traverse paragraphs from soup
            for link in soup.find_all("a"):
                data = link.get('href')
                f.write(data)
                f.write("\n")
            f.close()
            #if all good sed 0
            return 0
        except:
            return 9
        #return 9 if there is a problem writing the file
        return 0
    #if all good sed 0
    except:
        return 10
    #return 9 if there is a problem with the internrt conection


def update_txt(list_of_links):
    #updates links.txt
    try:
        #find links.txt
        location = os.path.join(RESOURCES_PATH, DIRNAME, record_file)
        #open links.txt
        file = open(location,'w')
        #update links.txt
        for link in list_of_links:
            file.write(link)
        # Closing file
        file.close
         #if all good sed 0
        return 0
    except:
        #return 9 if there is a problem writing the file
        return 9


def clear_the_txt_of_links():
    #clear links.txt from the unwanted links
    #open file
    try:
        #find links.txt
        location = os.path.join(RESOURCES_PATH, DIRNAME, record_file)
        #open links.txt
        file = open(location,'r')
        # initialize lists
        list_of_links = []
        new_list_of_links = []
        new_list_of_links2 = []
        #call get_list_from_txt 
        ex = get_list_from_txt(list_of_links)
        #if get_list_from_txt returns 8 return 8
        if ex == 8:
            return 8
        # Closing file
        file.close()
        #check for double links
        for link in list_of_links:
            #set for every link count = 0
            count = 0
             #put link in a
            a = link
            #run the lists
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
        file = open(location,'w')
        #write to file
        file.write(str(len(new_list_of_links2)))
        file.write('\n')
        file.write('0\n')
        file.write('4\n')
        file.write('9\n')
        for link in new_list_of_links2:
            file.write(link)
        # Closing file
        file.close
         #if all good sed 0
        return 0
    except:
        #return 9 if there is a problem writing the file
        return 9


def get_list_from_txt(list_of_links):
    #creates a list of links fom the txt file
    try:
        #find links.txt
        location = os.path.join(RESOURCES_PATH, DIRNAME, record_file)
        #open links.txt
        file = open(location,'r')
        for line in file:
            #add every line of the txt to the list
            list_of_links.append(line)
        return list_of_links
    except:
        return 8
        #return 8 if there is a problem reading the file
