import discord
import pickle
import asyncio
import nest_asyncio
from random import randint
from random import choice
import re

nest_asyncio.apply()
from discord.utils import get
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents = intents)
client.remove_command('help')

"""
NOTES!
- Add religion
- Add governments


BRAINSTORM
- 1 unit of time
	- 24 hours

"""



@client.event
async def on_ready():
	print("Ready")


def save_object(obj, filename):
	with open(filename, 'wb') as outp:  # Overwrites any existing file.
		pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

Countries = []
#save_object(Countries, "Countries")
# Countries = pickle.load("Countries")

#@client.event
#async def on_message(message):
#any on message shit goes here. (non commands, just actions to take on message)
#pass

#await client.process_commands(message)


async def aClassInitCategory(ctx, name, self):
	cat = await ctx.message.guild.create_category(name)
	await cat.create_text_channel(self.channelNames + "-general")
	return


async def aClassInitRoleCreate(ctx, name):
	await ctx.guild.create_role(name=name)
	return


async def aClassInitRoleAdd(ctx, name, self):
	manager = get(ctx.message.guild.members, id = self.managerID)
	await manager.add_roles(get(ctx.message.guild.roles, name= self.roleName))
	return


async def aClassInitChairChannel(ctx, name, chair, self):
	await chair.create_text_channel(self.chairChannelName)
	return
	


async def aClassInitChairPerms(ctx, name, self):
	cc = get(ctx.guild.channels, name=self.chairChannelName)
	print(self.chairChannelName)
	await cc.set_permissions(ctx.message.guild.default_role, view_channel=False)
	await cc.set_permissions(get(ctx.message.guild.roles, name= self.roleName), view_channel=True)
	return
		


class Country():
	#on country creation, add government later
	# Note to self, check for duplicates, or previously owned countries
	def __init__(self, ctx, name):
		#Equal to categoryName and roleName
		self.name = name
		self.managerID = ctx.message.author.id
		#create country category
		self.channelNames = re.sub('[^A-Za-z0-9 ]+', '', self.name.lower()).replace(" ", "-")
		
		self.categoryName = name
		asyncio.run(aClassInitCategory(ctx, name, self))
		
		#Make a country role
		
		self.roleName = name
		asyncio.run(aClassInitRoleCreate(ctx, name))
		asyncio.run(aClassInitRoleAdd(ctx, name, self))
		
		#make a private chair DM
		
		chair = get(ctx.message.guild.categories, name='chair')
		
		self.chairChannelName = self.channelNames + "-chair"
		asyncio.run(aClassInitChairChannel(ctx, name, chair, self))
		
		asyncio.run(aClassInitChairPerms(ctx, name, self))
		
		#randomly assign base stats
		#Population
		#-Education
		#-Nationalism
		#Natural Resources
		#Wealth
		#-Income
		#Army
		#-Size
		#-Combat power
		#-Unit types
		#-Tactics
		#Infrastructure
		#-Standard of living
		#Tech
		#Awunga bunga


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
		#8
		stats = [1, 2, 4, 5, 5, 5, 8, 10]

		def yoink(stat):
			global stats
			e = choice(stat)
			stats = stat.remove(e)
			return e

		self.land_size = yoink(stats)

		self.standard_of_living = yoink(stats)

		self.land_lumber = yoink(stats)

		self.land_ore = yoink(stats)

		self.land_uranium = yoink(stats)

		self.land_fertility = yoink(stats)

		self.population = (1000000 * self.land_size) / (self.standard_of_living/2)
		#NOTE: add birth and death rates later
		self.education = yoink(stats)

		self.nationalism = yoink(stats)

		self.lumber = 0

		self.ore = 0

		self.uranium = 0

		self.wealth = 10
		#note: come up with equation for income
		self.income = 0

		self.food = 0

		self.tech = [
			#also remember commas, dumbass
			#Name, Is complete?, %of completion
			("Mine", False, 0),
			("Lumber Mill", False, 0),
			("Agriculture", False, 0),
			("Animal Husbandry", False, 0)
		]
			
		#self.army_size = 0

		#self.combat_power = 0

		#self.unit_types = ["Infantry"]

		#self.infrastructure = randint(1,10)
		#self.tech = [
		#	("pottery", False)
		#]
		# NOTE TO SELF DELETE COUNTRIES WHEN THEIR OWNER LEAVES THE SERVER
	async def techTree(self, ctx):
		embedVar = discord.Embed(title=f"{self.name} Tech", description="Country technologies", color= 0xe74c3c)
		for i, techno in enumerate(self.tech):
			if techno[2] > 0 and techno[2] < 1:
				embedVar.add_field(name=techno[0], value="In Progress", inline=False)
			elif techno[2] == 0:
				embedVar.add_field(name=techno[0], value="Unresearched", inline=False)
			elif techno[2] == 1:
				embedVar.add_field(name=techno[0], value="Completed", inline=False)
		await ctx.send(embed=embedVar)
		
	async def getStats(self, ctx):
		embedVar = discord.Embed(title=f"{self.name} Stats", description="Country statistics", color= 0xe74c3c)
		embedVar.add_field(name=str(self.land_size), value="Land Size", inline=True)
		embedVar.add_field(name=str(self.land_lumber), value="Land Lumber", inline=True)
		embedVar.add_field(name=str(self.land_ore), value="Land Ore", inline=True)
		embedVar.add_field(name=str(self.land_uranium), value="Land Uranium", inline=True)
		embedVar.add_field(name=str(self.land_fertility), value="Soil Fertility", inline=True)
		embedVar.add_field(name=str(self.standard_of_living), value="Standard of Living", inline=True)
		embedVar.add_field(name=str(self.nationalism), value="Nationalism", inline=True)
		embedVar.add_field(name=str(self.education), value="Education", inline=True)
		embedVar.add_field(name=str(self.wealth), value="Wealth", inline=True)
		embedVar.add_field(name=str(self.income), value="Income", inline=True)
		embedVar.add_field(name=str(self.population), value="Population", inline=True)
		embedVar.add_field(name=str(self.lumber), value="Lumber", inline=True)
		embedVar.add_field(name=str(self.ore), value="Ore", inline=True)
		embedVar.add_field(name=str(self.uranium), value="Uranium", inline=True)
		embedVar.add_field(name=str(self.food), value="Food", inline=True)
		await ctx.send(embed=embedVar)


