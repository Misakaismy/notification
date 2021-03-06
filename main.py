import discord
import os, signal
# import tempfile
from pathlib import Path
from subprocess import Popen
from discord.ext import commands

VERSION = "0.0.0"
TOKEN='ODIwOTY0MDU2MDA0OTUyMDk0.YE80Ww.crry4KSE1lv47NcBl1I3Kivtxec'
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.event
async def on_ready():
    print(r'Push coding in Name:{bot.user.name}, ID:{bot.user.id}')
    print('-----------------------')

@bot.event    
async def on_message(message):
    print('on_message get message from {0.author} : {0.content}'.format(message)) if message.author.id != bot.user.id else None
    ctx = await bot.get_context(message)
    if ctx.command != None:
        await bot.process_commands(message)

@bot.command(name = 'version',invoke_without_command = True)
async def command_get_version(ctx, *attr):
    await ctx.send(VERSION)

@bot.group(name = 'cogs', invoke_without_command = True)
async def cogs_group(ctx, *attr):
    description = 'cogs:\n'
    for file in os.listdir(r'./cogs'):
        if file.endswith('.py'):
            description += '  |- {}\n'.format(file[:-3])
    await ctx.send(description)

@cogs_group.command(name = 'load')
@commands.is_owner()
async def cogs_load(ctx, extention):
    bot.load_extension(f'cogs.{extention}')

@cogs_group.command(name = 'unload')
@commands.is_owner()
async def cogs_unload(ctx, extention):
    bot.unload_extension(f'cogs.{extention}')

@cogs_group.command(name = 'reload')
@commands.is_owner()
async def cogs_reload(ctx, extention):
    bot.unload_extension(f'cogs.{extention}')
    bot.load_extension(f'cogs.{extention}')
    ctx.send('reload cog {}'.format(extention))

#preload cogs
temp = 'load cogs:\n'
for file in os.listdir(r'./cogs'):
    if not file.startswith("__init__") and file.endswith('.py'):
        temp += '  |- {}\n'.format(file[:-3])
        bot.load_extension('cogs.{}'.format(file[:-3]))
print(temp)

bot.run(TOKEN)