import requests
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY="ZIEH13S88PJX3CSY"
BASE_URL="https://www.alphavantage.co/query"

# url=https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=ZIEH13S88PJX3CSY

def fetch_stock_data(symbol):
    params={
        "function" : "GLOBAL_QUOTE",
        "symbol":symbol,
        "apikey":API_KEY
    }
    print(f"fetching data for {symbol}..")
    response=requests.get(BASE_URL,params=params,verify=False)

    if response.status_code==200:
        print(response.json())
        return response.json()
    else:
        print(f"Error in API call check {response.status_code}")
        return None

    
# fetch_stock_data("IBM")

def fetch_and_save(data,symbol):
    if "Global Quote" not in data or not data["Global Quote"]:
        print("Invalid symbol or API limit reached")

    quote=data["Global Quote"]

    extracted_data={
        "symbol": quote["01. symbol"],
        "price": float(quote["05. price"]),
        "volume": int(quote["06. volume"]),
        "trading_day": quote["07. latest trading day"],
        "change_percent": quote["10. change percent"]    
        }

    print("-----------STOCK REPORT ----------")
    print(f"Symbol: {extracted_data['symbol']}")
    print(f"Price: {extracted_data['price']}")
    print(f"Change: {extracted_data['change_percent']}")

    filename=f"{symbol}_data.json"
    with open(filename, "w") as json_file:
        json.dump(extracted_data, json_file, indent=4)

    print(f"Data saved to {filename}")


if __name__ == "__main__":
    if len(sys.argv)>1:
        stock_sym=sys.argv[1]
    else:
        stock_sym=input("Enter the Stock symbol")

    raw_data=fetch_stock_data(stock_sym)
    if raw_data:
        fetch_and_save(raw_data,stock_sym)