@client.command(aliases=["clr333"])
@commands.has_role(929940836475625513)
async def clear333(ctx):
	embedVar = discord.Embed(title="Clear", description="Clear Menu", color= 0xe74c3c)
	embedVar.add_field(name="1- Countries", value="Clear the countries list", inline=False)
	embedVar.add_field(name="2- Chair Channels", value="Clear all the chair channels", inline=False)
	embedVar.add_field(name="3- Categories", value="Clear all the categories", inline=False)
	embedVar.add_field(name="4- Roles", value="Clear all the roles", inline=False)
	embedVar.add_field(name="5- A country", value="Clear a specific country", inline=False)
	embedVar.add_field(name="6- Empty channels", value="Clear random channels", inline=False)
	await ctx.send(embed=embedVar)
	def check(m):
		return m.channel == ctx.message.channel and m.author == ctx.message.author
	clrOption = await client.wait_for('message', check=check)
	clrOption = clrOption.content
	
	if clrOption == "1":
		with open('Countries', 'rb') as ctry:
			Countries = pickle.load(ctry)
		Countries = []
		save_object(Countries, "Countries")
		await ctx.send("Cleared!")
	elif clrOption == "2":
		chair = get(ctx.message.guild.categories, name='chair')
		if len(chair.channels) >= 1:
			for chan in chair.channels:
				await chan.delete()
			await ctx.send("Complete!")
		else:
			await ctx.send("Error: No channels found")
	elif clrOption == "3":
		whitelist = ["mmun", "text channels", "chair"]
		death = ctx.guild.categories
		await ctx.send(f"Whitelist: {whitelist}\n\nPLEASE CONFIRM OR EDIT CODE. CAPS MATTER.")
		def check(m):
			return m.channel == ctx.message.channel and m.author == ctx.message.author
		confirm = await client.wait_for('message', check=check)
		await confirm.delete()
		confirm = confirm.content
		
		if confirm == "wednesday":
			for cat in death:
				if cat.name in whitelist:
					print(f"saved {cat.name}")
				else:
					for channel in cat.channels:
						await channel.delete()
					await cat.delete()
					print(f"killed {cat.name}")
					
			await ctx.send("Complete!")
		else:
			await ctx.send("Cancelled.")
	elif clrOption == "4":
		whitelist = ["Chair", "Programmer", "Tester", "Bot", "MMUN Bot"]
		death = ctx.guild.roles
		await ctx.send(f"Whitelist: {whitelist}\n\nPLEASE CONFIRM OR EDIT CODE. CAPS MATTER.")
		def check(m):
			return m.channel == ctx.message.channel and m.author == ctx.message.author
		confirm = await client.wait_for('message', check=check)
		await confirm.delete()
		confirm = confirm.content
		
		if confirm == "thursday":
			for rle in death:
				if rle.name in whitelist or rle.name == "@everyone":
					print(f"saved {rle.name}")
				else:
					await rle.delete()
					print(f"killed {rle.name}")
					
			await ctx.send("Complete!")
		else:
			await ctx.send("Cancelled.")
	elif clrOption == "5":
		ctrys = []
		with open('Countries', 'rb') as ctry:
			Countries = pickle.load(ctry)
		for i in Countries:
			ctrys.append(i.name)
			
		await ctx.send(f"Select a country: \n{ctrys}")
		
		def check(m):
			return m.channel == ctx.message.channel and m.author == ctx.message.author
		confirm = await client.wait_for('message', check=check)
		confirmC = confirm.content
		if confirmC in ctrys:
			await ctx.send(f"Delete {confirmC}? (y/n)")
			confi = await client.wait_for('message', check=check)
			confi = confi.content
			for i in Countries:
				if i.name == confirmC:
					target = i
			if confi == "y":
				Countries.remove(target)
				save_object(Countries, "Countries")
				
				chair = get(ctx.message.guild.categories, name='chair')
				for i in chair.channels:
					if i.name == target.chairChannelName:
						await i.delete()

				cat = get(ctx.guild.categories, name=target.categoryName)
				if cat != None:
					await cat.delete()
				else:
					pass
					# await ctx.send(f"Cancelled.")

				rle = get(ctx.guild.roles, name=target.roleName)
				if rle != None:
					await rle.delete()
				else:
					pass
					# await ctx.send(f"Cancelled.")
				await ctx.send("Complete!")
				return
			else:
				await ctx.send(f"Cancelled.")
				return
		else:
			await ctx.send(f"{confirmC} not found. Please try again.")
			return
	elif clrOption == "6":
		whitelist = ["mmun", "text channels", "chair"]
		chnls = []
		for i in ctx.guild.channels:
			if i.name not in whitelist:
				name = i.category
				if name == None:
					name = "None"
					chnls.append(i)
				else:
					name = name.name
				print(i.name + "- " + name)
		if len(chnls) == 0:
			return
		else:
			for i in chnls:
				await ctx.send(i.name)
			await ctx.send("Do you want to delete the above channels? (y/n)")
			def check(m):
				return m.channel == ctx.message.channel and m.author == ctx.message.author
			confi = await client.wait_for('message', check=check)
			if confi.content == "y":
				for i in chnls:
					await i.delete()
				await ctx.send("Complete")
			
			
				
				
		
