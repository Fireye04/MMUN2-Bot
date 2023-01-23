from Commands.functions import *


async def getTech(ctx, arg):
    target = None
    with open('src/pickle/Countries', 'rb') as ctry:
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
            embedVar = discord.Embed(title=f"Mine", description="Tech details", color=0xe74c3c)
            embedVar.add_field(name="Allows the mining of ore", value="Effects", inline=False)
            embedVar.add_field(name="$" + str(target.tech[0][4]), value="Tech cost (per time unit)", inline=False)
            await ctx.send(embed=embedVar)

        if arg.lower() == "lumber mill":
            embedVar = discord.Embed(title=f"Lumber Mill", description="Tech details", color=0xe74c3c)
            embedVar.add_field(name="Allows the collection of lumber", value="Effects", inline=False)
            embedVar.add_field(name="$" + str(target.tech[1][4]), value="Tech cost (per time unit)", inline=False)
            await ctx.send(embed=embedVar)

        if arg.lower() == "agriculture":
            embedVar = discord.Embed(title=f"Agriculture", description="Tech details", color=0xe74c3c)
            embedVar.add_field(name="Allows the harvesting of food", value="Effects", inline=False)
            embedVar.add_field(name="$" + str(target.tech[2][4]), value="Tech cost (per time unit)", inline=False)
            await ctx.send(embed=embedVar)

        if arg.lower() == "animal husbandry":
            embedVar = discord.Embed(title=f"Animal Husbandry", description="Tech details", color=0xe74c3c)
            embedVar.add_field(name="Allows the domestication of animals for food", value="Effects", inline=False)
            embedVar.add_field(name="$" + str(target.tech[3][4]), value="Tech cost (per time unit)", inline=False)
            await ctx.send(embed=embedVar)

    ###ADD MORE TECHS HERE###


async def getResearch(ctx, arg):
    target = None
    with open('src/pickle/Countries', 'rb') as ctry:
        Countries = pickle.load(ctry)
    for i in Countries:
        if ctx.message.author.id == i.managerID:
            target = i
            break

    if arg is None:
        await ctx.send("Please specify a tech")
        await ctx.send("Use `.tech` to check your options")
        return

    tech = None
    prev = None
    for i in target.tech:
        if i[1] == True:
            prev = i
            await ctx.send(f"Switching research from {i[0]} to {arg}!")

    for i in target.tech:
        if i[0].lower() == arg.lower():
            if i[1] == False and i[2] <= i[3]:
                await ctx.send(f"Researching {i[0]}!")
                tech = i
                break
            elif i[1] == True:
                await ctx.send(f"Research on {i[0]} is already in progress!")
                return
            elif i[2] >= i[3]:
                await ctx.send(f"Research on {i[0]} Has already been completed!")
                return
            else:
                await ctx.send(
                    f"a̵̲̲̪̘̹̜̔̍͂á̵̢̛͇̹͙̭̩̰̯̱̰̘̘͓̬͛̐̂̓̑̆͒͘͘͜a̵̢̛̯̘͚̞̦̱͕̞̻̓̀͆̈́̈́͑̎͛͘̚͝ă̶̳̰͋̄͋͋̿̔̒̇͘̚̚͠͠a̷̖̭̪̬͉͇̗̗̘͉͔̝͒̽͐͋͗ͅa̵̘͙̯̥̻͒͜ͅâ̷̗̥̘̱̯̤̬̪̓̄͊͋ͅa̴̬̲̓̅̔̑̉͜a̶͎̹̼̜͉̥̞͔͍͖̯̫͐̂̀̂̚̚͜ͅā̶̛̛͚͍̫̹̯̟̗̻̩́̓̎͒͜ͅą̸͇̩͇͎͑͠a̷̧̛͈̘̦à̵̛̰̝̭̀̎́́͒̔̀̔ã̴̠͚͐̒͆̀̒̀̒͗̏̿̿͠͝a̶̱̳̯͍̜̫̣̿̾̿͊̏̒̈́̚͝a̵̦̜̘͍̰̘̹̗͋̓̓͂̄͌á̸̧̼̥͚̻̞͈̮͖̲̈̍́̆͗͘ȃ̸̢̹̩̺̙͚ą̷̜̻͊̅͋̒͜ặ̶͇̘̯̀ǎ̵̝͍̱̖̳̻̯̀̃̑́̃͗̕͠͝a̵͕̱̩͇̼̻̜̦͇̥͊̾͊̇̏͘ͅà̴̤͓̫̳͎̭̾̊̚a̸̡̝̙̹̬̠̅̓̈́͌͛̓̀͐͘ͅa̷̜͕̖̪̹̺̝̲̹̟͈͎̾̀̚a̴̧̡̨̞͇͚̗̗̬̦͔͓̦̺͋̑̾͜ä̷̢̛̪̗̜̮̝͇͕̞́̏̆͠͠ͅ")
                return

    if tech == None:
        await ctx.send(f"{arg} not found")
        return

    if prev != None:
        prev[1] = False

    tech[1] = True
    save_object(Countries, "src/pickle/Countries")


