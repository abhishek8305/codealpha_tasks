import yfinance as yf
import pandas as pd
from tabulate import tabulate

# ----------------------------
# Portfolio definition
# ----------------------------
portfolio = {
    'AAPL': {'shares': 10, 'buy_price': 180},
    'MSFT': {'shares': 5, 'buy_price': 330},
    'GOOGL': {'shares': 8, 'buy_price': 140},
    'TSLA': {'shares': 3, 'buy_price': 220}
}

# ----------------------------
# Fetch live data from Yahoo Finance
# ----------------------------
tickers = list(portfolio.keys())
data = yf.download(tickers=tickers, period='1d', interval='1d')['Close'].iloc[-1]

# ----------------------------
# Calculate metrics
# ----------------------------
rows = []
total_value = 0
total_investment = 0

for ticker, info in portfolio.items():
    shares = info['shares']
    buy_price = info['buy_price']
    current_price = data[ticker]
    current_value = shares * current_price
    investment = shares * buy_price
    profit_loss = current_value - investment
    profit_percent = (profit_loss / investment) * 100

    total_value += current_value
    total_investment += investment

    rows.append([
        ticker,
        shares,
        f"${buy_price:.2f}",
        f"${current_price:.2f}",
        f"${current_value:,.2f}",
        f"${profit_loss:,.2f}",
        f"{profit_percent:.2f}%"
    ])

# ----------------------------
# Summary
# ----------------------------
total_profit = total_value - total_investment
total_profit_percent = (total_profit / total_investment) * 100

# ----------------------------
# Display output
# ----------------------------
print("\n STOCK PORTFOLIO TRACKER ")
print(tabulate(rows, headers=[
    "Ticker", "Shares", "Buy Price", "Current Price", "Value", "P/L ($)", "P/L (%)"
]))
print("\n-----------------------------------")
print(f"Total Investment: ${total_investment:,.2f}")
print(f"Current Value:     ${total_value:,.2f}")
print(f"Total P/L:         ${total_profit:,.2f} ({total_profit_percent:.2f}%)")
print("-----------------------------------\n")