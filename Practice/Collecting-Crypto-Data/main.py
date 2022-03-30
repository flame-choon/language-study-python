# 코인 정보 조회

 #This example uses Python 2.7 and the python-request library.
 #From: CoinMarketCap

from curses import raw
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class CoinDataAPIClient():
    def __init__(self):
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
        }
        self.session = Session()
        self.session.headers.update(headers)
    
    # 1. 원하는 코인의 실시간 가격 정보를 조회
    # symbol example : btc, eth
    def get_coin_info(self, symbol):
        url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
            'symbol': symbol,
        }
        raw_resp = self.session.get(url, params=parameters)
        resp = raw_resp.json()
        return resp

    # 2. 사람들이 가장 많이 보는 코인 중에 가격이 제일 많이 바뀐 코인 정보 조회
    def get_trending_coin(self):
        url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/trending/gainers-losers'
        raw_resp = self.session.get(url)
        resp = raw_resp.json()
        return resp

    # 3. 비트코인 도미넌스를 조회 
    def get_bitcoin_dominance(self):
        url = 'https://sandbox-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
        raw_resp = self.session.get(url)
        resp = raw_resp.json()
        return resp    

coinData = CoinDataAPIClient()
bitcoin_dominance = coinData.get_bitcoin_dominance()
print(json.dumps(bitcoin_dominance, indent=4))

# get_coin_info('btc')    
# trending_coin = get_trending_coin()
# print(trending_coin)
# bitcoin_dominance = get_bitcoin_dominance()
# print(bitcoin_dominance)