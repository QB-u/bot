import discord
import random
from discord.ext.commands.bot import Bot
from discord.ext import commands

TOKEN = 'ODIyNDU2NzUxOTIzNTI3NzYw.YFSiig.6EZyJ_ASWzlDK2ukgHLxDpH2j6Y'

f = open('cat.txt')
listcat=f.readlines()

a = open('girl.txt')
listgirl=a.readlines()

b = open('sexy.txt')
listsexy=b.readlines()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.command()
async def cat(ctx):
    await ctx.send(random.choice(listcat))

@client.command()
async def girl(ctx):
    await ctx.send(random.choice(listgirl))

@client.command()
async def sexy(ctx):
    await ctx.send(random.choice(listsexy))

client.run(TOKEN)