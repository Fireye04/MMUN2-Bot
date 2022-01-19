import discord
import pickle
import asyncio
#import pandas as pd

from discord.ext import commands 
client = commands.Bot(command_prefix=".")
client.remove_command('help')





@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    #any on message shit goes here. (non commands, just actions to take on message)
    await client.process_commands(message)

@client.command(aliases=["h"])
async def help(ctx):
    #no help
    await ctx.send("This message lacks assistance in any form!")

@client.command(aliases=["m"])
async def message(ctx):
    #
    await ctx.send("It worked!")

@client.command(aliases=["c"])
# only chair can use
@commands.has_role(929940836475625513)
async def crisis(ctx):
    await ctx.send("CRISIS!!")


token = pickle.load( open( "token.p", "rb" ) )
client.run(token)