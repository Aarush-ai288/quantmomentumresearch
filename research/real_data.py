import pandas as pd
import yfinance as yf

'''
data = {
    "Date": ["Jan 1", "Jan 2", "Jan 3"],
    "Price": [100,105,103]
}

table = pd.DataFrame(data)
print(table)
'''

data = yf.download("AAPL", start="2020-01-01",end="2025-01-01")
#print(data.head())

'''
Open - Price at beg of day
Close - Price at end of day (used for returns over time)
Low - lowest price 
High - highest price
'''

data["Return"] = data["Close"].pct_change()
print(data.head())