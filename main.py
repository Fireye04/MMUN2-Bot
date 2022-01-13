import discord
import pickle
import asyncio
import pandas as pd
# https://www.freecodecamp.org/news/connect-python-with-sql/
import mysql.connector
from mysql.connector import Error
from discord.ext import commands 
client = commands.Bot(command_prefix=".")
client.remove_command('help')

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    await client.process_commands(message)

@client.command(aliases=["m"])
async def message(ctx):
    await ctx.send("It worked!")


token = pickle.load( open( "token.p", "rb" ) )
client.run(token)