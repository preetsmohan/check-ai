from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from GoogleScraper import scrape_with_config, GoogleSearchError
import json

# -*- coding: utf8 -*-

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 2

def scrape(keyword):
# See in the config.cfg file for possible values
	config = {
	    'use_own_ip': 'True',
	    'keyword': keyword,
	    'search_engines': ['google',],
	    'num_pages_for_keyword': 1,
	    'scrape_method': 'http',
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
	
	num_results = int(data[0]["num_results"])
	
	results_dict = data[0]["results"]
	
	for i in range(0, num_results):
		if results_dict[i]["domain"] != "":
			title = results_dict[i]["title"]
			link = results_dict[i]["link"]
			results.append((title, link))
	

	url = results[0][1]
	parser = HtmlParser.from_url("https://jobs.lever.co/zipdrug/023810b7-2db3-4c34-8f95-f3f713cb54c2", Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)

	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)

	sentences = []

	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		sentences.append(sentence)
	
	
	#print(results)
	return results, sentences
	
	#print(data)
	
	
	#for serp in search.serps:
	 #   print(serp)
	  #  for link in serp.links:
	   #     print(link)
if __name__ == '__main__':
	scrape('site:jobs.lever.co/* OR site:boards.greenhouse.io/* OR site:indeed.com/* OR site:ziprecruiter.com/* OR site:monster.com software OR engineer OR developer "healthcare" "technology" "objective-c" OR "swift" OR "iOS" -android')