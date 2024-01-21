# StockBot

### Project Overview

This Discord bot is designed to provide real-time stock market updates directly within your Discord server. Tailored for individual investors or stock market enthusiasts, the bot offers personalized stock tracking and regular market updates, ensuring users are always in the loop with the latest financial information.

### Features

Stock Watchlist: Users can add or remove stocks to their personal watchlist, allowing for customized tracking of specific stocks.
Real-Time Updates: The bot fetches the latest stock prices using the Alpha Vantage API, providing up-to-date market information.
User-Defined Refresh Rates: Users can set their preferred refresh rate, determining how often they receive stock updates.
Direct Messaging: Stock updates are sent directly to users, ensuring a clutter-free experience and personal data privacy.
Easy Interaction: Users can interact with the bot using simple commands to add or remove stocks from their watchlist or to set their refresh rate for updates.

### Commands

!addstock <TICKER>: Adds a stock to the user's watchlist and reports its current price.
!removestock <TICKER>: Removes a stock from the user's watchlist.
!refreshRate <MINUTES>: Sets the refresh rate for how often the user receives stock updates.
Installation and Setup

### Setup

Install the required dependencies using pip install -r requirements.txt.
Set up environment variables for your Discord token and Alpha Vantage API key.
Enter your Discord Channel ID.
Run the bot using python bot.py.

### Technologies Used

Discord.py: A Python library for interacting with the Discord API, used for creating and managing the bot.
Alpha Vantage API: Provides the financial data and real-time stock prices.
Python: The primary programming language used for the development of this bot.
