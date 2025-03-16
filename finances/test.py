import yfinance as yf

def get_nifty_data(choice):
    nifty = yf.Ticker("^NSEI")  # NIFTY 50 symbol on Yahoo Finance
    
    if choice == 1:
        # Fetch last 3 daily closing prices
        historical_data = nifty.history(period="5d")
        closing_prices = historical_data["Close"].dropna().tail(3).round(1).tolist()
        print("Last 3 daily closing prices of NIFTY 50:", closing_prices)
    
    elif choice == 2:
        # Fetch last 3 one-minute interval prices
        historical_data = nifty.history(period="1d", interval="1m")
        closing_prices = historical_data["Close"].dropna().tail(3).round(1).tolist()
        print("Last 3 one-minute interval prices of NIFTY 50:", closing_prices)

    else:
        print("Invalid choice! Please enter 1 or 2.")

# User input
choice = int(input("Enter 1 for last 3 daily closing prices, 2 for last 3 one-minute interval prices: "))
get_nifty_data(choice)
