
import requests
import json

api_request = requests.get("https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c")
api = json.loads(api_request.content)

coins = [
    {
        "symbol":"BTC",
        "amount_owned": 2,
        "price_per_coin": 3200
    },
    {
        "symbol":"EOS",
        "amount_owned": 100,
        "price_per_coin": 2.05
    }
]

for i in range(0,5):
    for coin in coins:
        if api["data"][i]["symbol"] == coin:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]

            print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
            print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("Number of Coin:", coin["amount_owned"])
            print("Total Amount Paid: ", "${:0.2f}" total_paid)
            print("---------------")

"""
import requests
import json

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {
    'start': 1,
    'limit': 5,
    'convert': 'USD',
    'CMC_PRO_API_KEY': '3889ce63-c733-403d-8b7d-c41a243b4ea'
}

try:
    api_request = requests.get(url, params=parameters)
    api_request.raise_for_status()  # Raise an HTTPError for bad responses
    api = api_request.json()

    if 'error' in api:
        print(f"API Error: {api['error']['message']}")
    else:
        for i in range(min(5, len(api.get('data', [])))):
            for coin in coins:
                if api['data'][i]['symbol'] == coin:
                    print(api['data'][i]['symbol'])
                    print("{0:.2f}".format(api['data'][i]['quote']['USD']['price']))
                    print("---------------")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
"""