





# newsapi lijkt heel erg op newsdataapi maar dan net iets gaarder. niet interessant dus.


from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='363077aaf8e34e31a36cdacc219ce13a')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(country='us')

# print (top_headlines)


# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      from_param='2022-09-22',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)


print (all_articles)


# /v2/top-headlines/sources
sources = newsapi.get_sources()