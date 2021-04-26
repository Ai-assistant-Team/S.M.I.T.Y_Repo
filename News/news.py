from CreateListWithLinks import create_list_with_links
from ClearListOfLinks import clear_list_of_links
from GetTitleFromArticle import get_title_from_article
import webbrowser

def test(list_of_links):
    #gets all the links from the wensite
    list_of_links = create_list_with_links(list_of_links)
    #keeps only the links of articles
    list_of_links = clear_list_of_links(list_of_links)
    #a=0
    answer = input("1. Get every link\n2. Get every atricles title\n3. Get one article for every category\n4. Get a specific number of news\n5. Get news of a specific category\n0. Termination\n")
    while 5>4:
        if answer == "1":
            print_all_links(list_of_links)
        elif answer == "2":
            print_all_titles(list_of_links)
        elif answer == "3":
            get_one_of_everything(list_of_links)
        elif answer == "4":
            get_some_news(list_of_links)
        elif answer == "5":
            get_news_by_category(list_of_links)
        elif answer == "0":
            #Terminate program
            break
        else:
            #wrong input scenario
            print("Wrong Input Idiot, Try Again")
        answer = input("\n1. Get every link\n2. Get every atricles title\n3. Get one article for every category\n4. Get a specific number of news\n5. Get news of a specific category\n0. Termination\n")
    print("Done")

def go_to_link(list_of_all_links,list_of_links,last_number):
    while 5>4:
        links = input("which ones shall i open ? ")
        links = links.split()
        for link in links:
            #str -> int -> int -1 ->str
            link = str(int(link)-1)
        #Termination veriable
        valid_form = "Yes"
        for link in links:
            #if int(link) >= int(size):
            if int(link) > last_number:
                #print("I only have " + size + " aveliable. Choose a pointer that is not biger than " + size + " or separate the pointers with spaces")
                print("\nYOU IDIOT\nWhere on earth did you see "+ link +" as a title's pointer .I only have " + str(last_number) + "news articles aveliable. Choose a pointer that is not biger than " + str(last_number) + " or separate the pointers with spaces\n")
                valid_form = "No"
                break
        if valid_form == "Yes":
            break
    for pointer in links:
        #open link in browser
        webbrowser.open_new_tab(list_of_all_links[int(pointer)])

def get_one_of_everything(list_of_links):
    list_one_of_one_of_everything = []
    # veriables that count in every category how many articles have been prined
    elada =0
    politiki = 0
    kosmos = 0
    oikonomia = 0
    travel = 0
    auto = 0
    tech = 0
    media = 0
    all_categories =0

    for link in list_of_links:
        a = link
        if a.__contains__("https://www.news.gr/ellada/"):
            #The count is 0 or 1
            if elada == 0 :
                list_one_of_one_of_everything.append(link)
                all_categories = all_categories +1
                elada = elada + 1
        elif a.__contains__("https://www.news.gr/politikh/"):
            if politiki == 0 :
                list_one_of_one_of_everything.append(link)
                all_categories = all_categories +1
                politiki = politiki + 1
        elif a.__contains__("https://www.news.gr/kosmos/"):
            if kosmos == 0 :
                list_one_of_one_of_everything.append(link)
                all_categories = all_categories +1
                kosmos = kosmos + 1
        elif a.__contains__("https://www.news.gr/oikonomia/"):
            if oikonomia == 0 :
                list_one_of_one_of_everything.append(link)
                all_categories = all_categories +1
                oikonomia = oikonomia + 1
        elif a.__contains__("https://www.news.gr/travel/"):
             if travel == 0 :
                list_one_of_one_of_everything.append(link)
                all_categories = all_categories +1
                travel = travel + 1
        elif a.__contains__("https://www.news.gr/auto/"):
            if auto == 0 :
                list_one_of_one_of_everything.append(link)
                all_categories = all_categories +1
                auto = auto + 1
        elif a.__contains__("https://www.news.gr/tech/"):
            if tech == 0 :
                list_one_of_one_of_everything.append(link)
                all_categories = all_categories +1
                tech = tech + 1
        elif a.__contains__("https://www.news.gr/media/"):
            if media == 0 :
                list_one_of_one_of_everything.append(link)
                all_categories = all_categories +1
                media = media + 1
        #When the program prints one of every categoty TERMINATE
        if all_categories == 8:
            break
    print_all_titles(list_one_of_one_of_everything)
    go_to_link(list_of_all_links,list_one_of_one_of_everything,len(list_one_of_one_of_everything))

