import discord
import pickle
import asyncio
import nest_asyncio
# from random import randint
from random import choice
import re
from datetime import datetime

nest_asyncio.apply()
from discord.utils import get
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.messages = True
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
# Do stuff when a time unit passes
async def timeUnit():
	pass

pass
# when the bot is ready
# Used to run the time loop
@client.event
async def on_ready():
	print("Ready")
	
	
	botChannel = get(client.get_guild(929935033869951016).channels, name="bot-announcements")
	
	i = 0
	while True:
		tme = datetime.now()
		t = tme.strftime("%X")
		if i%5 == 0:
			print(t)
		#midnight is 07:00:00
		if t == "00:8:00":
			await botChannel.send("One time unit has passed!")
			await timeUnit()
		await asyncio.sleep(1)
		i+=1


pass
#Pickle function
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

# Help Command
@client.command(aliases=["h"])
async def help(ctx):
	#no help
	#await ctx.send("This message lacks assistance in any form!")
	embedVar = discord.Embed(title=f"Help", description="Command help", color= 0xe74c3c)
	embedVar.add_field(name="Create Country (.cc)", value="Creates a country", inline=False)
	embedVar.add_field(name="Statistics (.s)", value="Check your country statistics", inline=False)
	embedVar.add_field(name="Technology (.t)", value="Check your technological progression", inline=False)
	embedVar.add_field(name="Message (.m <country>)", value="Send a private message to anoter country", inline=False)
	await ctx.send(embed=embedVar)



pass
########CLASS INIT#########
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
		


pass

########CLASS INIT#########

# Country class declaration
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
			#Name, %of completion, cost
			["Mine", 0, 1000],
			["Lumber Mill", 0, 1000],
			["Agriculture", 0, 1000],
			["Animal Husbandry", 0, 1000]
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
			if techno[1] > 0 and techno[1] < 1:
				embedVar.add_field(name=techno[0], value="In Progress", inline=False)
			elif techno[1] == 0:
				embedVar.add_field(name=techno[0], value="Unresearched", inline=False)
			elif techno[1] == 1:
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





pass

# Clear command
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
					for channel in cat.channels:
						await channel.delete()
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
			
			
				

pass

# Create a new country
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




pass

# Get country stats
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



pass

# Get tech details
@client.command(aliases=["t", "tech"])
async def technology(ctx, *, arg=None):
	
	target = None
	with open('Countries', 'rb') as ctry:
		Countries = pickle.load(ctry)
	for i in Countries:
		if ctx.message.author.id == i.managerID:
			target = i
			break
			
	if arg == None:
		print(target)
		if target != None:
			await target.techTree(ctx)
	else:
		###ADD MORE TECHS HERE###
		
		if arg.lower() == "mine":
			
			embedVar = discord.Embed(title=f"Mine", description="Tech details", color= 0xe74c3c)
			embedVar.add_field(name="Allows the mining of ore", value="Effects", inline=False)
			embedVar.add_field(name="$" + str(target.tech[0][2] ), value="Tech cost (per time unit)", inline=False)
			await ctx.send(embed=embedVar)
			
		if arg.lower() == "lumber mill":
			
			embedVar = discord.Embed(title=f"Lumber Mill", description="Tech details", color= 0xe74c3c)
			embedVar.add_field(name="Allows the collection of lumber", value="Effects", inline=False)
			embedVar.add_field(name="$"+str(target.tech[1][2]), value="Tech cost (per time unit)", inline=False)
			await ctx.send(embed=embedVar)
			
			
		if arg.lower() == "agriculture":
			
			embedVar = discord.Embed(title=f"Agriculture", description="Tech details", color= 0xe74c3c)
			embedVar.add_field(name="Allows the harvesting of food", value="Effects", inline=False)
			embedVar.add_field(name="$"+str(target.tech[2][2]), value="Tech cost (per time unit)", inline=False)
			await ctx.send(embed=embedVar)
			
		if arg.lower() == "animal husbandry":
			
			embedVar = discord.Embed(title=f"Animal Husbandry", description="Tech details", color= 0xe74c3c)
			embedVar.add_field(name="Allows the domestication of animals for food", value="Effects", inline=False)
			embedVar.add_field(name="$"+str(target.tech[3][2]), value="Tech cost (per time unit)", inline=False)
			await ctx.send(embed=embedVar)
			
		###ADD MORE TECHS HERE###



pass

# research techs
@client.command(aliases=["r"])
async def research(ctx, *, arg=None):
	if arg == None:
		pass


	
pass

# get actions
@client.command(aliases=["a"])
async def actions(ctx, *, arg=None):
	if arg == None:
		pass

pass

# Message another country
@client.command(aliases=["m"])
async def message(ctx, args=None):
	
	with open('Countries', 'rb') as ctry:
		Countries = pickle.load(ctry)
		
	options = []
	for i in Countries:
		options.append(i.name)

	userC = None
	for i in Countries:
		if ctx.message.author.id == i.managerID:
			userC = i
			break
			
	if userC == None:
		await ctx.send("Please make a country before using this command.")
		return
	
	if args == None:
		await ctx.send("Please specify which country you want to contact. Your options are as follows: ", delete_after=3)
		await ctx.send(options, delete_after=10)
		def check(m):
			return m.channel == ctx.message.channel and m.author == ctx.message.author
		name = await client.wait_for('message', check=check)
		print(options)
		if name.content in options:
			target = name.content
		else:
			await ctx.send("Country not found, watch your caps", delete_after=3)
			return
		await name.delete()
	else:
		if args in options:
			target = args
		else:
			await ctx.send("Country not found, watch your caps", delete_after=3)
			return
		
	await ctx.send(f"Contacting {target}...", delete_after=3)
	
	for i, country in enumerate(Countries):
		if country.name == target:
			targetC = country

	if targetC == None:
		await ctx.send("404: Country not found", delete_after=3)
		return
	
	
	category = get(ctx.guild.categories, name= targetC.categoryName)
	
	targetRoleName = targetC.roleName
	targetChannelName = targetC.channelNames

	userRoleName = userC.roleName
	userChannelName = userC.channelNames

	comboChannelName = targetChannelName + "-" + userChannelName
	
	for channel in ctx.guild.channels:
		if channel.name == comboChannelName:
			exist = True
			break
		else:
			exist = False
	
	userRole = get(ctx.guild.roles, name=userRoleName)
	targetRole = get(ctx.guild.roles, name=targetRoleName)
	
	if exist == True:
		channel = get(ctx.guild.channels, name = comboChannelName)
	
		await channel.send(userRole.mention + " You have mail from " + targetRole.mention + "!")
	else:
		channel = await ctx.guild.create_text_channel(comboChannelName, category=category)
		await channel.set_permissions(targetRole, view_channel=True, send_messages=True)
		await channel.set_permissions(userRole, view_channel=True, send_messages=True)
		await channel.set_permissions(ctx.guild.default_role, view_channel=False)
	
	
	
		await channel.send("Channel configuration success! " + userRole.mention + ", " + targetRole.mention)
	
	await ctx.message.delete()
		
		
pass

# Begin a crisis
@client.command(aliases=["c"])
# only chair can use
@commands.has_role(929940836475625513)
async def crisis(ctx):
	await ctx.send("CRISIS!!")
	
	


pass

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

#token = "sugondese nutz"
#save_object(token, "token.p")

	
pass

#Run
token = pickle.load(open("token.p", "rb"))
client.run(token)
