import requests

# coin = "ethereum"

coins = ["ethereum", "bitcoin", "dogecoin", "cardano", "polkadot", "solana"]

coin_data = list()

for coin in coins:
    url = f"https://api.coingecko.com/api/v3/coins/{coin}"

    res = requests.get(url=url)
    print(f"response status code: {res.status_code}")
    res_dict = res.json()
    current_price = res_dict["market_data"]["current_price"]["usd"]

    print(f"{coin} current price: {current_price}")

    current_coin_data = {
        "coin": coin,
        "current_price": current_price,
        "ath": res_dict["market_data"]["ath"]["usd"],
        "last_updated": res_dict["last_updated"],
    }

    coin_data.append(current_coin_data)

print("RESULTSSSS")
print(coin_data)
