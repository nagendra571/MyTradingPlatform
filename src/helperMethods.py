import pandas as pd
import yfinance as yf
from datetime import datetime

from datetime import datetime, timedelta
from urllib.parse import quote_plus
import feedparser

WATCHLIST_PATH = "C:\\Nagendra\\Code\\Files\\Book1.xlsx"

def get_float(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        return info["floatShares"]
    except Exception as e:
        print("Error reading watchlist:", e)
        return 0

# ---------------------------------------------
# Simulate your data (replace with your real Excel read)
# ---------------------------------------------
def load_watchlist():
    try:
        df = pd.read_excel(WATCHLIST_PATH)
        df.columns = [c.strip().lower() for c in df.columns]
        df = df.dropna(subset=['symbol'])
        df['Float'] = df.apply(lambda row: get_float(row.symbol)/1000000, axis = 1)
        df_filtered = df[df['net chng'] > 0]
        return df_filtered
    except Exception as e:
        print("Error reading watchlist:", e)
        return pd.DataFrame()

def get_stock_news_URL(ticker, days=90): 
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    query = quote_plus(f'{ticker} OR {ticker} after:{start_date.strftime("%Y-%m-%d")} before:{end_date.strftime("%Y-%m-%d")}')
    return  f'https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en'


# ---------------------------------------------
# Fetch news (you already have your logic)
# ---------------------------------------------

def get_news_for_stock(ticker, days=1): 
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    rss_url = get_stock_news_URL(ticker, days)
    
    feed = feedparser.parse(rss_url)
    
    news_items = []
    for entry in feed.entries[:100]:  # Hardcoded max 100 articles
        try:
            news_items.append({
                'date': entry.get('published', 'N/A'),
                'title': entry.title,
                'url': entry.link,
                'source': entry.get('source', {}).get('title', 'N/A'),
                'company': ticker,
                'ticker': ticker
            })
        except:
            continue
    
    df = pd.DataFrame(news_items)
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        df_sorted = df.sort_values(by = 'date', ascending= False)
    return df_sorted


# ---------------------------------------------
# Dummy AI analysis (replace later with real LLM call)
# ---------------------------------------------
def get_ai_analysis(symbol):
    return f"AI Analysis for {symbol}:\n\n{symbol} shows strong volume activity, bullish setup in short term."