@client.command(aliases=["cc"])
async def createCountry(ctx):
	with open('Countries', 'rb') as ctry:
		Countries = pickle.load(ctry)
	await ctx.send(Countries)
	for country in Countries:
		if country.managerID == ctx.message.author.id:
			await ctx.send(f"Looks like you already own {country.name}! Please delete it before making a new country! (Delete feature in progress)")
			return
			break
		
	await ctx.send("Country Creation process initiated!")
	
	async def nameCountry():
		async with ctx.typing():
			await asyncio.sleep(.8)
			
		# PLEASE FOR THE LOVE OF GOD MAKE THE FIRST LETTER OF NAME CAPITALIZED
			
		await ctx.send("What will your country be named?")
		
		def check(m):
			return m.channel == ctx.message.channel and m.author == ctx.message.author
		name = await client.wait_for('message', check=check)
		if name == "quit" or name == "exit":
			return "quit"
		for country in Countries:
			if name.content == country.name:
				await ctx.send(f"Looks like that country has already been taken by {country.manager.mention}! Try chosing a different name!")
		return name
		
	name = await nameCountry()
	if name == "quit":
		return
	countre = Country(ctx, name.content)
	Countries.append(countre)
	await ctx.send(Countries)
	save_object(Countries, "Countries")

@client.command(aliases=["s"])
async def stats(ctx):
	target = None
	with open('Countries', 'rb') as ctry:
		Countries = pickle.load(ctry)
	for i in Countries:
		if ctx.message.author.id == i.managerID:
			target = i
			break
	print(target)
	if target != None:
		await target.getStats(ctx)

