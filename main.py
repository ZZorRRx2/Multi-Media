#imports necssary modules
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

#Create a Discord Client instance and sets the command prefix
#Intents in discord help control the data this bot receive
#Here we are listening to all events that can happen
intents = discord.Intents.all() #Initalise an instance of intents  with all intents enabled
client = discord.Client(intents=intents) #Creates a Discord client instance with the defined intents
bot = command.Bot(command_prefix='!', intents=intents) #Creates a bot with the command prefix set to !

#Declare that the bot is ready and running
@bot.event #Marks event
async def on_ready(): #The event when the bot is ready and logged in
	print(f'Logged in as {bot.user.name}') #Our message telling all that the bot is ready

#Set the commands
@bot.command()
async def greet(ctx):
	resposne = 'Hello'
	await ctx.send(response)

@bot.command()
async def list_command(ctx):
	resonse = 'A response'
	await ctx.send (response)
