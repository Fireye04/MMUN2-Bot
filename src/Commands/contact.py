import pickle

from discord.utils import get


async def sendMessage(ctx, client, args):
    with open('src/pickle/Countries', 'rb') as ctry:
        Countries = pickle.load(ctry)

    options = []
    for i in Countries:
        options.append(i.name)

    userC = None
    for i in Countries:
        if ctx.message.author.id == i.managerID:
            userC = i
            break

    if userC is None:
        await ctx.send("Please make a country before using this command.")
        return

    if args is None:
        await ctx.send("Please specify which country you want to contact. Your options are as follows: ",
                       delete_after=3)
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

    targetC = None

    for i, country in enumerate(Countries):
        if country.name == target:
            targetC = country

    if targetC is None:
        await ctx.send("404: Country not found", delete_after=3)
        return

    category = get(ctx.guild.categories, name=targetC.categoryName)

    targetRoleName = targetC.roleName
    targetChannelName = targetC.channelNames

    userRoleName = userC.roleName
    userChannelName = userC.channelNames

    comboChannelName = targetChannelName + "-" + userChannelName

    exist = False

    for channel in ctx.guild.channels:
        if channel.name == comboChannelName:
            exist = True
            break
        else:
            exist = False

    userRole = get(ctx.guild.roles, name=userRoleName)
    targetRole = get(ctx.guild.roles, name=targetRoleName)

    if exist is True:
        channel = get(ctx.guild.channels, name=comboChannelName)

        await channel.send(userRole.mention + " You have mail from " + targetRole.mention + "!")
    else:
        channel = await ctx.guild.create_text_channel(comboChannelName, category=category)
        await channel.set_permissions(targetRole, view_channel=True, send_messages=True)
        await channel.set_permissions(userRole, view_channel=True, send_messages=True)
        await channel.set_permissions(ctx.guild.default_role, view_channel=False)

        await channel.send("Channel configuration success! " + userRole.mention + ", " + targetRole.mention)

    await ctx.message.delete()
