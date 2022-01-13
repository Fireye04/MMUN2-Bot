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

@client.command(aliases=["h"])
async def help(ctx):
    await ctx.send("This message lacks assistance in any form!")

@client.command(aliases=["m"])
async def message(ctx):
    await ctx.send("It worked!")

@client.command(aliases=["c"])
@commands.has_role('<@&929940836475625513>')
async def crisis(ctx):
    ctx.send("CRISIS!!")


token = pickle.load( open( "token.p", "rb" ) )
client.run(token)