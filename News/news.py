from ClearTheTxtOfLinks import clear_the_txt_of_links
from ClearTheTxtOfLinks import get_list_from_txt
from ClearTheTxtOfLinks import create_txt_with_links
from ClearTheTxtOfLinks import update_txt
from getTitleFromArticle import get_title_from_article


def get_news():
    news_titles =""
    create_txt_with_links()
    clear_the_txt_of_links()
    list_of_links = []
    list_of_links = get_list_from_txt(list_of_links)
    totall = int(list_of_links[0])
    num_of_pages = int(list_of_links[1])
    links_sended = num_of_pages
    
    if(int(num_of_pages) + 5 < totall):
        num_of_pages = num_of_pages + 5
        start = num_of_pages + 3
        for x in range(start,totall):
            #news_titles = news_titles + get_title_from_article(list_of_links[x]) + '\n'
            news_titles = news_titles + get_title_from_article(list_of_links[x]) + '\n'
            links_sended = links_sended +1
            if links_sended == num_of_pages:
                break
    
    list_of_links[1] = str(links_sended) + '\n'
    update_txt(list_of_links)
    return news_titles
