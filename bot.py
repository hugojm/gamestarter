# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI
from datetime import datetime


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
cg = CoinGeckoAPI()

bot = commands.Bot(command_prefix='!')


@bot.command(name='price')
async def game_price(ctx):
    api_result = cg.get_price(ids='gamestarter', vs_currencies='usd', include_24hr_vol='true',
                              include_24hr_change='true', include_last_updated_at='true')
    response = 'Current price: ' + str(round(api_result['gamestarter']['usd'], 3)) + '$ \n' + '24hr volume: ' + str(round(api_result['gamestarter']['usd_24h_vol'], 3)) + '$ \n' + '24hr change: ' + str(
        round(api_result['gamestarter']['usd_24h_change'], 3)) + '% \n' + 'Last update: ' + str(datetime.fromtimestamp(api_result['gamestarter']['last_updated_at']))

    await ctx.send(response)

bot.run(TOKEN)
