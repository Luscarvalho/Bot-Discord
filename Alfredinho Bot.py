import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='$')
@client.event
async def on_ready():
    print('Bot Ligado')

@client.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command(aliases = ['Pergunta', 'teste'])
async def pergunta(ctx, *,perg):
    respostas = [
        'Sim.',
        'Não.',
        'Talvez.']
    await ctx.send(f'Pergunta: {perg}\nResposta: {random.choice(respostas)}')

@client.command(aliases=['Chance', 'Corno'])
async def corno(ctx):
    await ctx.send(f'Você tem chance de {random.randrange(100)}% de ser corno')

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} mensagens apagadas.')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason = reason)
    await ctx.send(f'{member} foi expulso do servidor.')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason = reason)
    await ctx.send(f'{member} foi banido do servidor.')

client.run('ODg5OTA0OTA2NDUzMDAwMjc0.YUoChw.CH2L49hjl51gdi6nf_gClDLa5HU')