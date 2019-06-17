import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import mktime
import re

class FileCollection:

    def __init__(self):
        pass

    def getSupportingFile(url, outfile, header, crumb, cookie):
        # get a file from the web and write it to a location

        try:
            r = requests.get(url, headers=header, cookies=cookie)
            with open(outfile, 'wb') as f:
                f.write(r.content)
            print("completed downloading and writing this file: " + url)

        except Exception as e:
            print("there was a problem downloading or writing this file: " + url)
            print(e)


    def getYahooCrumb():

        url = 'https://finance.yahoo.com/quote/AAPL/history'
        with requests.session():
            header = {'Connection': 'keep-alive',
                      'Expires': '-1',
                      'Upgrade-Insecure-Requests': '1',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
                      }

            website = requests.get(url, headers=header)
            crumb = re.findall('"CrumbStore":{"crumb":"(.+?)"}', str(BeautifulSoup(website.text, 'lxml')))
            return (header, crumb[0], website.cookies)


    def convert_to_unix(vdate):
        print(vdate)
        datum = datetime.strptime(vdate, '%d-%m-%Y')
        return int(mktime(datum.timetuple()))
