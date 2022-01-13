import discord
import pickle
import asyncio
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

client.run("")