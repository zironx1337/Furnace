import discord
from discord.ext import commands

#prefix
bot=commands.Bot(command_prefix='?')

#on_Ready
@bot.event
async def on_ready():
    print('Online')



#game_alert_commands


@bot.command()
async def l(ctx):
    if 'RUNNER' in [i.name for i in ctx.message.author.roles]:
        await ctx.send('-l')

    else:
        await ctx.send('Lol You have no perms')


@bot.command()
async def q(ctx):
    if 'RUNNER' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's Qureka Time!!**''')

    else:
        await ctx.send('Lol You have no perms')



#token
bot.run('ODI4MjkyMzk1NzM3MTUzNjE3.YGnd8w.bgGV432GJg5W14f3JFCYrCgyNbc',bot=False)
