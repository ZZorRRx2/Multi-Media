#imports necssary modules
import discord
import os
import logging
import json
from discord.ext import commands
from dotenv import load_dotenv

#Create a Discord Client instance and sets the command prefix
#Intents in discord help control the data this bot receive
#Here we are listening to all events that can happen
intents = discord.Intents.all() #Initalise an instance of intents  with all intents enabled
client = discord.Client(intents=intents) #Creates a Discord client instance with the defined intents
bot = commands.Bot(command_prefix='mm! ', intents=intents) #Creates a bot with the command prefix set to !

#Declare that the bot is ready and running
@bot.event #Marks event
async def on_ready(): #The event when the bot is ready and logged in
	print(f'Logged in as {bot.user.name}') #Our message telling all that the bot is ready

#Bot Commands
#Setting commands

#Main commands
@bot.command() #This is a command
async def greet(ctx): #the "greet" is a response for !greet. ctx allows the context of the command to be displayed where the called command occured
	response = 'Hello' #this holds the string for the response
	await ctx.send(response)

@bot.command()
async def list_command(ctx):
	response = 'A response'
	await ctx.send (response)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
	#Does user have permissions?
	if ctx.author.guild_permissions.administrator:
		if reason:
			await member.ban(reason=reason)
			await ctx.send(f"{member.mention} has been banned for: {reason}")
		else:
			await ctx.send("Reasoning needed")
	else:
		await ctx.send("Permissions Missing")

@bot.command()
async def unban(ctx, member_id: str, *, reason=None):
	if ctx.author.guild_permissions.administrator:
		if reason:
			await ctx.guild.unban(member_id, reason=reason)
			await ctx.send(f"{member_id} has been unbanned for {reason}")
			return
		else:
			await ctx.send("Reasoning needed")
	else:
		await ctx.send("Permissions Missing")
#Events
#Event command error
ERROR_LOG_CHANNEL_ID = 1217514929586835516
@bot.event
async def on_command_error(ctx, error):
	error_log_channel = bot.get_channel(ERROR_LOG_CHANNEL_ID)
	if error_log_channel is not None:
		await error_log_channel.send(f"An error occured in {ctx.guild.name} - {ctx.author.name}: {error}")
	else:
		print(f"Channel not found: {ERROR_LOG_CHANNEL_ID}")
	print(f"An error occurred in {ctx.guild.name} - {ctx.author.name}: {error}")

#Retrieve token from .env file
load_dotenv() #Takes our token from the .env file
bot.run(os.getenv('TOKEN')) #Runs the discord bot using our Token

#Set the logging settings
logging.basicConfig(level=logging.INFO,
	format='[%(asctime)s] [%(levelname)s]: %(messages)s',
	handlers=[
		logging.FileHandler('bot.log'), #saves logs to a file
		logging.StreamHandler() 	#Displays logs in the console
])
