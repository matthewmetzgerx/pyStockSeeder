import requests
from bs4 import BeautifulSoup
import json
from sys import exit
import pandas as pd


try:
    with open('config.json') as config:
        cfg = json.load(config)
except:
    print("You must create a config.json file. An example file is provided: example-config.json")
    print("Edit the file and change the name to config.json")
    exit(0)


def getInterestRates():
    # Add daily bond interest rate data from US Treasury

    Rates_URL = cfg["otherFiles"][0]["origin"]
    req = requests.get(Rates_URL)
    soup = BeautifulSoup(req.content, 'lxml')
    rows = soup.find("table", {"class": "t-chart"}).find_all("tr")
    columns = [r.get_text().strip().replace(" ", "") for r in rows[0].find_all("th")]
    rate_data = []
    for row in rows[1:]:
        values = [r.get_text().strip() for r in row.find_all("td")]
        rate_data.append(values)
    df = pd.DataFrame(rate_data, columns=columns)
    df.to_csv(cfg["otherFiles"][0]["writeTo"], index=False)

def main():
    getInterestRates()





main()
