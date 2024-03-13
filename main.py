#imports necssary modules
import discord
import os
import logging
import json
from discord.ext import commands
from dotenv import load_dotenv

#Reads from our config file
with open('config.json', 'r') as config_file:
	config = json.load(config_file)
	error_channels = config.get("error_channels",{})

#Function to update error channels in the config file
def update_config():
	with open('config.json', 'w') as config_file:
		json.dump(config, config_file, indent=4)

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

#Events
#Event command error
@bot.event
async def on_command_error(ctx, error):
	server_id = str(ctx.guild.id) #Gets the server error channel
	error_channel_name = error_channels.get(server_id)

	#If the error channel is not set, then we shall make a new one
	if not error_channel_id:
		error_channel_id = ctx.channel.id
		error_channels[server_id] = error_channel_id
		update_config()

	#Get or Create the error channel
	error_channel = ctx.guild.get_channel(error_channel_id)
	if not error_channel:
		error_channel = await ctx.guild.create_text_channel("bot-errors")

	#Send the error message
	await error_channel.send(f"An error occurred: {error}")

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
