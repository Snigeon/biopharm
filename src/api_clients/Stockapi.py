import requests
from config import key_
class StockMarketClient:
    BASE_URL = 'https://www.alphavantage.co/query'

    def fetch_company_overview(self, symbol):
        response = requests.get(
            f"{self.BASE_URL}?function=OVERVIEW&symbol={symbol}&apikey={key_}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching stock data: {response.status_code}")