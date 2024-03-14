import discord
import os
import logging
import json
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='mm! ', intents =intents)

@bot.event
async def on_ready():
	print(f'Loggind in as {bot.user.name}')
ERROR_LOG_CHANNEL_ID = 1217514929586835516
@bot.event
async def on_command_error(ctx, error):
	error_log_channel = bot.get_channel(ERROR_LOG_CHANNEL_ID)
	if error_log_channel is not None:
		await error_log_channel.send(f"Error in {ctx.guild.name}: {error}")
	else:
		print(f"channel not found")

load_dotenv()
bot.run(os.getenv('TOKEN'))

logging.basicConfig(level=logging.INFO,
	format='[%(asctime)s] [%(levelname)s]: %(messages)s',
		handlerse=[
			logging.FileHandler('bot.log'),
			logging.StreamHandler()
])
