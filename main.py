import discord
import pickle
import asyncio
#import pandas as pd
from discord.utils import get    
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
async def message(ctx, args):
    #ideally creates a new chat/thread for any chats
    countryRoles = []
    role = get(ctx.guild.roles, id=930978865654927421)
    countryRoles.append(role)
    role = get(ctx.guild.roles, id=930978983800098837)
    countryRoles.append(role)
    role = get(ctx.guild.roles, id=933471681530462299)
    countryRoles.append(role)
    role = get(ctx.guild.roles, id=933471787776368640)
    countryRoles.append(role)
    role = get(ctx.guild.roles, id=933471880806014986)
    countryRoles.append(role)
    role = get(ctx.guild.roles, id=933471997059551272)
    countryRoles.append(role)
    role = get(ctx.guild.roles, id=930978937440460851)
    countryRoles.append(role)
    role = get(ctx.guild.roles, id=930979017610367066)
    countryRoles.append(role)
    role = get(ctx.guild.roles, id=930978900803215410)
    countryRoles.append(role)

    germany = ["Germany", "germany"]
    
    us = ["US", "us", "United States", "united states"]

    france = ["France", "france"]

    russia = ["Russia", "russia"]

    ottoman = ["Ottoman", "Ottoman Empire", "ottoman empire", "ottoman", "Ottomans", "ottomans"]

    china = ["China", "china"]

    japan = ["japan", "Japan"]

    italy = ["Italy", "italy"]

    ireland = ["Ireland", "ireland"]
    
    author = ctx.message.author
    #init aRole as @everyone, reassigned later
    aRole = get(ctx.guild.roles, id=929935033869951016)
    target = args
    print("from- "+ author.name + "\nto- " + target)

    for i, role in enumerate(countryRoles):
        if role in author.roles:
            aRole = role
    
    if target in germany and aRole.name != "Germany":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=5)
        
        category = get(ctx.guild.categories, name="GERMANY")

        channel = await ctx.guild.create_text_channel(aRole.name + "-" + target, category=category)
        
        gRole = get(ctx.guild.roles, id=930978865654927421)
        
        await channel.send("Channel configuration success! " + gRole.mention + ", " + aRole.mention)
        
        await bot.delete_message(ctx.message)
        
    if target in germany and aRole.name == "Germany":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.")
    else:
        print("lose")
    await ctx.send("It worked!")

@client.command(aliases=["c"])
# only chair can use
@commands.has_role(929940836475625513)
async def crisis(ctx):
    await ctx.send("CRISIS!!")

token = pickle.load(open("token.p", "rb"))
client.run(token)