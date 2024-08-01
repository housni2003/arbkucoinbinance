import numpy as np
import json
def arbitrage_profit(binance_price, kucoin_price, binance_fee, kucoin_fee, amount):
    """
    Calculate the profit from arbitrage given the parameters.
    """
    # Calculate the trading fees on both exchanges
    trading_fee_binance = amount * binance_price * binance_fee
    trading_fee_kucoin = amount * kucoin_price * kucoin_fee
    
    # Total fees include trading fees and fixed withdrawal/deposit fees
    total_fees = trading_fee_binance + trading_fee_kucoin

    # Calculate profit from price difference minus total fees
    profit = (binance_price - kucoin_price) * amount - total_fees
    
    return profit

def profit_w_optimal_amount(binance_price, kucoin_price, binance_fee, kucoin_fee, pair):
    max_profit = -np.inf
    optimal_amount = 0
    # Test different amounts to find the optimal one
    for amount in range(1, 10001):  # Adjust range as necessary
        profit = arbitrage_profit(binance_price, kucoin_price, binance_fee, kucoin_fee, amount)
        if profit > max_profit and profit > 0:
            max_profit = profit
            optimal_amount = amount
    if max_profit > 0:
        print(f"pair : {pair}, binance price : {binance_price}, kucoin_price : {kucoin_price}")
        print(f"Optimal Amount: {optimal_amount}")
        print(f"Max Profit: {max_profit:.4f} USDT")
        # Ensure file handling is correct
        # try:
        #     with open("arbitrage.txt", "a") as file:
        #         file.write(results)
        # except OSError as e:
        #     print(f"Error writing to file: {str(e)}")
    return pair, binance_price, kucoin_price, optimal_amount, max_profit

