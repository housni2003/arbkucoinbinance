# import requests

# def get_eth_to_usdt_prices():
#     crypto_id = 'ethereum'  # CoinGecko ID for Ethereum
#     target_currency = 'usdt'  # Target currency for the trading pair
#     url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/tickers"
#     response = requests.get(url)
#     data = response.json()

#     exchange_prices = []
#     for ticker in data['tickers']:
#         if ticker['target'].lower() == target_currency:
#             exchange = ticker['market']['name']
#             pair = ticker['base'] + '/' + ticker['target']
#             price = ticker['last']
#             exchange_prices.append((exchange, pair, price))

#     return exchange_prices

# # Example usage:
# prices = get_eth_to_usdt_prices()

# for exchange, pair, price in prices:
#     print(f"Exchange: {exchange}, Pair: {pair}, Price: ${price:,.2f}")
# Answer :
# Exchange: BYDFi, Pair: ETH/USDT, Price: $3,107.14
# Exchange: BigONE, Pair: ETH/USDT, Price: $3,108.93
# Exchange: FameEX, Pair: ETH/USDT, Price: $3,108.25
# Exchange: Bitunix, Pair: ETH/USDT, Price: $3,107.63
# Exchange: BYDFi, Pair: ETH/USDT, Price: $3,107.14
# Exchange: BigONE, Pair: ETH/USDT, Price: $3,108.93
# Exchange: FameEX, Pair: ETH/USDT, Price: $3,108.25
# Exchange: Bitunix, Pair: ETH/USDT, Price: $3,107.63
# Exchange: FameEX, Pair: ETH/USDT, Price: $3,108.25
# Exchange: Bitunix, Pair: ETH/USDT, Price: $3,107.63
# Exchange: Bitunix, Pair: ETH/USDT, Price: $3,107.63
# Exchange: WEEX, Pair: ETH/USDT, Price: $3,108.41
# Exchange: Phemex, Pair: ETH/USDT, Price: $3,108.32
# Exchange: HashKey Global, Pair: ETH/USDT, Price: $3,106.90
# Exchange: Bitexlive, Pair: ETH/USDT, Price: $3,107.85
# Exchange: Trubit, Pair: ETH/USDT, Price: $3,107.69
# Exchange: HashKey Exchange, Pair: ETH/USDT, Price: $3,107.16
# Exchange: WhiteBIT, Pair: ETH/USDT, Price: $3,109.49
# Exchange: Bittime, Pair: ETH/USDT, Price: $3,109.09
# Exchange: Vindax, Pair: ETH/USDT, Price: $3,103.32
# Exchange: BitVenus, Pair: ETH/USDT, Price: $3,108.41

# import requests

# def get_binance_eth_price():
#     url = "https://api.binance.com/api/v3/ticker/price"
#     params = {
#         "symbol": "ETHUSDT"
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
    
#     if 'price' in data:
#         return float(data['price'])
#     else:
#         return None

# def get_kucoin_eth_price():
#     url = "https://api.kucoin.com/api/v1/market/orderbook/level1"
#     params = {
#         "symbol": "ETH-USDT"
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
    
#     if 'data' in data and 'price' in data['data']:
#         return float(data['data']['price'])
#     else:
#         return None

# # Example usage:
# binance_price = get_binance_eth_price()
# kucoin_price = get_kucoin_eth_price()

# if binance_price is not None:
#     print(f"The current price of ETH/USDT on Binance is: ${binance_price:,.2f}")
# else:
#     print("Failed to retrieve price data from Binance.")

# if kucoin_price is not None:
#     print(f"The current price of ETH/USDT on KuCoin is: ${kucoin_price:,.2f}")
# else:
#     print("Failed to retrieve price data from KuCoin.")

# import requests

# def get_binance_all_prices():
#     base_url = "https://api.binance.com"
    
#     # Step 1: Get all trading pairs from the exchangeInfo endpoint
#     exchange_info_url = f"{base_url}/api/v3/exchangeInfo"
#     response = requests.get(exchange_info_url)
#     data = response.json()
    
#     trading_pairs = [symbol['symbol'] for symbol in data['symbols']]
    
#     # Step 2: Get the prices for all trading pairs
#     prices_url = f"{base_url}/api/v3/ticker/price"
#     response = requests.get(prices_url)
#     prices_data = response.json()
    
#     prices = {}
#     for item in prices_data:
#         symbol = item['symbol']
#         if symbol in trading_pairs:
#             prices[symbol] = float(item['price'])
    
#     return prices

# # Example usage:
# prices = get_binance_all_prices()
# count = 0 
# # Print prices for all trading pairs
# for symbol, price in prices.items():
#     print(f"Symbol: {symbol}, Price: {price}")
#     count +=1

# # Print the total number of coins
# print(f"Total number of coins: {len(prices)}")
# print("count", count)

import requests
import time

def get_kucoin_all_trading_pairs():
    base_url = "https://api.kucoin.com"
    symbols_url = f"{base_url}/api/v1/symbols"
    
    response = requests.get(symbols_url)
    data = response.json()
    
    if data['code'] != '200000':
        raise Exception(f"Failed to retrieve trading pairs from KuCoin: {data['msg']}")
    
    trading_pairs = [symbol['symbol'] for symbol in data['data']]
    return trading_pairs

def get_kucoin_price(symbol):
    base_url = "https://api.kucoin.com"
    ticker_url = f"{base_url}/api/v1/market/orderbook/level1?symbol={symbol}"
    
    response = requests.get(ticker_url)
    data = response.json()
    
    if data['code'] == '200000' and 'data' in data:
        price = float(data['data']['price'])
        # print(price)
        return price
    else:
        print(f"Failed to retrieve price for {symbol}: {data['msg']}")
        return None

# Example usage:
def get_kucoin_pairs_and_prices():
    try:
        pairs = get_kucoin_all_trading_pairs()
        with open("kucoin_pair.txt", "w") as file:
            for pair in pairs:
                formatted_pair = pair.replace("-", "")  # Remove the hyphen
                value = get_kucoin_price(pair)
                if value is not None:
                    print(formatted_pair)
                    file.write(f"{formatted_pair}\n")  # Write the price with 10 decimal places
                else:
                    file.write(f"{formatted_pair}: N/A\n")
                time.sleep(0.1)  # Add a small delay to respect API rate limits
    except Exception as e:
        print(f"Error occurred: {str(e)}")
