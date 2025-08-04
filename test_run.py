from stock_data import fetch_stock_data

# Get Apple's stock data from June 1 to July 1, 2024
data = fetch_stock_data("AAPL", "2024-06-01", "2024-07-01")

# Print the top 5 rows to check the output
print(data.head())
