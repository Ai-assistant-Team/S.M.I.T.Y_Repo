#https://www.geeksforgeeks.org/newspaper-article-scraping-curation-python/
from newspaper import Article
def get_title_from_article(url):
    try:
        #A new article from TOI
        #For different language newspaper refer above table
        # el for Greek
        toi_article = Article(url, language="el")
        #To download the article
        toi_article.download()
        #To parse the article
        toi_article.parse()
        #To extract title
        return toi_article.title
    except:
        return 10
