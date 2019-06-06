import requests
import pandas as pd
from pandas.compat import StringIO

class StockHistory:

    def __init__(self, token, dir):
        self.token = token
        self.directory = dir


    def get_eod_data(self, symbol="AAPL.US", api_token="", session=None):
        # Retrieve the stock history for a particular stock from https://eodhistoricaldata.com/

        if session is None:
            session = requests.Session()
            url = "https://eodhistoricaldata.com/api/eod/%s" % symbol
            params = {"api_token": api_token}
            r = session.get(url, params=params)

            if r.status_code == requests.codes.ok:
                df = pd.read_csv(StringIO(r.text), skipfooter=1, parse_dates=[0], index_col=0, engine="python")
                return df
            else:
                print("Stock history problem: " + str(r.status_code) + ", " + r.reason + ", " + url)


    def getHistory(self, stocksymbols):
        # for each symbol, retrieve the history for the stock and write it to file.

        for symbol in stocksymbols:
            print(symbol)
            sym = symbol.replace(".", "-") + ".US"

            try:
                data = self.get_eod_data(sym, self.token)
                out = open(self.directory + sym + ".csv", "wt")
                out.write(data.to_csv())
                out.close()
            except:
                print("Stock " + symbol + " skipped due to error.")




