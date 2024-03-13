#imports necssary modules
import discord
import os
import logging
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

#Set the commands
@bot.command() #This is a command
async def greet(ctx): #the "greet" is a response for !greet. ctx allows the context of the command to be displayed where the called command occured
	response = 'Hello' #this holds the string for the response
	await ctx.send(response)

@bot.command()
async def list_command(ctx):
	response = 'A response'
	await ctx.send (response)

#Events
@bot.event
async def on_command_error(ctx, error):
	error_message = f'Error occured while processing command: {error}'
	logging.error(error_message)
	await ctx.send(error_message)

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
