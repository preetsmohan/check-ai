from flask import Flask
import checkai_scraper as scraper

app = Flask(__name__)

@app.route('/')
def hello_world():
	results = scraper.scrape('hello')
	print("hi")
	print(results)
	return "Hello"