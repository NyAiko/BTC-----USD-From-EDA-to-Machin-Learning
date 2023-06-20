import yfinance as yf
import datetime
# Define the ticker symbol for Bitcoin
symbol = "BTC-USD"

# Define the start and end dates for the data
start_date = "2010-01-01"
end_date = datetime.date.today().strftime("%Y-%m-%d")

# Use yfinance to fetch the Bitcoin price data
data = yf.download(symbol, start=start_date, end=end_date)

# Print the collected data
print(data)