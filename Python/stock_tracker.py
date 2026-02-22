# CodeAlpha - Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 300
}

total_investment = 0

print("Stock Portfolio Tracker")
print("Available Stocks:", list(stock_prices.keys()))
print("Type 'done' to finish\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Added {stock_name}: ${investment}")
    else:
        print("Stock not available.")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio summary saved to portfolio_summary.txt")