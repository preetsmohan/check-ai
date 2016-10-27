
from GoogleScraper import scrape_with_config, GoogleSearchError
import json

# See in the config.cfg file for possible values
config = {
    'use_own_ip': 'True',
    'keyword': 'software OR engineer OR developer "healthcare" "objective-c" OR "swift" OR "iOS"',
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

print(results)

#print(data)


#for serp in search.serps:
 #   print(serp)
  #  for link in serp.links:
   #     print(link)