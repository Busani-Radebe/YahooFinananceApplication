import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import matplotlib.pyplot as plt

# Create the main window
window = tk.Tk()
window.title('Financial Statistics')
window.geometry('400x300')

# Function to display error messages
def show_error_message(message):
    messagebox.showerror('Error', message)

# Function to open a URL link
def open_link(url):
    import webbrowser
    webbrowser.open_new(url)

# Function to show historical data graph
def show_historical_data():
    ticker_symbol = ticker_entry.get()

    if not ticker_symbol:
        messagebox.showerror('Error', 'Please enter a ticker symbol')
        return

    try:
        ticker = yf.Ticker(ticker_symbol)
        historical_data = ticker.history(period='max')

        plt.figure()
        plt.plot(historical_data['High'])
        plt.ylabel('High')
        plt.xlabel('Date')
        plt.title(f'Historical High Prices for {ticker_symbol}')
        plt.show()
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Function to show number of shares outstanding
def show_num_shares():
    ticker_symbol = ticker_entry.get()

    if not ticker_symbol:
        messagebox.showerror('Error', 'Please enter a ticker symbol')
        return

    try:
        ticker = yf.Ticker(ticker_symbol)
        num_shares = ticker.info['sharesOutstanding']
        messagebox.showinfo('Number of Shares', f'The number of outstanding shares for {ticker_symbol} is {num_shares}')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Function to show news articles
def show_news():
    ticker_symbol = ticker_entry.get()

    if not ticker_symbol:
        messagebox.showerror('Error', 'Please enter a ticker symbol')
        return

    try:
        ticker = yf.Ticker(ticker_symbol)
        news = ticker.news

        if len(news) == 0:
            messagebox.showinfo('No News', 'No news articles available for the specified ticker symbol')
            return

        # Create a new window to display the news articles
        news_window = tk.Toplevel(window)
        news_window.title('News Articles')
        news_window.geometry('600x400')

        # Create a scrollable text widget to display the news articles
        news_text = tk.Text(news_window, height=20, width=80)
        news_text.pack()

        # Display each news article with clickable links
        for article in news:
            title = article['title']
            link = article['link']
            news_text.insert(tk.END, title + '\n')
            news_text.insert(tk.END, link + '\n\n')
            # Make the link clickable
            news_text.tag_configure('link', foreground='blue', underline=True)
            news_text.tag_bind('link', '<Button-1>', lambda event, url=link: open_link(url))
            news_text.insert(tk.END, '\n')

    except Exception as e:
        show_error_message(f'An error occurred: {str(e)}')

# Function to show dividend history on a graph
def show_dividend_history():
    ticker_symbol = ticker_entry.get()

    if not ticker_symbol:
        messagebox.showerror('Error', 'Please enter a ticker symbol')
        return

    try:
        ticker = yf.Ticker(ticker_symbol)
        dividend_history = ticker.dividends

        if len(dividend_history) == 0:
            messagebox.showinfo('No Dividend History', 'No dividend history available for the specified ticker symbol')
            return

        plt.figure()
        plt.plot(dividend_history)
        plt.ylabel('Dividends')
        plt.xlabel('Date')
        plt.title(f'Dividend History for {ticker_symbol}')
        plt.show()

    except Exception as e:
        show_error_message(f'An error occurred: {str(e)}')

# Create a label and entry for the ticker symbol
ticker_label = tk.Label(window, text='Enter Ticker Symbol:')
ticker_label.pack()

ticker_entry = tk.Entry(window)
ticker_entry.pack()

# Create buttons for various actions
historical_button = tk.Button(window, text='Show Historical Data', command=show_historical_data)
historical_button.pack()

shares_button = tk.Button(window, text='Show Shares Outstanding', command=show_num_shares)
shares_button.pack()

news_button = tk.Button(window, text='Show News', command=show_news)
news_button.pack()

dividend_button = tk.Button(window, text='Show Dividend History', command=show_dividend_history)
dividend_button.pack()

# Start the main loop
window.mainloop()
