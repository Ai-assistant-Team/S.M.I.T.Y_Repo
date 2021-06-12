from ClearTheTxtOfLinks import clear_the_txt_of_links
from ClearTheTxtOfLinks import get_list_from_txt
from ClearTheTxtOfLinks import update_txt
from GetTitleFromArticle import get_title_from_article
import webbrowser


def get_news():
    news_titles =""
    list_of_links = []
    try:
        list_of_links = get_list_from_txt(list_of_links)
    except:
        return 8
    totall = int(list_of_links[0])
    used = int(list_of_links[1])
    start = int(list_of_links[2])
    end = int(list_of_links[3])
    
    if(used < totall):
        if (used + 5 < totall):
            step = 5
        else:
            step = totall-used

        for x in range(start,end+1):
            title_article =  get_title_from_article(list_of_links[x])
            if title_article == 10:
                return 10
            news_titles = news_titles + title_article + '\n'

        used = used +step
        start = start +step
        end = end +step
        list_of_links[1] = str(used) + '\n'
        list_of_links[2] = str(start) + '\n'
        list_of_links[3] = str(end) + '\n'
        a = update_txt(list_of_links)
        if a == 9:
            return 9
    else:
        news_titles = "No more news aveliable"
    return news_titles

def open_news_page(title):
    try:
        list_of_links = []
        list_of_links = get_list_from_txt(list_of_links)
        fount = 'no'
        end = int(list_of_links[1]) + 4
        for x in range(4,end):
            if (get_title_from_article(list_of_links[x]) == title):
                fount = 'yes'
                webbrowser.open_new_tab(list_of_links[x])
                break
        if fount == 'no':
            return 'Title not found'
        else:
            return 'Title found'
    except:
        return 10
