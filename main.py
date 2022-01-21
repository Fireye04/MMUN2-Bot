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

#@client.event
#async def on_message(message):
    #any on message shit goes here. (non commands, just actions to take on message)
    #pass
        
            
        
    #await client.process_commands(message)

@client.command(aliases=["h"])
async def help(ctx):
    #no help
    await ctx.send("This message lacks assistance in any form!")

@client.command(aliases=["m"])
async def messageCountry(ctx, args):
    #ideally creates a new chat/thread for any chats
    exist = False
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
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="GERMANY")
        
        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "germany-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=930978865654927421)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "germany-" + aRoleName)

            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
        else:
            channel = await ctx.guild.create_text_channel("germany-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
        
        
        
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)
        
        await ctx.message.delete()
    
    elif target in germany and aRole.name == "Germany":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    elif target in us and aRole.name != "US":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="US")

        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "us-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=930978983800098837)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "us-" + aRoleName)

            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
        else:
            
            channel = await ctx.guild.create_text_channel("us-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
        
        
        
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)
        
        await ctx.message.delete()
    elif target in us and aRole.name == "US":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    elif target in france and aRole.name != "France":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="FRANCE")

        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "france-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=933471681530462299)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "france-" + aRoleName)

            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
        else:
            
            channel = await ctx.guild.create_text_channel("france-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
        
        
        
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)
        
        await ctx.message.delete()
    elif target in france and aRole.name == "France":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    elif target in russia and aRole.name != "Russia":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="RUSSIA")

        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "russia-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=933471787776368640)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "russia-" + aRoleName)

            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
        else:
            
            channel = await ctx.guild.create_text_channel("russia-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
        
        
        
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)
        
        await ctx.message.delete()
    elif target in russia and aRole.name == "Russia":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    elif target in ottoman and aRole.name != "Ottoman":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="OTTOMAN")

        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "ottoman-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=933471880806014986)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "ottoman-" + aRoleName)

            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
        else:
            
            channel = await ctx.guild.create_text_channel("ottoman-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
        
        
        
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)
        
        await ctx.message.delete()
    elif target in ottoman and aRole.name == "Ottoman":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    elif target in japan and aRole.name != "Japan":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="JAPAN")

        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "japan-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=933471997059551272)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "japan-" + aRoleName)

            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
            
        else:
            
            channel = await ctx.guild.create_text_channel("japan-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
        
        
        
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)
        
        await ctx.message.delete()
    elif target in japan and aRole.name == "Japan":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    elif target in china and aRole.name != "China":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="CHINA")

        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "china-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=930978937440460851)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "china-" + aRoleName)
            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
            
        else:
            
            channel = await ctx.guild.create_text_channel("china-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
        
        
        
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)
        
        await ctx.message.delete()
    elif target in china and aRole.name == "China":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    elif target in italy and aRole.name != "Italy":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="ITALY")

        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "italy-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=930979017610367066)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "italy-" + aRoleName)
            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
            
        else:
            
            channel = await ctx.guild.create_text_channel("italy-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
        
        
        
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)
        
        await ctx.message.delete()
    elif target in italy and aRole.name == "Italy":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    elif target in ireland and aRole.name != "Ireland":
        
        await ctx.send("Configuring chat with " + target + "...", delete_after=3)
        
        category = get(ctx.guild.categories, name="IRELAND")

        aRoleName = aRole.name.lower()
        
        for channel in ctx.guild.channels:
            if channel.name == "ireland-" + aRoleName:
                exist = True
                break
            else:
                exist = False

        uRole = get(ctx.guild.roles, id=930978900803215410)
        
        if exist == True:
            channel = get(ctx.guild.channels, name = "ireland-" + aRoleName)
            await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
        else:
            
            channel = await ctx.guild.create_text_channel("ireland-" + aRole.name, category=category)
            await channel.set_permissions(aRole, view_channel=True)
            await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)       
        
        
        
        await ctx.message.delete()
    elif target in ireland and aRole.name == "Ireland":
        await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
    else:
        await ctx.send("Could not find country. Please try again", delete_after=5)
        await ctx.message.delete()
    # await ctx.send("It worked!")

@client.command(aliases=["c"])
# only chair can use
@commands.has_role(929940836475625513)
async def crisis(ctx):
    await ctx.send("CRISIS!!")

token = pickle.load(open("token.p", "rb"))
client.run(token)