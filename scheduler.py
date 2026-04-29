import time
import schedule
import requests

def job():

    symbols = [

        # Mega Cap US
        "AAPL","MSFT","GOOG","AMZN","META","NVDA","TSLA","NFLX","AMD","INTC",

        # Finance
        "JPM","BAC","WFC","GS","MS","C","BLK","SCHW","AXP","USB",

        # Healthcare
        "JNJ","PFE","MRK","ABBV","UNH","LLY","TMO","DHR","BMY","CVS",

        # Consumer
        "WMT","COST","HD","LOW","NKE","SBUX","MCD","KO","PEP","PG",

        # Industrial
        "CAT","DE","BA","GE","MMM","HON","UPS","FDX","RTX","LMT",

        # Energy
        "XOM","CVX","COP","SLB","BP","OXY","PSX","MPC","VLO","EOG",

        # ETFs
        "SPY","QQQ","DIA","IWM","VTI","VOO","XLF","XLK","XLE","ARKK",

        # India NSE
        "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
        "SBIN.NS","LT.NS","ITC.NS","BHARTIARTL.NS","HINDUNILVR.NS",

        "AXISBANK.NS","KOTAKBANK.NS","WIPRO.NS","MARUTI.NS","BAJFINANCE.NS",
        "ASIANPAINT.NS","SUNPHARMA.NS","TITAN.NS","ULTRACEMCO.NS","ONGC.NS",

        # Extra Growth / Popular
        "SHOP","UBER","SQ","PLTR","SNOW","CRM","ADBE","ORCL","IBM","PYPL"
    ]

    success = 0
    fail = 0

    for symbol in symbols:
        try:
            requests.get(
                f"http://127.0.0.1:8000/fetch/{symbol}",
                timeout=20
            )
            print(f"Updated {symbol}")
            success += 1
        except:
            print(f"Failed {symbol}")
            fail += 1

    print(f"Cycle Complete | Success: {success} | Failed: {fail}")

# every 5 mins recommended
schedule.every(5).minutes.do(job)

print("Scheduler Running for 100+ Symbols...")

job()

while True:
    schedule.run_pending()
    time.sleep(1)