@client.command(aliases=["t", "tech"])
async def technologies(ctx):
	target = None
	with open('Countries', 'rb') as ctry:
		Countries = pickle.load(ctry)
	for i in Countries:
		if ctx.message.author.id == i.managerID:
			target = i
			break
	print(target)
	if target != None:
		await target.techTree(ctx)

@client.command(aliases=["h"])
async def help(ctx):
	#no help
	await ctx.send("This message lacks assistance in any form!")

	
"""
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
targetID = 3
print("from- "+ author.name + "\nto- " + target)


# ONLY ONE ROLE PER PERSON PLS
for i, role in enumerate(countryRoles):
if role in author.roles:
	aRole = role




if target in germany and aRole.name != "Germany":

target = "Germany"
targetID = 930978865654927421

elif target in germany and aRole.name == "Germany":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

elif target in us and aRole.name != "US":

target = "US"
targetID = 930978983800098837

elif target in us and aRole.name == "US":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

elif target in france and aRole.name != "France":

target = "France"
targetID = 933471681530462299

elif target in france and aRole.name == "France":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

elif target in russia and aRole.name != "Russia":

target = "Russia"
targetID = 933471787776368640

elif target in russia and aRole.name == "Russia":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

elif target in ottoman and aRole.name != "Ottoman":

target = "Ottoman"
targetID = 933471880806014986

elif target in ottoman and aRole.name == "Ottoman":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

elif target in japan and aRole.name != "Japan":

target= "Japan"
targetID = 933471997059551272

elif target in japan and aRole.name == "Japan":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

elif target in china and aRole.name != "China":

target = "China"
targetID = 930978937440460851

elif target in china and aRole.name == "China":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

elif target in italy and aRole.name != "Italy":

target = "Italy"
targetID = 930979017610367066

elif target in italy and aRole.name == "Italy":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

elif target in ireland and aRole.name != "Ireland":

target = "Ireland"
targetID = 930978900803215410

elif target in ireland and aRole.name == "Ireland":

await ctx.send("Stop trying to talk to yourself. If you have no friends, just say so.", delete_after=5)
await ctx.message.delete()

else:
await ctx.send("Could not find country. Please try again", delete_after=5)
await ctx.message.delete()

# await ctx.send("It worked!")

if targetID != 3:
await ctx.send("Configuring chat with " + target + "...", delete_after=3)

category = get(ctx.guild.categories, name= target.upper())

aRoleName = aRole.name.lower()
targetL = target.lower() + "-"

for channel in ctx.guild.channels:
	if channel.name == targetL + aRoleName:
		exist = True
		break
	else:
		exist = False

uRole = get(ctx.guild.roles, id= targetID)

if exist == True:
	channel = get(ctx.guild.channels, name = targetL + aRoleName)

	await channel.send(uRole.mention + " You have mail from " + aRole.mention + "!")
else:
	channel = await ctx.guild.create_text_channel(targetL + aRole.name, category=category)
	await channel.set_permissions(aRole, view_channel=True)



	await channel.send("Channel configuration success! " + uRole.mention + ", " + aRole.mention)

await ctx.message.delete()
"""
		
		
@client.command(aliases=["c"])
# only chair can use
@commands.has_role(929940836475625513)
async def crisis(ctx):
	await ctx.send("CRISIS!!")
	
	
@client.command(aliases=["co"])
# only chair can use
async def crisisOpt(ctx):
	embed = discord.Embed(
	title='Crisis Opt',
	description="Are you currently available to deal with a crisis?",
	color=0x00ff00)
	embed.add_field(name='React', value="f", inline=False)
	embed.add_field(name='Reported By', value="g", inline=False)
	await ctx.send(embed=embed)

#token = "sugondese nutz"
#save_object(token, "token.p")
token = pickle.load(open("token.p", "rb"))
client.run(token)
