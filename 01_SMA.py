#SMA.py
import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt

sma_length = 21 # Adjust this to test dif MA's
ticker = "BTC-USD" # Bitcoin / USD chart
period = "3mo" # 3 months of data
interval = "1d" # 1D timeframe (candles)

# Fetch data
df = yf.download(ticker, period=period, interval=interval)

# Calculate SMA
df["SMA"] = df ["Close"].rolling(window=sma_length).mean()

# Plot price & SMA
plt.figure(figsize=(14, 6))
plt.plot(df["Close"], label="BTC Price", linewidth=1.5)
plt.plot(df["SMA"], label=f"SMA-{sma_length}", linewidth=2, color="orange")
plt.title(f"{ticker} with {sma_length}-Period SMA")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()