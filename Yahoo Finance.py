import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
                                                                                    
# Create a function to handle the button click event
def show_dividend_history():
    ticker_symbol = ticker_entry.get()

    if not ticker_symbol:
        messagebox.showerror('Error', 'Please enter a ticker symbol')
        return

    try:
        ticker = yf.Ticker(ticker_symbol)
        dividend_df = ticker.dividends

        if dividend_df.empty:
            messagebox.showinfo('No Dividends', 'No dividend data available for the specified ticker symbol')
            return

        dividend_df = dividend_df.resample('Y').sum().reset_index()
        dividend_df['Year'] = dividend_df['Date'].dt.year

        plt.figure()
        plt.bar(dividend_df['Year'], dividend_df['Dividends'])
        plt.ylabel('Dividend Yield')
        plt.xlabel('Dividend History')
        plt.title(f'Dividend History for {ticker_symbol}')
        plt.xlim(dividend_df['Year'].min(), dividend_df['Year'].max())
        plt.show()
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Create the main window
window = tk.Tk()
window.title('Dividend History')
window.geometry('400x200')

# Create a label and an entry field for the ticker symbol
ticker_label = tk.Label(window, text='Enter Ticker Symbol:')
ticker_label.pack()

ticker_entry = tk.Entry(window)
ticker_entry.pack()

# Create a button to show the dividend history
show_button = tk.Button(window, text='Show Dividend History', command=show_dividend_history)
show_button.pack()

# Start the Tkinter event loop
window.mainloop()
