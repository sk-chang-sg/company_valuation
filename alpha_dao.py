import configparser
import requests
import json


class AlphaDAO:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read("keys.ini")

        # self.alpha_key = config["alpha_vantage"]["key"]
        self.alpha_key = "demo"

        self.base_url = "https://www.alphavantage.co/query?"

    def get_balance_sheet(self, symbol: str) -> pd.DataFrame:
        params = {
            "function": "BALANCE_SHEET",
            "symbol": symbol,
            "apikey": self.alpha_key,
        }
        r = requests.get(self.base_url, params=params)
        return r.json()

    def get_balance_sheet(self, symbol: str) -> pd.DataFrame:
        params = {
            "function": "BALANCE_SHEET",
            "symbol": symbol,
            "apikey": self.alpha_key,
        }
        r = requests.get(self.base_url, params=params)
        return r.json()
