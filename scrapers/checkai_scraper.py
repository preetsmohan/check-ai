from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from GoogleScraper import scrape_with_config, GoogleSearchError
import json

from bs4 import BeautifulSoup as Soup
import urllib, requests, re, pandas as pd
import linkedin_scraper

# -*- coding: utf8 -*-

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import unidecode


TOTAL_INDEED = 3

LANGUAGE = "english"
SENTENCES_COUNT = 1

username = "check-ai-team@umich.edu"
password = "checkaiteam"

#http://stackoverflow.com/questions/18907503/logging-in-to-linkedin-with-python-requests-sessions
def linkedin(url):
	html = linkedin_scraper.return_html(url)
	#print(HtmlParser)
	return html


#http://blog.nycdatascience.com/student-works/project-3-web-scraping-company-data-from-indeed-com-and-dice-com/
def indeed(url):
	count = 0
	jobs = []
	base_url = url

	#print("BASE URL START", base_url)

	if base_url.endswith('.html'):
		base_url = base_url[:-5]

	if "q-" in base_url:
		base_url = "http://www.indeed.com/jobs?q=" + base_url[24:]

	base_url = base_url.replace('-', '+')
	base_url = base_url.replace(',', '%2C')
	
	#print("BASE URL", base_url)
	sort_by = ''
	start_from = '&start='
	
	pd.set_option('max_colwidth',500)    # to remove column limit (Otherwise, we'll lose some info)

	for page in range(1,2): # page from 1 to 100 (last page we can scrape is 100)
		try:
			page = (page-1) * 10  
			url = "%s%s%s%d" % (base_url, sort_by, start_from, page) # get full url 
			req = urllib.request.Request(url, headers={'User-Agent': 'Chrome/35.0.1916.47 Safari/537.36'})
			read = urllib.request.urlopen(req).read()
	
			target = Soup(read, "lxml")
			targetElements = target.findAll('div', attrs={'class' : '  row  result'}) # we're interested in each row (= each job)
		    	
			for elem in targetElements:
				#print("COUNT:", count)
				if count < TOTAL_INDEED:
					comp_name = elem.find('span', attrs={'itemprop':'name'}).getText().strip()
					job_title = elem.find('a', attrs={'class':'turnstileLink'}).attrs['title']
					home_url = "http://www.indeed.com"
					job_link = "%s%s" % (home_url,elem.find('a').get('href'))
					jobs.append((comp_name + "-" + job_title, job_link))
					count += 1

		except Exception as e:
			print("invalid link")
	return jobs
	

def scrape(keyword):
# See in the config.cfg file for possible values
	num_pages = 1
	config = {
	    'use_own_ip': 'False',
	    'keyword': keyword,
	    'search_engines': ['google',],
	    'num_pages_for_keyword': num_pages,
	    'scrape_method': 'http',
    	    'sel_browser': 'phantomjs',
	    'do_caching': 'True',
	    'output_filename': 'results.json'
	}

	try:
	    search = scrape_with_config(config)
	except GoogleSearchError as e:
	    print(e)

	with open('results.json') as data_file:    
		data = json.load(data_file)
	
	results = []
	
	for w in range (0, num_pages):
		num_results = int(data[w]["num_results"])
		
		results_dict = data[w]["results"]
		
		for i in range(0, num_results):
			if results_dict[i]["domain"] != "":
				title = results_dict[i]["title"]
				link = results_dict[i]["link"]

				if "-" + " " in title:
				 	loc = title.find("-" + " ")
				 	if loc >= 0:
				 		title = title[:loc]
	
				if "indeed" in link:
					if "resume" not in link:
						indeed_jobs = indeed(link)
						for job in indeed_jobs:
							results.append((job[0], job[1]))
				elif "linkedin" in link:
					if "view" in link:
						loc = title.find(" " + "in" + " ")
						if loc >= 0:
							title = title[:loc + 1]
						results.append((title, link))

				elif "monster" not in link:
					results.append((title, link)) #it isn't excluding monster from the query?


	all_summaries = []
	
	for result in results:
		url = result[1]

		try:
			if "linkedin" in url:
				doc = linkedin(url)
				parser = PlaintextParser.from_string(doc, Tokenizer(LANGUAGE))

			else:
				parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    		# or for plain text files
    		# parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
			stemmer = Stemmer(LANGUAGE)

			summarizer = Summarizer(stemmer)
			summarizer.stop_words = get_stop_words(LANGUAGE)
	
			summary = []

			for sentence in summarizer(parser.document, SENTENCES_COUNT):
				sentence = sentence._text
				#if '\\x' in sentence:
				#	raise
				#error_chars = [i for i, letter in enumerate(sentence) if letter == '\\x']
				#print("ERROR CHARS", error_chars)
				#for char in error_chars:
					#sentence = sentence[char:] + sentence[:char + 4]

				summary.append(sentence)
				#if 'xa0' in sentence:
					#raise

			all_summaries.append(summary)

		except Exception as e:
                    message = ["Could not retrieve summary for this posting. Please click apply to learn more."]
                    print(e)
                    all_summaries.append(message)

	
	#print(results)
	return results, all_summaries, len(results)
	
	#print(data)
	
	
	#for serp in search.serps:
	 #   print(serp)
	  #  for link in serp.links:
	   #     print(link)
if __name__ == '__main__':
	#scrape('site:jobs.lever.co/* OR site:boards.greenhouse.io/* OR site:indeed.com/* OR site:ziprecruiter.com/* OR site:monster.com software OR engineer OR developer "healthcare" "technology" "objective-c" OR "swift" OR "iOS" -android')
	#scrape('site:jobs.lever.co/* OR site:boards.greenhouse.io/* OR site:ziprecruiter.com/* software OR engineer OR developer "healthcare" "technology" "objective-c" OR "swift" OR "iOS" -android')
	linkedin("https://www.linkedin.com/jobs/view/160027275")
