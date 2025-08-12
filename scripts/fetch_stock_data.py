import os
import yfinance as yf
import psycopg2

def fetch_and_store():
    symbol = "AAPL"
    data = yf.download(symbol, period="1d", interval="1h")

    if data.empty:
        print("No data fetched.")
        return

    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="postgres"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_data (
            datetime TIMESTAMP,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume BIGINT
        )
    """)

    for index, row in data.iterrows():
        cur.execute(
            "INSERT INTO stock_data VALUES (%s, %s, %s, %s, %s, %s)",
            (index.to_pydatetime(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume'])
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Data stored successfully!")
