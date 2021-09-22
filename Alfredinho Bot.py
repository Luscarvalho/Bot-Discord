import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix='$')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODg5OTA0OTA2NDUzMDAwMjc0.YUoChw.KY7BtxdrY6UeqFDjHxVW-Aj_XA4')
