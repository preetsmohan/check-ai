#http://stackoverflow.com/questions/18907503/logging-in-to-linkedin-with-python-requests-sessions
import http.cookiejar as cookielib
import os
import urllib
import re
import string
from bs4 import BeautifulSoup

cookie_filename = "parser.cookies.txt"

username = "check-ai-team@umich.edu"
password = "checkaiteam"

class LinkedInParser(object):

    def __init__(self, login, password, url):
        """ Start up... """
        self.login = login
        self.password = password
        self.url = url

        # Simulate browser with cookies enabled
        self.cj = cookielib.MozillaCookieJar(cookie_filename)
        if os.access(cookie_filename, os.F_OK):
            self.cj.load()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPRedirectHandler(),
            urllib.request.HTTPHandler(debuglevel=0),
            urllib.request.HTTPSHandler(debuglevel=0),
            urllib.request.HTTPCookieProcessor(self.cj)
        )
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                           'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

        # Login
        self.loginPage()

        self.html = self.loadHTML()
       # print(self.html)

        self.cj.save()


    def loadPage(self, url, data=None):
        """
        Utility function to load HTML from URLs for us with hack to continue despite 404
        """
        # We'll print the url in case of infinite loop
        # print "Loading URL: %s" % url
        try:
            if data is not None:
                response = self.opener.open(url, data)
            else:
                response = self.opener.open(url)
            return ''.join([str(l) for l in response.readlines()])
        except Exception as e:
            # If URL doesn't load for ANY reason, try again...
            # Quick and dirty solution for 404 returns because of network problems
            # However, this could infinite loop if there's an actual problem
            return "Error loading this job description"

    def loadSoup(self, url, data=None):
        """
        Combine loading of URL, HTML, and parsing with BeautifulSoup
        """
        html = self.loadPage(url, data)
        soup = BeautifulSoup(html, "lxml")
        return soup

    def loginPage(self):
        """
        Handle login. This should populate our cookie jar.
        """
        soup = self.loadSoup("https://www.linkedin.com/")
        try:
            csrf = soup.find(id="loginCsrfParam-login")['value']
            login_data = urllib.parse.urlencode({
                'session_key': self.login,
                'session_password': self.password,
                'loginCsrfParam': csrf,
            }).encode('utf8')
    
            self.loadPage("https://www.linkedin.com/uas/login-submit", login_data)
        except:
            return 

        return

    def loadHTML(self):
        soup = self.loadSoup(self.url)
        #print(soup)

        html = str(soup)
        end = html.find('property="og:description"')
        html = html[:end]
        begin = html.rfind("meta")
        html = html[begin + 14:]
        html = html.replace("&amp;amp;", "&")
        html = html.replace("&#x27;", "'")
        html = html.replace("&amp;nbsp;", " ")
        html = html.replace('\xc2\xb7', "-")
        return html

def return_html(url):
    parser = LinkedInParser(username, password, url).html
    #print(parser)
    return parser


if __name__ == '__main__':
    return_html("https://www.linkedin.com/jobs/view/160027275")
