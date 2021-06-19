#https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
import pathlib
import requests
from bs4 import BeautifulSoup
from SMITY.definePATH import RESOURCES_PATH
import os

#add libraries

DIRNAME = 'News'

record_file = 'links.txt'

def create_txt_with_links():
    try:
        urls = 'https://www.news.gr/'
        grab = requests.get(urls)
        soup = BeautifulSoup(grab.text, 'html.parser')
        try:
            filename = os.path.join(RESOURCES_PATH, DIRNAME, record_file)
            # opening a file in write mode
            f = open(filename, 'w')
            # traverse paragraphs from soup
            for link in soup.find_all("a"):
                data = link.get('href')
                f.write(data)
                f.write("\n")
            f.close()
            return 0
        except:
            return 9
        return 0
    except:
        return 10


def update_txt(list_of_links):
    try:
        location = os.path.join(RESOURCES_PATH, DIRNAME, 'links.txt')
        file = open(location,'w')
        for link in list_of_links:
            file.write(link)
        # Closing file
        file.close
        return 0
    except:
        return 9


def clear_the_txt_of_links():
    #open file
    try:
        location = os.path.join(RESOURCES_PATH, DIRNAME, 'links.txt')
        file = open(location,'r')

        list_of_links = []
        new_list_of_links = []
        new_list_of_links2 = []

        ex = get_list_from_txt(list_of_links)
        if ex == 8:
            return 8
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
        file = open(location,'w')
        file.write(str(len(new_list_of_links2)))
        file.write('\n')
        file.write('0\n')
        file.write('4\n')
        file.write('9\n')
        for link in new_list_of_links2:
            file.write(link)
        # Closing file
        file.close
        return 0
    except:
        return 9


def get_list_from_txt(list_of_links):
    try:
        location = os.path.join(RESOURCES_PATH, DIRNAME, 'links.txt')
        file = open(location,'r')
        for line in file:
            list_of_links.append(line)
        return list_of_links
    except:
        return 8
