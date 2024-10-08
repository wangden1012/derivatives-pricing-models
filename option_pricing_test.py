"""
Script testing functionalities of option_pricing package:
- Testing stock data fetching from Yahoo Finance using pandas-datareader
- Testing Black-Scholes option pricing model   
"""

from option_pricing import BlackScholesModel, MonteCarloPricing, BinomialTreeModel, Ticker

# Fetching the prices from yahoo finance
data = Ticker.get_historical_data('TSLA')
print(Ticker.get_columns(data))
print(Ticker.get_last_price(data, 'Adj Close'))
Ticker.plot_data(data, 'TSLA', 'Adj Close')

# Black-Scholes model testing
BSM = BlackScholesModel(100, 100, 365, 0.1, 0.2)
print(BSM.calculate_option_price('Call Option'))
print(BSM.calculate_option_price('Put Option'))




