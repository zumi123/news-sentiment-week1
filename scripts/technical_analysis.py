import os
import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as ta
import yfinance as yf

# === CONFIGURATION ===
USE_PYNANCE = True  # Set to False to use CSV files instead
TICKER = "AAPL"
CSV_PATH = "data/yfinance_data/AAPL_historical_data.csv"
OUTPUT_FOLDER = "outputs"

# === LOAD DATA ===
if USE_PYNANCE:
    print(f"Loading {TICKER} data using yfinance...")
    df = yf.Ticker(TICKER).history(start="2023-01-01", end="2023-12-31")
else:
    print(f"Loading data from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH, parse_dates=["Date"])
    df.set_index("Date", inplace=True)

# === CALCULATE INDICATORS ===
df["SMA_20"] = ta.sma(df["Close"], length=20)
df["RSI"] = ta.rsi(df["Close"], length=14)
df["MACD"] = ta.macd(df["Close"])["MACD_12_26_9"]

# === PLOTTING ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Plot 1: Close Price and SMA
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Close"], label="Close Price", color="blue")
plt.plot(df.index, df["SMA_20"], label="SMA 20", color="orange")
plt.title(f"{TICKER} - Close Price and 20-day SMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
sma_path = os.path.join(OUTPUT_FOLDER, f"{TICKER}_price_sma.png")
plt.savefig(sma_path)
plt.close()
print(f"Saved plot: {sma_path}")

# Plot 2: RSI
plt.figure(figsize=(12, 4))
plt.plot(df.index, df["RSI"], label="RSI", color="purple")
plt.axhline(70, color='red', linestyle='--', linewidth=1)
plt.axhline(30, color='green', linestyle='--', linewidth=1)
plt.title(f"{TICKER} - Relative Strength Index (RSI)")
plt.xlabel("Date")
plt.ylabel("RSI")
plt.legend()
plt.grid(True)
plt.tight_layout()
rsi_path = os.path.join(OUTPUT_FOLDER, f"{TICKER}_rsi.png")
plt.savefig(rsi_path)
plt.close()
print(f"Saved plot: {rsi_path}")

# Plot 3: MACD
plt.figure(figsize=(12, 4))
df["MACD"].plot(label="MACD", color="black")
plt.title(f"{TICKER} - MACD")
plt.xlabel("Date")
plt.ylabel("MACD Value")
plt.grid(True)
plt.legend()
plt.tight_layout()
macd_path = os.path.join(OUTPUT_FOLDER, f"{TICKER}_macd.png")
plt.savefig(macd_path)
plt.close()
print(f"Saved plot: {macd_path}")