from ClearTheTxtOfLinks import clear_the_txt_of_links
from ClearTheTxtOfLinks import get_list_from_txt
from ClearTheTxtOfLinks import update_txt
from GetTitleFromArticle import get_title_from_article
from SMITY.openUrls import openUrl
#add libraries


def get_news():
    #returns 5 tiles of atricles in str form
    try:
        #initialize
        news_titles =""
        list_of_links = []
        try:
            #call get_list_from_txt(list_of_links)
            list_of_links = get_list_from_txt(list_of_links)
        except:
            return 8
        #totall links
        totall = int(list_of_links[0])
        #links that the user have seen
        used = int(list_of_links[1])
        #the number of the line of the first lin that it is going to return
        start = int(list_of_links[2])
        #the number of the line of the last lin that it is going to return
        end = int(list_of_links[3])

        if(used < totall):
            #if the links that the user has already seen is less than the totall news
            if (used + 5 < totall):
                #if the links that the user has already seen plush the 5 links that is going to see are less than the totall news
                step = 5
            else:
                #if the remaining links are less than 5
                step = totall-used

            for x in range(start,end):
                #turn links in to tiltles
                title_article =  get_title_from_article(list_of_links[x])
                if title_article == 10:
                    return 10
                news_titles = news_titles + title_article + '\n'
            #increas the used links
            used = used +step
            #increas the line of the first link
            start = start +step
            #increas the line of the last link
            end = end +step
            #write the rest links number
            list_of_links[1] = str(used) + '\n'
            #write the next first link number
            list_of_links[2] = str(start) + '\n'
            #write the next last link number
            list_of_links[3] = str(end) + '\n'
            #call update_txt(list_of_links)
            a = update_txt(list_of_links)
            if a == 9:
                #return 9 if there is a problem writing the file
                return 9
        else:
            #if there is no more titles aveliable
            news_titles = "No more news aveliable"
        return news_titles
    except:
        return 1  #return 9 if something went wrong

def open_news_page(title):
    try:
        list_of_links = []
        list_of_links = get_list_from_txt(list_of_links)
        fount = 'no'
        end = int(list_of_links[1]) + 4
        for x in range(4,end):
            if (get_title_from_article(list_of_links[x]) == title):
                fount = 'yes'
                o = openUrl(list_of_links[x])
                if o == 14:
                    return 14
                break
        if fount == 'no':
            return 'Title not found'
        else:
            return 'Title found'
    except:
        return 10
