import re
from datetime import datetime
# from random import randint
from random import choice

import nest_asyncio
from discord.ext import commands

from Commands.contact import *
from Commands.countryIntel import *
from Commands.functions import *
from Commands.help import *

nest_asyncio.apply()

intents = discord.Intents.all()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command('help')

"""
NOTES!
- Add religion
- Add governments


BRAINSTORM
- 1 unit of time
	- 24 hours

"""


# Do stuff when a time unit passes
async def timeUnit():
    with open('src/pickle/Countries', 'rb') as ctry:
        Countries = pickle.load(ctry)
    for target in Countries:
        await target.timeUnitC()
    save_object(Countries, "src/pickle/Countries")


botChannel = None


# when the bot is ready
# Used to run the time loop
@client.event
async def on_ready():
    global botChannel
    print("Ready")

    botChannel = get(client.get_guild(929935033869951016).channels, name="bot-announcements")

    # Time Units
    i = 0
    while True:
        tme = datetime.now()
        t = tme.strftime("%X")
        if i % 10 == 0:
            print(t)
        if i % 30 == 0:
            # await botChannel.send("One time unit has passed!")
            print("One time unit has passed!")
            await timeUnit()
        # midnight is 07:00:00
        if t == "20:8:00":
            # await botChannel.send("One time unit has passed!")
            await timeUnit()
        await asyncio.sleep(1)
        i += 1


# Countries = []


# save_object(Countries, "src/pickle/Countries")
# Countries = pickle.load("src/pickle/Countries")

# @client.event
# async def on_message(message):
# any on message shit goes here. (non commands, just actions to take on message)
# pass

# await client.process_commands(message)

# Help Command
@client.command(aliases=["h"])
async def help(ctx):
    # src/Commands/help.py
    await getHelp(ctx)


########CLASS INIT#########
async def aClassInitCategory(ctx, name, self):
    cat = await ctx.message.guild.create_category(name)
    await cat.create_text_channel(self.channelNames + "-general")
    return


async def aClassInitRoleCreate(ctx, name):
    await ctx.guild.create_role(name=name)
    return


async def aClassInitRoleAdd(ctx, name, self):
    manager = get(ctx.message.guild.members, id=self.managerID)
    await manager.add_roles(get(ctx.message.guild.roles, name=self.roleName))
    return


async def aClassInitChairChannel(ctx, name, chair, self):
    await chair.create_text_channel(self.chairChannelName)
    return


async def aClassInitChairPerms(ctx, name, self):
    cc = get(ctx.guild.channels, name=self.chairChannelName)
    print(self.chairChannelName)
    await cc.set_permissions(ctx.message.guild.default_role, view_channel=False)
    await cc.set_permissions(get(ctx.message.guild.roles, name=self.roleName), view_channel=True)
    return


########CLASS INIT#########

