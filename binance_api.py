import requests

def get_binance_price_for_a_pair(symbol):
    base_url = "https://api.binance.com"
    ticker_url = f"{base_url}/api/v3/ticker/price?symbol={symbol}"

    response = requests.get(ticker_url)
    data = response.json()

    if 'price' in data:
        return float(data['price'])
    else:
        print(f"Failed to retrieve price for {symbol}: {data}")
        return None

def get_binance_all_prices():
    base_url = "https://api.binance.com"
    
    # Step 1: Get all trading pairs from the exchangeInfo endpoint
    exchange_info_url = f"{base_url}/api/v3/exchangeInfo"
    response = requests.get(exchange_info_url)
    data = response.json()
    
    trading_pairs = [symbol['symbol'] for symbol in data['symbols']]
    
    # Step 2: Get the prices for all trading pairs
    prices_url = f"{base_url}/api/v3/ticker/price"
    response = requests.get(prices_url)
    prices_data = response.json()
    
    prices = {}
    for item in prices_data:
        symbol = item['symbol']
        if symbol in trading_pairs:
            prices[symbol] = float(item['price'])
    
    return prices

def get_binance_all_all_prices():
    try:
        prices = get_binance_all_prices()
        count = 0 
        with open("binance_pair.txt", "w") as file:
            # Write prices for all trading pairs
            for symbol, price in prices.items():
                file.write(f"{symbol}\n")
                count += 1

        # Print the total number of coins
        print(f"Total number of coins: {len(prices)}")
        print("count", count)
    except Exception as e:
        print(f"Error occurred: {str(e)}")

