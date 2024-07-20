import configparser, requests, json, os

class AlphaDAO:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read("keys.ini")

        self.alpha_key = config["alpha_vantage"]["key"]
        # self.alpha_key = "demo"
        self.base_url = "https://www.alphavantage.co/query?"
        self.file_path = "data"

    def get_balance_sheet(self, symbol: str) -> None:
        params = {
            "function": "BALANCE_SHEET",
            "symbol": symbol,
            "apikey": self.alpha_key,
        }
        r = requests.get(self.base_url, params=params)
        self._dump_to_file(data=r.json(), name=symbol+"-balance_sheet")
        # return r.json()

    def get_income_statement(self, symbol: str) -> None:
        params = {
            "function": "INCOME_STATEMENT",
            "symbol": symbol,
            "apikey": self.alpha_key,
        }
        r = requests.get(self.base_url, params=params)
        self._dump_to_file(data=r.json(), name=symbol+"-income_statement")
        # return r.json()
    
    def get_cashflow_statement(self, symbol: str) -> dict:
        params = {
            "function": "CASH_FLOW",
            "symbol": symbol,
            "apikey": self.alpha_key,
        }
        r = requests.get(self.base_url, params=params)
        self._dump_to_file(data=r.json(), name=symbol+"-cashflow_statement")
        # return r.json()
    
    def _dump_to_file(self, data: dict, name:str):
        file_path = os.path.join(self.file_path, name+".json")
        with open(file_path, 'w') as f: 
            json.dump(data, f)

