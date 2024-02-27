#import requests

def intializeNewsDataApi():
	from newsdataapi import NewsDataApiClient
	myApiKey = "pub_863217ce7c032d5216385aff833d85e7a999"
	api = NewsDataApiClient(apikey=myApiKey)
	return api

apiClient = intializeNewsDataApi();

def acquireNewsSetNewsDataApi(api, newsLanguage = "nl"):
	import random
	# call and read the total number of results
	categories = "environment,politics,science,world"
	response = api.news_api(language = newsLanguage, page = 0, category = categories)
	totalSize = response["totalResults"]
	# take n article indexes that fall between the number of results
	numberOfArticles = 12
	articles = random.sample(range(totalSize), numberOfArticles)
	###  divmod is used here to translate this article index to a pagenumber and indexnumber within a page
	articleList = []
	for i in articles:
		pageNumber, indexNumber = divmod(i, 10)
		# ####pageNumber = str(pageNumber)
		response = api.news_api(language = newsLanguage, page = pageNumber, category = categories)
		article = response["results"][indexNumber]
		articleList.append(article)
	return articleList

myNews = acquireNewsSetNewsDataApi(apiClient)

# def acquireDistributedNewsSetNewsDataApi(api, newsLanguage = "nl"):
# 	# the goal of this function is get a set of news. however with a maximum of 1 article per unique news source.
# 	import random
# 	# call and read the total number of results
# 	categories = "environment,politics,science,world"
# 	response = api.news_api(language = newsLanguage, category = categories)
# 	totalSize = response["totalResults"] - 1
# 	print(totalSize)
# 	### set number of articles
# 	numberOfArticles = 12
# 	### start iterating
# 	articleList = []
# 	iterator_count = 0
# 	# arbitrary number simply to avoid endless loops
# 	while iterator_count < 1000:
# 		articleNumber = random.randint(0, totalSize)
# 		pageNumber, indexNumber = divmod(articleNumber, 10)
# 		response = api.news_api(language = newsLanguage, page = pageNumber, category = categories)
# 		article = response["results"][indexNumber]
# 		print(article)
# 		### check whether the newsource already exist in any of the earlier articles
# 		isduplicatesource = False
# 		for j in articleList:
# 			if j["source_id"] == article["source_id"]:
# 				isduplicatesource = True
# 		if not isduplicatesource:
# 			articleList.append(article)
# 		if len(articleList) >= numberOfArticles:
# 			break
# 		iterator_count += 1
# 		print (len(articleList))
# 	return articleList
## op zich werkt dus functie wel maar in de praktijk niet echt lekker. 
## de reden is dat de source 'boerderij.nl' onevenredig vaak voorkomt
## waardoor er heeeeeeeeeeeeel veel calls nodig zijn om tot een lijst van 12 te komen.
# myNews = acquireDistributedNewsSetNewsDataApi(apiClient)



def buildMyNewsFileName(myName = "JohnDoe"):
	from datetime import date
	import json
	# build the file's name
	today = str(date.today())
	fileName = ("_").join(["RandKrant", myName, today])
	return fileName

print ( buildMyNewsFileName())

def saveNewsContentToFile(myNews):
	import json
	import os 
	# save to file
	path = os.path.join(os.getcwd(), "rawoutput")
	filename = buildMyNewsFileName()
	with open(path + "\\" +filename + ".json", "w") as writtenFile:
		json.dump(myNews, writtenFile)

saveNewsContentToFile(myNews)



# OBSOLETE MAAR TOCH NOG NIET HELEMAAL VERWIJDEREN
# def acquireNewsCompleteSetNewsDataApi(api, newsLanguage = "nl"):
# 	#we need iteration here because the page size is limited (10)
# 	#iterate with page = 0, page = 1 .... until nextPage in response is null
# 	articleList = []
# 	page = 0
# 	# 50 is an arbitrary number here (to prevent endless loops)
# 	while page < 50:
# 	  response = api.news_api( q= "ajax" , language = newsLanguage, page = page)
# 	  articleList.extend(response["results"])
# 	  nextPage = response["nextPage"]
# 	  if nextPage is None:
# 	    break
# 	  page += 1
# 	return articleList
# 	#print("Total number of news articles found:", len(myNews))

# #myNews = acquireNewsCompleteSetNewsDataApi(apiClient)
# #print (len(myNews))