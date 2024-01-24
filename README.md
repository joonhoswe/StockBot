# StockBot

### Project Overview

This Discord bot is designed to provide real-time stock market updates directly within your Discord server.    

Tailored for individual investors or stock market enthusiasts, the bot offers personalized stock tracking and regular market updates, ensuring users are always in the loop with the latest financial information.

<img width="728" alt="Screenshot 2024-01-21 at 3 18 51 PM" src="https://github.com/joonhoswe/StockBot/assets/149014867/d7e24bc5-2c4a-4ccd-96d9-09d70c6939d4">

### Features

Stock Watchlist: Users can add or remove stocks to their personal watchlist, allowing for customized tracking of specific stocks.    

Real-Time Updates: The bot fetches the latest stock prices using the Alpha Vantage API, providing up-to-date market information.    

Direct Messaging: Stock updates are sent directly to users, ensuring a clutter-free experience and personal data privacy.  

Easy Interaction: Users can interact with the bot using simple commands to add or remove stocks from their watchlist or to set their refresh rate for updates.

### Commands

!addstock <TICKER>: Adds a stock to the user's watchlist and reports its current price.  

<img width="452" alt="Screenshot 2024-01-21 at 3 20 01 PM" src="https://github.com/joonhoswe/StockBot/assets/149014867/7f2cda1b-0ffc-4c3e-affe-071a38c17450">

!removestock <TICKER>: Removes a stock from the user's watchlist.  

<img width="343" alt="Screenshot 2024-01-21 at 3 20 44 PM" src="https://github.com/joonhoswe/StockBot/assets/149014867/7c5861c9-75c4-441f-b882-bd95548e58fc">

!stockPrice <TICKER>: Returns current stock price.

<img width="447" alt="Screenshot 2024-01-21 at 3 21 24 PM" src="https://github.com/joonhoswe/StockBot/assets/149014867/8d51ab96-e8ee-4e40-bafc-402aa01f41bb">

!showStocks: Returns watchlist of stocks.

<img width="465" alt="Screenshot 2024-01-21 at 3 21 32 PM" src="https://github.com/joonhoswe/StockBot/assets/149014867/f0dbdc52-d491-41eb-8d7f-8d009182bf8d">


### Installation and Setup 

Set up environment variables for your Discord token and Alpha Vantage API key.  

Enter your Discord Channel ID.  

Run the bot using python bot.py.

### Technologies Used

Discord.py: A Python library for interacting with the Discord API, used for creating and managing the bot.  

Alpha Vantage API: Provides the financial data and real-time stock prices.  

Python: The primary programming language used for the development of this bot.
