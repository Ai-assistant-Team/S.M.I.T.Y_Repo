#https://www.geeksforgeeks.org/newspaper-article-scraping-curation-python/

from newspaper import Article

def get_title_from_article(url):
    toi_article = Article(url, language="el") # el for Greek
    #To download the article
    toi_article.download()
    #To parse the article
    toi_article.parse()
    #To extract title
    return toi_article.title