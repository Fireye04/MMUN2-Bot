import discord
import asyncio


async def getHelp(ctx):
    #no help
    #await ctx.send("This message lacks assistance in any form!")
    embedVar = discord.Embed(title=f"Help", description="Command help", color= 0xe74c3c)
    embedVar.add_field(name="Create Country (.cc)", value="Creates a country", inline=False)
    embedVar.add_field(name="Statistics (.s)", value="Check your country statistics", inline=False)
    embedVar.add_field(name="Technology (.t)", value="Check your technological progression", inline=False)
    embedVar.add_field(name="Research (.r <tech>)", value="Research a specified tech", inline=False)
    embedVar.add_field(name="Actions (.a)", value="Preform country actions", inline=False)
    embedVar.add_field(name="Message (.m <country>)", value="Send a private message to anoter country", inline=False)

    await ctx.send(embed=embedVar)
