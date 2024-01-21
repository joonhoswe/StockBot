import os
import discord
import asyncio
from alpha_vantage.timeseries import TimeSeries
from collections import defaultdict
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # To access message content

bot = commands.Bot(command_prefix="!", intents=intents)

# Global variable for the stock list
stock_list = []

# Dictionary to hold user preferences
user_stocks = defaultdict(set)

@bot.command(name='greet')
async def greet(ctx):
   await ctx.send("hello")

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f'{bot.user} is connected to the following guild:\n{guild.name}(id: {guild.id})')
    bot.loop.create_task(stock_update_every_30_minutes())

# Function to get stock data 
    
async def get_stock_data(ticker):
    """ Fetches stock data for a given ticker symbol using Alpha Vantage. """
    try:
        data, _ = ts.get_quote_endpoint(symbol=ticker)
        if not data.empty:
            # Extracting the price from the returned DataFrame
            price = data['05. price'][0]
            return {"regularMarketPrice": price}
        else:
            print(f"No data found for {ticker}")
            return None
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Adds a stock to user's watch list
      
@bot.command(name='addStock')
async def add_stock(ctx, ticker: str):
    """ Adds a stock to the watchlist and reports its current price """
    ticker = ticker.upper()  # Convert ticker to uppercase
    if ticker not in stock_list:
        stock_info = await get_stock_data(ticker)
        if stock_info:
            current_price = stock_info['regularMarketPrice']
            stock_list.append(ticker)
            await ctx.send(f"{ticker} added to the watchlist. Current Price: {current_price}")
        else:
            await ctx.send(f"Failed to fetch data for {ticker}.")
    else:
        await ctx.send(f"{ticker} is already in the watchlist.")

# Removes a stock given a ticker
        
@bot.command(name='removeStock')
async def remove_stock(ctx, ticker: str):
    ticker = ticker.upper()  # Convert ticker to uppercase for consistency
    if ticker in stock_list:
        stock_list.remove(ticker)
        await ctx.send(f"{ticker} removed from the watchlist.")
    else:
        await ctx.send(f"{ticker} is not in the watchlist.")

# Fetches current stock price given a ticker

@bot.command(name='stockPrice')
async def stock_price(ctx, *tickers):
    for ticker in tickers:
        try:
            data, _ = ts.get_quote_endpoint(symbol=ticker)
            price = data['05. price'][0]
            await ctx.send(f"{ticker}: {price}")
        except Exception as e:
            await ctx.send(f"Error fetching price for {ticker}: {e}")
    
# Function to continuously give stock updates every 15 minutes in the form of a Discord chat msg
            
async def stock_update_every_15_minutes():
    await bot.wait_until_ready()
    channel = bot.get_channel(1133386948690579468)  # Replace with your channel ID!
    while not bot.is_closed():
        if stock_list:  # Check if the stock list is not empty
            messages = []
            for ticker in stock_list:
                try:
                    stock_info = await get_stock_data(ticker) 
                    msg = f"{ticker}: Current Price: {stock_info['regularMarketPrice']}"
                    messages.append(msg)
                except Exception as e:
                    print(f"Error fetching data for {ticker}: {e}")
            if messages:
                await channel.send('\n'.join(messages))
        else:
            print("No stocks in watchlist.")
        await asyncio.sleep(900)  # Sleep for 15 minutes (900 seconds) 

bot.run(TOKEN)