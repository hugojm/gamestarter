# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import requests
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
cg = CoinGeckoAPI()

bot = commands.Bot(command_prefix='$')


@bot.command(name='game_price', help="Responds with the $GAME price and some other metrics")
async def game_price(ctx):
    api_result = cg.get_price(ids='gamestarter', vs_currencies='usd', include_24hr_vol='true',
                              include_24hr_change='true', include_last_updated_at='true')
    response = 'Current price: ' + str(round(api_result['gamestarter']['usd'], 3)) + '$ \n' + '24hr volume: ' + str(round(api_result['gamestarter']['usd_24h_vol'], 3)) + '$ \n' + '24hr change: ' + str(
        round(api_result['gamestarter']['usd_24h_change'], 3)) + '% \n' + 'Last update: ' + str(datetime.fromtimestamp(api_result['gamestarter']['last_updated_at']))

    await ctx.send(response)

@bot.command(name='dark_price', help="Responds with the $DARK price and some other metrics")
async def game_price(ctx):
    api_result = cg.get_price(ids='dark-frontiers', vs_currencies='usd', include_24hr_vol='true',
                              include_24hr_change='true', include_last_updated_at='true')
    response = 'Current price: ' + str(round(api_result['dark-frontiers']['usd'], 3)) + '$ \n' + '24hr volume: ' + str(round(api_result['dark-frontiers']['usd_24h_vol'], 3)) + '$ \n' + '24hr change: ' + str(
        round(api_result['dark-frontiers']['usd_24h_change'], 3)) + '% \n' + 'Last update: ' + str(datetime.fromtimestamp(api_result['dark-frontiers']['last_updated_at']))

    await ctx.send(response)


@bot.command(name='eth_gas', help="Responds with the Etherium gas price")
async def gas_eth_price(ctx):
    response = requests.get('https://ethgasstation.info/api/ethgasAPI.json?api-key=6436bcefcdf39761538d2e76ac2729d1b0eea11c2f3c7091e05068990365')
    dict = json.loads(response.content)
    response = 'Recommended fast: ' + str(dict['fast']/10) + ' gwei \n' + 'Fastest: ' + str(dict['fastest']/10) + ' gwei \n' + 'Average: ' + str(dict['average']/10) + ' gwei \n' + 'Block time: ' + str(round(dict['block_time'],3))+ 's'

    await ctx.send(response)

@bot.command(name='bsc_gas', help="Responds with the Binance Smart Chain gas price")
async def gas_bsc_price(ctx):
    response = requests.get('https://bscgas.info/gas?apikey=4e161255deaa4859aa1e1e5c0b85cb9b')
    dict = json.loads(response.content)
    response = response = 'Recommended fast: ' + str(dict['fast']) + ' gwei \n' + 'Fastest: ' + str(dict['instant']) + ' gwei \n' + 'Average: ' + str(dict['standard']) + ' gwei \n' + 'Block time: ' + str(round(dict['block_time'],3))+ 's'

    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)
