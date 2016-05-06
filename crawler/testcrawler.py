import psycopg2
import urllib2
import xml.etree.ElementTree as etree
from bs4 import BeautifulSoup
import requests
import json
import csv
import feedparser
import random

def crawlpage(url, cat, json_array):
	d=feedparser.parse(url)
	print len(d['entries'])
	i=0
	for post in d.entries:
		json_obj = {}
		i=i+1
		cat1 = getNewCategory(cat,i)
		#print cat1
		json_obj['category'] = cat1
		json_obj['class'] = cat
		json_obj['article'] = post.description
		json_obj['url'] = post.link
		json_array.append(json_obj);
	return json_array

def getNewCategory(cat,i):
	print "cat",cat
	i = random.randint(0,4);
	#print i
	sports = ['tennis', 'football', 'cricket', 'rugby', 'soccer']
	tech = ['computer', 'mobile', 'ibm', 'cisco', 'tablet']
	entertainment = ['dance', 'music', 'drama', 'games', 'piano']
	business = ['stock', 'trade', 'shares', 'market', 'funds']
	if(cat == 'sports'):
		print sports[i]
		return sports[i]
	if(cat == 'tech'):
		print tech[i]
		return tech[i]
	if(cat == 'entertainment'):
		print entertainment[i]
		return entertainment[i]
	if(cat == 'business'):
		print business[i]
		return business[i]
	return cat

def crawlCsvAndCreateJsonFile(fileName, jsonfile):
	ifile  = open(fileName, "rb")
	jsonFile = open(jsonfile,"w")
	reader = csv.reader(ifile)
	rownum = 0
	mainJson = {}
	jsonArray = []
	for row in reader:
		#print row
		if rownum == 0:
			header = row
		else:
			rss = row[0]
			category = row[1]
			jsonArray = crawlpage(rss, category, jsonArray)
		rownum += 1
	mainJson['news_articles'] = jsonArray
	#print mainJson
	jsondata = json.dumps(mainJson)
	jsonFile.write(jsondata)
	ifile.close()
	jsonFile.close()

crawlCsvAndCreateJsonFile('rss_link.csv', 'news.json');
