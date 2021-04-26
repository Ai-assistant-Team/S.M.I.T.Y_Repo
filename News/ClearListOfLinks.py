def clear_list_of_links(list_of_links):
    #create new list
    new_list_of_links = []
    #add every link only one time
    for link in list_of_links:
    #veriable that counts the times a link if found in the new list
        count = 0
        #temporaty veriable
        a = link
        for new_link in new_list_of_links:
        #temporaty veriable
            b = new_link
            if a == b :
                count= count + 1
        #if the link is not already in the list put it 
        if count == 0 and a.__contains__("https://www.news.gr/") and a > "https://www.news.gr/\n" and a.__contains__("/article/"):
            new_list_of_links.append(link)
    return new_list_of_links