async def doActions(ctx, client):
    with open('src/pickle/Countries', 'rb') as ctry:
        Countries = pickle.load(ctry)
    target = None
    for i in Countries:
        if ctx.message.author.id == i.managerID:
            target = i
            break
    if target is None:
        return

    embedVar = discord.Embed(title=f"{target.name} Actions", description="Country Actions", color=0xe74c3c)
    embedVar.add_field(name="1) Build Infrastructure", value="Construct or improve crucial infrastructure",
                       inline=False)
    embedVar.add_field(name="2) Budget Allocation", value="INCOMPLETE", inline=False)
    await ctx.send(embed=embedVar)

    await ctx.send("Please provide the corresponding number for the option you wish to select")

    def check(m):
        return m.channel == ctx.message.channel and m.author == ctx.message.author

    aChoice = await client.wait_for('message', check=check)
    print(aChoice.content)
    if aChoice.content == "1":
        embedVar = discord.Embed(title=f"{target.name} Infrastructure", description="Country Infrastructure",
                                 color=0xe74c3c)
        fields = 0
        for i, item in enumerate(target.infrastructure):
            # TODO: add tech descriptors to list and implement here

            for itemm in target.tech:

                if item[3] == itemm[0] and itemm[5]:
                    fields += 1
                    embedVar.add_field(name=f"{i + 1}) Build {item[0]}", value=f"cost = {item[4]}", inline=False)
        if fields == 0:
            await ctx.send("No infrastructure found. Try researching some tech.")
            return

        await ctx.send(embed=embedVar)

        await ctx.send("Please provide the corresponding number for the option you wish to select")

        def check(m):
            return m.channel == ctx.message.channel and m.author == ctx.message.author

        iChoice = await client.wait_for('message', check=check)

        for i, item in enumerate(target.infrastructure):
            if str(i + 1) == iChoice.content:
                # cost stuff that I have yet to implement
                await ctx.send("How many do you wish to purchase? Max is 10, Min is 1. Type 'quit' to quit.")

                def check(m):
                    return m.channel == ctx.message.channel and m.author == ctx.message.author

                numChoice = await client.wait_for('message', check=check)
                numChoice = numChoice.content
                if numChoice == "quit":
                    await ctx.send("Quit Process.")
                    return
                try:
                    numChoice = int(numChoice)
                except TypeError:
                    await ctx.send("Ur dumb. Give me a number, knucklehead.")
                    return

                if numChoice > 10:
                    numChoice = 10
                elif numChoice == 0:
                    await ctx.send("Quit Process.")
                    return
                elif numChoice < 1:
                    numChoice = 1

                if item[1] + numChoice > 10:
                    numChoice = 10 - item[1]

                item[1] += numChoice
                save_object(Countries, "src/pickle/Countries")

                await ctx.send(f"{numChoice} {item[0]} purchased!")

                if numChoice == 1:
                    await ctx.send(f"Plurals are a pain in the ass to code, fuck you.")
