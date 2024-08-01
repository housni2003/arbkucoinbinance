# main.py
import json
from kucoin_api import get_kucoin_pairs_and_prices
from binance_api import get_binance_all_all_prices
from arbitrage import *
from findsimilar_pairs import *
import os
from sort import *

def main():
    binance_fee = 0.001
    kucoin_fee  = 0.001
    pairs_file1 = read_pairs('binance_pair.txt')
    pairs_file2 = read_pairs('kucoin_pair.txt')
    similar_pairs = find_similar_pairs(pairs_file1, pairs_file2)
    results = []
    count = 0
    with open("arbitrage_results.json", 'w') as file:
                file.write('[')
    for pair in similar_pairs:
        kucoin_new_pair_good_format = kucoin_symbol_format(pair)
        binance_price, kucoin_price = find_prices_of_similar_pairs(pair, kucoin_new_pair_good_format)
        pair, binance_price, kucoin_price, optimal_amount, max_profit = profit_w_optimal_amount(binance_price, kucoin_price, binance_fee, kucoin_fee, pair)
        result = {
                'pair': pair,
                'binance_price': binance_price,
                'kucoin_price': kucoin_price,
                'optimal_amount': optimal_amount,
                'max_profit': max_profit
        }
        if max_profit > 0:
            
            with open("arbitrage_results.json", "a") as file:
                json.dump(result, file, indent=4)
                file.write(",\n")  # Add a comma and a new line after each object
            # Remove the trailing comma and add the closing bracket
    with open("arbitrage_results.json", 'r') as file:
        content = file.read().strip()
        print(content[-1])
        content = content[:-1]
        with open("arbitrage_results.json", 'w') as file:
            file.write(content)
    with open("arbitrage_results.json", 'a') as file:
        file.write('\n]')
if __name__ == "__main__":
    main()
