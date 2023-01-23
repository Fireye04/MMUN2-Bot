import pickle

import discord
from discord.utils import get


# Pickle function
def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


async def clr(ctx, client):
    embedVar = discord.Embed(title="Clear", description="Clear Menu", color=0xe74c3c)
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
        with open('src/pickle/Countries', 'rb') as ctry:
            Countries = pickle.load(ctry)
        Countries = []
        save_object(Countries, "src/pickle/Countries")
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
        with open('src/pickle/Countries', 'rb') as ctry:
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
                save_object(Countries, "src/pickle/Countries")

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