def get_some_news(list_of_links):
    a=0
    how_many= input("How many news would you like? ")
    int_how_many = int(how_many)
    while int_how_many > len(list_of_links) or int_how_many <= 0:
        if int_how_many > len(list_of_links):
            how_many = input("I can not provide you with so many articles.\nPlease choose a number smaler than " + str(len(list_of_links)) + " ")
        elif  int_how_many <= 0:
                how_many = input("How on earth can I show you 0 or an negative number of news.\nIDIOT\nGive a serius aswer ")
                #turn how_many from str to int
                int_how_many = int(how_many)     
    a = get_news(list_of_links, int_how_many,a)
    while 5>4:
        more_news = input("Whould you like more news? ")
        more_news = more_news.lower()
        #if the users answer contains the word yes or something that means yes and ther is no cofiusion for example "YES NO" ask how many
        if (
             more_news.__contains__("yes")
            or more_news.__contains__("sure")
            or more_news.__contains__("yeah")
            or more_news.__contains__("why not")) and (not( more_news.__contains__("no") or more_news.__contains__("do not") or more_news.__contains__("don't"))):
                how_many = input("How many more ?")
                int_how_many = int(how_many)
                a = get_news(list_of_links, int_how_many,a)
        #if the users answer contains the word no or something that means no and ther is no cofiusion for example "YES NO" terminate
        elif (
            more_news.__contains__("no")
            or more_news.__contains__("do not")
            or more_news.__contains__("don't")) and (not more_news.__contains__("yes")
            or more_news.__contains__("sure")
            or more_news.__contains__("yeah")
            or more_news.__contains__("why not")
            or more_news.__contains__("why not")):
                break
        # incase the users unser is something like "Yes i do not"
        else:
            print("Are you stupid?\nDecide Yes or No ")
            
def get_news(list_of_links,how_many,start):
    end = start
    links = []
    #starting point + how many articles = stop point
    how_many = how_many + start
    for link in range (start,how_many):
        print(str(link +1) +"  " +get_title_from_article(list_of_links[link]))
        links.append(link)
        end = link
    go_to_link(list_of_links,links,link+1)
    return end+1

def print_all_links(list_of_links):
    count = 1
    for link in list_of_links:
        print(str(count) + "  " + link)
        count = count + 1
    go_to_link(list_of_links,list_of_links,len(list_of_links))

def print_all_titles(list_of_links):
    count = 1
    for link in list_of_links:
        print(str(count) +"  " + get_title_from_article(link))
        count = count + 1
    go_to_link(list_of_links,list_of_links,len(list_of_links))
    
def get_news_by_category(list_of_links):
    answer = input ("Choose category : \n- Ellada News\n- Politiki News\n- Kosmos News\n- Oikonomia News\n- Travel News\n- Auto News\n- Tech News\n- Media News\n")
    answer = answer.lower()
    while (5 > 0):
        if answer.__contains__("ellada") and answer.__contains__("news") :
            keyWord = "https://www.news.gr/ellada/"
            break
        elif answer.__contains__("politiki") and answer.__contains__("news") :
            keyWord = "https://www.news.gr/politiki/"
            break
        elif answer.__contains__("kosmos") and answer.__contains__("news") :
            keyWord = "https://www.news.gr/kosmos/"
            break
        elif answer.__contains__("oikonomia") and answer.__contains__("news") :
            keyWord = "https://www.news.gr/oikonomia/"
            break
        elif answer.__contains__("travel") and answer.__contains__("news") :
            keyWord = "https://www.news.gr/travel/"
            break
        elif answer.__contains__("auto") and answer.__contains__("news") :
            keyWord = "https://www.news.gr/auto/"
            break
        elif answer.__contains__("tech") and answer.__contains__("news") :
            keyWord = "https://www.news.gr/tech/"
            break
        elif answer.__contains__("media") and answer.__contains__("news") :
            keyWord = "https://www.news.gr/media/"
            break
        else:
            answer = input ("Wrong Input\nChoose category : \n- Ellada\n- Politiki\n- Kosmos\n- Oikonomia\n- Travel\n- Auto\n- Tech\n- Media\n")
            answer = answer.lower()
    list_of_links_in_category = []
    for link in list_of_links:
        a = link
        if a.__contains__(keyWord):
            list_of_links_in_category.append(link)
    print_all_titles(list_of_links_in_category)
    go_to_link(list_of_links,list_of_links_in_category,len(list_of_links_in_category))
            
    
list_of_links = []
test(list_of_links)
p = input("enter to exit")
