# YahooFinananceApplication
The provided code is a Python script that uses the Tkinter library to create a graphical user interface (GUI) window for displaying dividend history for a given ticker symbol using data from Yahoo Finance (via the yfinance library). Here's the documented version of the code:

python
Copy code
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

        # Resample the dividend data on a yearly basis and calculate the sum
        dividend_df = dividend_df.resample('Y').sum().reset_index()
        dividend_df['Year'] = dividend_df['Date'].dt.year

        # Create a bar plot of the dividend history
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
The script starts by importing the necessary libraries: tkinter for creating the GUI, messagebox from tkinter for displaying error or informational messages, pandas for working with data, matplotlib.pyplot for creating plots, datetime for handling date and time information, and yfinance for retrieving dividend data from Yahoo Finance.

The show_dividend_history function is defined to handle the button click event. It retrieves the ticker symbol entered in the GUI's entry field, checks if it is empty, and displays an error message if so. Otherwise, it attempts to retrieve the dividend data for the given ticker symbol using the yf.Ticker class from the yfinance library. If the dividend data is empty, it displays an informational message. Otherwise, it resamples the dividend data on a yearly basis, calculates the sum for each year, and creates a bar plot using matplotlib.pyplot to visualize the dividend history.

The main part of the script creates the GUI window using tkinter. It sets the window title and geometry, and then creates a label and an entry field for the user to input the ticker symbol. Additionally, a button is created with the label "Show Dividend History," and its command is set to the show_dividend_history function. Finally, the script starts the Tkinter event loop to display the GUI window and handle user interactions.

Note: Make sure you have the required libraries (tkinter, pandas, matplotlib, datetime, and yfinance) installed before running this script.
