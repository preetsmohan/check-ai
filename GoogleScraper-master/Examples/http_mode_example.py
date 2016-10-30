#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from GoogleScraper import scrape_with_config, GoogleSearchError

keywords = [
    'software OR engineer OR developer "healthcare" "objective-c" OR "swift" OR "iOS"'
]

# See in the config.cfg file for possible values
config = {
    'use_own_ip': 'True',
    'keyword': 'software OR engineer OR developer "healthcare" "objective-c" OR "swift" OR "iOS"',
    'search_engines': ['google',],
    'num_pages_for_keyword': 1,
    'scrape_method': 'http',
    'do_caching': 'True'
}

try:
    search = scrape_with_config(config)
except GoogleSearchError as e:
    print(e)

for serp in search.serps:
    print(serp)
    for link in serp.links:
        print(link)