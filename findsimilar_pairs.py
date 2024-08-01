from kucoin_api import get_kucoin_price
from binance_api import get_binance_price_for_a_pair

# Function to read pairs from a file and return as a set
def read_pairs(filename):
    with open(filename, 'r') as f:
        pairs = {line.strip() for line in f}
    return pairs

# Function to find similar pairs between two sets of pairs
def find_similar_pairs(pairs1, pairs2):
    similar_pairs = set()
    for pair1 in pairs1:
        for pair2 in pairs2:
            if pair1 == pair2:
                similar_pairs.add(pair1)
                similar_pairs.add(pair2)
    return similar_pairs

def kucoin_symbol_format(symbol):
    suffixes = ["USDT", "BTC", "DAI", "ETH", "USDC", "EUR", "DOGE", "BRL", "TRY", "TRX"]
    # Formater le symbole pour KuCoin
    for suffix in suffixes:
        if symbol.endswith(suffix):
            new_symbol = symbol[:-len(suffix)] + '-' + suffix
            # print(new_symbol)
            return new_symbol
    return symbol
    

def find_prices_of_similar_pairs(similar_pairs, hyphen_format_kucoin):
        # print(f"pair : {pair}")
        binance_price = get_binance_price_for_a_pair(similar_pairs)
        kucoin_price = get_kucoin_price(hyphen_format_kucoin)
        # print(f"pair : {hyphen_format_kucoin}, binance price : {binance_price}, kucoin_price : {kucoin_price}")
        return binance_price, kucoin_price

# Read pairs from both files