# Country class declaration
class Country:
    # on country creation, add government later
    # Note to self, check for duplicates, or previously owned countries
    def __init__(self, ctx, name):
        # Equal to categoryName and roleName
        self.name = name
        self.managerID = ctx.message.author.id
        # create country category
        self.channelNames = re.sub('[^A-Za-z0-9 ]+', '', self.name.lower()).replace(" ", "-")

        self.categoryName = name
        asyncio.run(aClassInitCategory(ctx, name, self))

        # Make a country role

        self.roleName = name
        asyncio.run(aClassInitRoleCreate(ctx, name))
        asyncio.run(aClassInitRoleAdd(ctx, name, self))

        # make a private chair DM

        chair = get(ctx.message.guild.categories, name='chair')

        self.chairChannelName = self.channelNames + "-chair"
        asyncio.run(aClassInitChairChannel(ctx, name, chair, self))

        asyncio.run(aClassInitChairPerms(ctx, name, self))

        # randomly assign base stats
        # Population
        # -Education
        # -Nationalism
        # Natural Resources
        # Wealth
        # -Income
        # Army
        # -Size
        # -Combat power
        # -Unit types
        # -Tactics
        # Infrastructure
        # -Standard of living
        # Tech
        # Awunga bunga

        """ UPDATED
        land size
        population
        education
        nationalism
        lumber, ore, uranium
        wealth, income, food
        standard of living
        army (specifics TBD)
        tech
        """
        # 8 OG, using other to cut uranium for now
        # stats = [1, 2, 4, 5, 5, 5, 8, 10]

        statsEdit = [1, 2, 4, 5, 5, 8, 10]

        def yoink(stat):
            global statsEdit
            e = choice(stat)
            statsEdit = stat.remove(e)
            return int(e)

        self.land_size = yoink(statsEdit)

        self.standard_of_living = yoink(statsEdit)

        self.happiness = 0

        self.land_lumber = yoink(statsEdit)

        self.land_ore = yoink(statsEdit)

        # self.land_uranium = yoink(stats)

        self.land_fertility = yoink(statsEdit)

        self.population = int(self.land_size / (self.standard_of_living / 5))
        # NOTE: add birth and death rates later
        self.education = yoink(statsEdit)

        self.nationalism = yoink(statsEdit)

        self.lumber = 0

        self.ore = 0

        # self.uranium = 0

        self.wealth = 10
        # note: come up with equation for income
        self.income = 0

        self.food = 0

        self.tech = [
            # also remember commas, dumbass
            # Name, in Progress?, time in development, duration (in time units), cost, is Complete

            # My dumbass forgot to add a "is complete", but all you gotta do is if [2] >= [3] return true
            # ignore that imma add it
            ["Mine", False, 0, 5, 1000, False],
            ["Lumber Mill", False, 0, 5, 1000, False],
            ["Agriculture", False, 0, 5, 1000, False],
            ["Animal Husbandry", False, 0, 5, 1000, False]
        ]

        self.infrastructure = [
            # Name, quantity (scale of 1-10), Quality?, Linked Tech (Put tech name) put "None" if no tech is
            # required), Cost per unit
            ["Mines", 0, 1, "Mine", 1000],
            ["Lumber Mills", 0, 1, "Lumber Mill", 1000],
            ["Farms", 1, 1, "Agriculture", 1000],
            ["Ranches", 1, 1, "Animal Husbandry", 1000]
        ]

        self.food_deficit = 0

        self.food_per_turn = 0

        self.starvation_time = 0

    # self.army_size = 0

    # self.combat_power = 0

    # self.unit_types = ["Infantry"]

    # self.infrastructure = randint(1,10)
    # self.tech = [
    #	("pottery", False)
    # ]
    # TODO NOTE TO SELF DELETE COUNTRIES WHEN THEIR OWNER LEAVES THE SERVER
    async def techTree(self, ctx):
        embedVar = discord.Embed(title=f"{self.name} Tech", description="Country technologies", color=0xe74c3c)
        print(self.tech)
        for techno in self.tech:
            if techno[1]:
                thng = ":green_square: "
                embedVar.add_field(name=thng + techno[0], value=f"{int(techno[2] / techno[3] * 100)}% completed",
                                   inline=False)
            elif techno[3] > techno[2] > 0:
                thng = ":yellow_square: "
                embedVar.add_field(name=thng + " " + techno[0], value=f"{int(techno[2] / techno[3] * 100)}% completed",
                                   inline=False)
            elif techno[2] == 0:
                thng = ":arrow_right: "
                embedVar.add_field(name=thng + techno[0], value="Unresearched", inline=False)
            elif techno[5]:
                thng = ":white_check_mark: "
                embedVar.add_field(name=thng + techno[0], value="Completed", inline=False)
            else:
                thng = ":exclamation: "
                embedVar.add_field(name=thng + techno[0], value="Look the code broke, I'm sorry my guy", inline=False)
        await ctx.send(embed=embedVar)

    async def getStats(self, ctx):
        embedVar = discord.Embed(title=f"{self.name} Stats", description="Country statistics", color=0xe74c3c)
        embedVar.add_field(name=str(self.land_size), value="Land Size", inline=True)
        embedVar.add_field(name=str(self.land_lumber), value="Land Lumber", inline=True)
        embedVar.add_field(name=str(self.land_ore), value="Land Ore", inline=True)
        # embedVar.add_field(name=str(self.land_uranium), value="Land Uranium", inline=True)
        embedVar.add_field(name=str(self.land_fertility), value="Soil Fertility", inline=True)
        embedVar.add_field(name=str(self.standard_of_living), value="Standard of Living", inline=True)
        embedVar.add_field(name=str(self.happiness), value="Happiness", inline=True)
        embedVar.add_field(name=str(self.nationalism), value="Nationalism", inline=True)
        embedVar.add_field(name=str(self.education), value="Education", inline=True)
        embedVar.add_field(name=str(self.wealth), value="Wealth", inline=True)
        embedVar.add_field(name=str(self.income), value="Income", inline=True)
        embedVar.add_field(name=str(self.population), value="Population", inline=True)
        embedVar.add_field(name=str(self.lumber), value="Lumber", inline=True)
        embedVar.add_field(name=str(self.ore), value="Ore", inline=True)
        # embedVar.add_field(name=str(self.uranium), value="Uranium", inline=True)
        embedVar.add_field(name=str(self.food), value="Food", inline=True)
        await ctx.send(embed=embedVar)

        embedVar = discord.Embed(title=f"{self.name} Infrastructure", description="Country infrastructure",
                                 color=0xe74c3c)
        i = 0
        for item in self.infrastructure:
            for itemm in self.tech:
                if itemm[0] == item[3] and itemm[5]:
                    i += 1
                    embedVar.add_field(name=item[0], value="Stats", inline=False)
                    embedVar.add_field(name=str(item[1]), value="Number of " + item[0], inline=True)
                    embedVar.add_field(name=str(item[2]), value="Quality of " + item[0], inline=True)
        if i != 0:
            await ctx.send(embed=embedVar)

        i = 0
        embedVar = discord.Embed(title=f"{self.name} Tech", description="Country Technology", color=0xe74c3c)
        for techno in self.tech:
            if techno[2] >= techno[3]:
                i += 1
                embedVar.add_field(name=techno[0], value="Researched", inline=False)
            elif techno[1]:
                i += 1
                embedVar.add_field(name=techno[0], value="In Progress", inline=False)

        if i != 0:
            await ctx.send(embed=embedVar)

    async def timeUnitC(self):
        # advance tech
        # TODO: do cost stuff here
        for item in self.tech:
            # if in progress
            if item[1]:
                # Progress research
                item[2] += 1
                # if research complete
                if item[2] >= item[3]:
                    # set in progress to false
                    item[1] = False
                    item[5] = True
                    print(item[0] + " completed!")

                    # Check if tech is a prerequisite for a building,
                    # !depreciated
                    """for itemm in self.infrastructure:
                        if itemm[3].lower() == item[0].lower():
                            itemm[4] = True"""

        await botChannel.send("-------------------------------")
        await botChannel.send("`Before`")
        await botChannel.send(f"```Population- {self.population}\n"
                              f"Standard of Living- {self.standard_of_living}\n"
                              f"Food- {self.food}\n"
                              f"Food Deficit- {self.food_deficit}\n"
                              f"Starvation Time- {self.starvation_time}\n"
                              f"Happiness- {self.happiness}\n```")

        # Generate resources
        # HARD CODED
        for item in self.infrastructure:
            if item[1] > 0:
                if item[0] == "Mines":
                    # Equation: Ore amount = Stat * Number of items * Quality
                    self.ore += int(((self.land_ore * item[1]) // 2) * item[2])

                if item[0] == "Lumber Mills":
                    # Equation: Lumber amount = Stat * Number of items * Quality
                    self.lumber += int(((self.land_lumber * item[1]) // 2) * item[2])

                if item[0] == "Farms":
                    # Equation: Food amount = Stat * Number of items * Quality
                    self.food += int(((self.land_fertility * item[1]) // 2) * item[2])

                if item[0] == "Ranches":
                    # Equation: Food amount = Constant * Number of items * Quality
                    self.food += int(((4 * item[1]) // 2) * item[2])

        # Food Subtraction
        self.food -= self.population * (self.standard_of_living // 2)

        if self.food < 0:

            self.food_deficit = 0 - self.food
            self.food = 0
            self.starvation_time += 1

            self.happiness -= (self.food_deficit * self.starvation_time) // 2

        else:
            self.starvation_time = 0
            self.food_deficit = 0

        if self.starvation_time >= 3:
            self.population -= self.food_deficit // 2
        else:
            self.population += (11 - self.standard_of_living)

        await botChannel.send("`After`")
        await botChannel.send(f"```Population- {self.population}\n"
                              f"Standard of Living- {self.standard_of_living}\n"
                              f"Food- {self.food}\n"
                              f"Food Deficit- {self.food_deficit}\n"
                              f"Starvation Time- {self.starvation_time}\n"
                              f"Happiness- {self.happiness}\n```")

        # Later, update to give a time buffer between deficit beginning and starvation
    # save_object(Countries, "src/pickle/Countries")

    # Leaving possibility for more than 1 tech in development


# Clear command
@client.command(aliases=["clr333"])
@commands.has_role(929940836475625513)
async def clear333(ctx):
    await clr(ctx, client)


# Create a new country
@client.command(aliases=["cc"])
async def createCountry(ctx):
    with open('src/pickle/Countries', 'rb') as ctry:
        Countries = pickle.load(ctry)
    await ctx.send(Countries)
    for country in Countries:
        if country.managerID == ctx.message.author.id:
            await ctx.send(
                f"Looks like you already own {country.name}! Please delete it before making a new country! (Delete "
                f"feature in progress)")
            return

    await ctx.send("Country Creation process initiated!")

    async def nameCountry():
        async with ctx.typing():
            await asyncio.sleep(.8)

        # PLEASE FOR THE LOVE OF GOD MAKE THE FIRST LETTER OF NAME CAPITALIZED

        await ctx.send("What will your country be named?")

        def check(m):
            return m.channel == ctx.message.channel and m.author == ctx.message.author

        nameI = await client.wait_for('message', check=check)
        if nameI == "quit" or nameI == "exit":
            return "quit"
        for countryy in Countries:
            if nameI.content == countryy.name:
                await ctx.send(
                    f"Looks like that country has already been taken by {countryy.manager.mention}! Try choosing a "
                    f"different name!")
        return nameI

    name = await nameCountry()
    if name == "quit":
        return
    countre = Country(ctx, name.content)
    Countries.append(countre)
    await ctx.send(Countries)
    save_object(Countries, "src/pickle/Countries")


# Get country stats
@client.command(aliases=["s"])
async def stats(ctx):
    target = None
    with open('src/pickle/Countries', 'rb') as ctry:
        Countries = pickle.load(ctry)
    for i in Countries:
        if ctx.message.author.id == i.managerID:
            target = i
            break
    print(target)
    if target is not None:
        await target.getStats(ctx)


# Get tech details
@client.command(aliases=["t", "tech"])
async def technology(ctx, *, arg=None):
    # src/Commands/countryIntel.py
    await getTech(ctx, arg)


# research techs
@client.command(aliases=["r"])
async def research(ctx, *, arg=None):
    await getResearch(ctx, arg)


# get actions
@client.command(aliases=["a"])
async def actions(ctx):
    await doActions(ctx, client)


# Message another country
@client.command(aliases=["m"])
async def message(ctx, args=None):
    await sendMessage(ctx, client, args)


# Begin a crisis
@client.command(aliases=["c"])
# only chair can use
@commands.has_role(929940836475625513)
async def crisis(ctx):
    await ctx.send("CRISIS!!")


# Opt in/out of crises
@client.command(aliases=["co"])
async def crisisOpt(ctx):
    embed = discord.Embed(
        title='Crisis Opt',
        description="Are you currently available to deal with a crisis?",
        color=0x00ff00)
    embed.add_field(name='React', value="f", inline=False)
    embed.add_field(name='Reported By', value="g", inline=False)
    await ctx.send(embed=embed)


# token = "your mother"
# save_object(token, "token.p")

if __name__ == "__main__":
    # Run
    token = pickle.load(open("src/pickle/token.p", "rb"))
    client.run(token)
