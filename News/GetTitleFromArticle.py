#https://www.geeksforgeeks.org/newspaper-article-scraping-curation-python/

from newspaper import Article

def get_title_from_article(url):
    try:
        #A new article from TOI
        #url = "https://www.news.gr/ellada/article/2555711/egklima-koropi-profilakistike-o-76chronos-gia-ti-dolofonia-tou-giou-tou.html"
        #For different language newspaper refer above table
        toi_article = Article(url, language="el") # el for Greek
        #To download the article
        toi_article.download()
        #To parse the article
        toi_article.parse()
        #To extract title
        return toi_article.title
    except:
        return 10