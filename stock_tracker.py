import yfinance as yf
import pandas as pd
portfolio = {
    'AAPL': [10, 150],
    'TSLA': [5, 200]    
}
portfolio['GOOG']=[7,250]
del portfolio['AAPL']
symbols = list(portfolio.keys())
data = yf.download(symbols, period="1d", auto_adjust=False)['Close']
current_prices = data.iloc[-1] if not data.empty else None
if current_prices is not None:
    df = pd.DataFrame.from_dict(portfolio, orient='index', columns=['Quantity', 'Purchase_Price'])
    df['Current_Price'] = df.index.map(current_prices.to_dict())
    df['Value'] = df['Quantity'] * df['Current_Price']
    df['Cost'] = df['Quantity'] * df['Purchase_Price']
    df['P/L'] = df['Value'] - df['Cost']
    
    print("\nPortfolio Summary:")
    print(df[['Quantity', 'Purchase_Price', 'Current_Price', 'P/L']])
else:
    print("Failed to fetch data.")