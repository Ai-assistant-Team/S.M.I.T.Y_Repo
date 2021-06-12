from news import get_news, open_news_page
from ClearTheTxtOfLinks import create_txt_with_links
from ClearTheTxtOfLinks import clear_the_txt_of_links
def test():
    a = create_txt_with_links()
    if a == 10:
        return 10
    a = clear_the_txt_of_links()
    if a == 8:
        return 8
    elif a == 9:
        return 9
    n = get_news()
    print(n)
    a =open_news_page("Συναγερμός στις φυλακές Αγίου Στεφάνου: 15 κρούσματα – Θετικός και ο Νίκος Παλαιοκώστας")
    print(a)
    print("\nok")

print (test())
