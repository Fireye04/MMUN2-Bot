import discord
import pickle
import asyncio
import nest_asyncio

nest_asyncio.apply()
from discord.utils import get
from discord.ext import commands

client = commands.Bot(command_prefix=".")
client.remove_command('help')


@client.event
async def on_ready():
	print("Ready")


def save_object(obj, filename):
	with open(filename, 'wb') as outp:  # Overwrites any existing file.
		pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

Countries = []
save_object(Countries, "Countries")
# Countries = pickle.load("Countries")

#@client.event
#async def on_message(message):
#any on message shit goes here. (non commands, just actions to take on message)
#pass

#await client.process_commands(message)


async def aClassInitCategory(ctx, name):
	return await ctx.message.guild.create_category(name)


async def aClassInitRoleCreate(ctx, name):
	return await ctx.guild.create_role(name=name)


async def aClassInitRoleAdd(ctx, name, self):
	await ctx.message.author.add_roles(self.role)
	return


async def aClassInitChairChannel(ctx, name, chair):
	return await chair.create_text_channel(name + "-chair")


async def aClassInitChairPerms(ctx, name, self):
	await self.chairChannel.set_permissions(ctx.message.guild.default_role, view_channel=False)
	await self.chairChannel.set_permissions(self.role, view_channel=True)
	return
		
		
class Country():
	#on country creation, add government later
	# Note to self, check for duplicates, or previously owned countries
	def __init__(self, ctx, name):
	
		self.name = name
		self.manager = ctx.message.author
		#create country category
		
		
		
		self.category = asyncio.run(aClassInitCategory(ctx, name))
		
		#Make a country role
		
		self.role = asyncio.run(aClassInitRoleCreate(ctx, name))
		asyncio.run(aClassInitRoleAdd(ctx, name, self))
		
		#make a private chair DM
		
		chair = get(ctx.message.guild.categories, name='Chair')
		
		self.chairChannel = asyncio.run(aClassInitChairChannel(ctx, name, chair))
		
		asyncio.run(aClassInitChairPerms(ctx, name, self))
		
		#randomly assign base stats
		
		#Awunga bunga
			
			
			# NOTE TO SELF DELETE COUNTRIES WHEN THEIR OWNER LEAVES THE SERVER
		
		
@client.command(aliases=["cc"])
async def createCountry(ctx):
	with open('Countries', 'rb') as ctry:
		Countries = pickle.load(ctry)
		
	for country in Countries:
		if country.manager == ctx.message.author:
			await ctx.send(f"Looks like you already own {country.name}! Please delete it before making a new country! (Delete feature in progress)")
			#return
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
	await save_object(Countries, "Countries")
		
		
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
	
	
token = pickle.load(open("token.p", "rb"))
client.run(token)
