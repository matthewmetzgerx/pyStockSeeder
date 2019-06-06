import requests
from bs4 import BeautifulSoup
import pandas as pd
from classes import StockHistory as sh
import json
from sys import exit

try:
    with open('config.json') as config:
        cfg = json.load(config)
except:
    print("You must create a config.json file. An example file is provided: example-config.json")
    print("Edit the file and change the name to config.json")
    exit(0)

def getSupportingFile(url, outfile):
    # Get Index Stock collections data
    # Has MarketCap, IPO uear, sector, industry, etc

    try:
        r = requests.get(url)
        with open(outfile, 'wb') as f:
            f.write(r.content)
        print("completed downloading and writing this file: " + url)

    except Exception as e:
        print("there was a problem downloading or writing this file: " + url)
        print(e)


def getSNP500():
    # Add stocks from S&P 500 wikipedia page to dictionary array

    WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    req = requests.get(WIKI_URL)
    soup = BeautifulSoup(req.content, 'lxml')
    rows = soup.find("table", id="constituents").find("tbody").find_all("tr")
    stock_data = []

    for row in rows:
        stock = {}
        cells = row.find_all("td")
        if len(cells) > 0:
            rn = cells[0].get_text()
            stock["symbol"] = cells[0].get_text().strip()
            stock["name"] = cells[1].get_text()
            stock["sector"] = cells[3].get_text()
            stock["industry"] = cells[4].get_text()
            stock["capcategory"] = "large"
            stock_data.append(stock)
    return stock_data


def getSNP400():
    # Add stocks from S&P 400 wikipedia page to dictionary array

    WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies"
    req = requests.get(WIKI_URL)
    soup = BeautifulSoup(req.content, 'lxml')
    rows = soup.find("table", {'class':'wikitable sortable'}).find("tbody").find_all("tr")
    stock_data = []

    for row in rows:
        stock = {}
        cells = row.find_all("td")
        if len(cells) > 0:
            rn = cells[0].get_text()
            stock["name"] = cells[0].get_text()
            stock["symbol"] = cells[1].get_text().strip()
            stock["sector"] = cells[2].get_text()
            stock["industry"] = cells[3].get_text()
            stock["capcategory"] = "mid"
            stock_data.append(stock)
    return stock_data


def getSNP1000():
    # Add stocks from S&P 1000 (small, mid) wikipedia page to dictionary array

    WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_1000_companies"
    req = requests.get(WIKI_URL)
    soup = BeautifulSoup(req.content, 'lxml')
    rows = soup.find("table", id="constituents").find("tbody").find_all("tr")
    stock_data = []

    for row in rows:
        stock = {}
        cells = row.find_all("td")
        if len(cells) > 0:
            rn = cells[0].get_text()
            stock["name"] = cells[0].get_text()
            stock["symbol"] = cells[1].get_text().strip()
            stock["sector"] = cells[3].get_text()
            stock["industry"] = cells[4].get_text()
            stock["capcategory"] = ""
            stock_data.append(stock)
    return stock_data


def scrubMarketCap(data):
    # Set the marketcap to a float or null

    data["MarketCap"] = data["MarketCap"].str.replace("$", "")
    data['MarketCap'] = data['MarketCap'].apply(
        lambda x:
        float(str(x).replace("B", ""))*1000000000 if 'B' in str(x) else x)
    data['MarketCap'] = data['MarketCap'].apply(
        lambda x:
        float(str(x).replace("M", ""))*1000000 if 'M' in str(x) else x)
    return data


def setMarketCap(row, exlist, edf):
    # get marketcap from dict where symbol is in current exchange

    if row["symbol"] in exlist:
        if row["symbol"] in edf:
            return edf[row["symbol"]]["MarketCap"]
    return row["marketcap"]


def setCapCategory(row):
    # get capcategory by market cap value
    cat = "small"
    if row["marketcap"] >= 10000000000:
        cat = "large"
    elif row["marketcap"] < 10000000000 and row["marketcap"] >= 2000000000:
        cat = "mid"
    return cat


def setExchange(row, exlist, exchange):
    # if in exchange return the exchange name to set dataframe

    if row["symbol"] in exlist:
        return exchange
    else:
        return row["exchange"]


def setSector(row, exlist, edf):
    # if in exchange return the sector name to set dataframe

    if row["symbol"] in exlist:
        if row["symbol"] in edf:
            return edf[row["symbol"]]["Sector"]
    return row["sector"]


def setIndustry(row, exlist, edf):
    # if in exchange return the industry name to set dataframe

    if row["symbol"] in exlist:
        if row["symbol"] in edf:
            return edf[row["symbol"]]["industry"]
    return row["industry"]


def updateDataFrame(primarydf, exchangefile, exchangename):
    # set values in the primary stock dataframe

    sdf = scrubMarketCap(pd.read_csv(exchangefile))
    lsym = list(sdf["Symbol"])
    caps = sdf[["Symbol","MarketCap"]].set_index('Symbol').T.to_dict()
    secs = sdf[["Symbol", "Sector"]].set_index('Symbol').T.to_dict()
    inds = sdf[["Symbol", "industry"]].set_index('Symbol').T.to_dict()

    primarydf["sector"] = primarydf.apply(
        lambda row:
        setSector(row, lsym, secs), axis="columns")

    primarydf["industry"] = primarydf.apply(
        lambda row:
        setIndustry(row, lsym, inds), axis="columns")

    primarydf["marketcap"] = primarydf.apply(
        lambda row:
        setMarketCap(row, lsym, caps), axis="columns")

    primarydf["capcategory"] = primarydf.apply(
        lambda row:
        setCapCategory(row), axis="columns")

    return primarydf


def main():

    # --------------------------------------------------------------------------
    # MAIN Build the dataframe and generate the data files
    # --------------------------------------------------------------------------
    # Note: the S&P 1000 covers the S&P400, thus we do not need to use th3
    # getSNP400 function in this case. It is left in script simply due to
    # the fact that it may be needed in some future effort

    df1 = pd.DataFrame(getSNP500())
    df2 = pd.DataFrame(getSNP1000())
    df1 = df1.append(df2, ignore_index=True)
    df1["exchange"] = ""
    df1["marketcap"] = None

    [getSupportingFile(support["origin"], support["writeTo"]) for support in cfg["supportingFiles"]]
    for support in cfg["supportingFiles"]:
        df1 = updateDataFrame(df1, support["writeTo"], support["exchange"])

    df1 = df1[[
        'symbol', 'name', 'exchange', 'sector',
        'industry', 'capcategory', 'marketcap'
    ]]

    df1.to_csv(cfg["writeseeder"])
    hist = sh.StockHistory(cfg["eodAPItoken"], cfg["historyDir"])
    hist.getHistory(list(df1["symbol"]))

    print("Execution completed.")

main()
