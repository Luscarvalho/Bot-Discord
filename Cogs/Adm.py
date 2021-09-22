import discord
import random
from discord.ext import commands

class Adm(commands.Cog):
    def __init__(self, client):
        self.client = client

    #eventos
    @commands.Cog.listener()
    async def on_ready(self):
        print('Alfredinho Bot está on.')

    #comandos
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'{amount} mensagens apagadas.')

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason = reason)
        await ctx.send(f'{member.mention} foi expulso do servidor.')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você não tem permissões para usar esse comando.")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason = reason)
        await ctx.send(f'{member.mention} foi banido do servidor.')
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você não tem permissões para usar esse comando.")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} desbanido')
                return
    
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você não tem permissões para usar esse comando.")
    
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Silenciado")
        if not mutedRole:
            mutedRole = await guild.create_role(name="Mutado")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title="MUTADO", description=f"{member.mention} É UM OTARIO E FOI MUTADO", colour=discord.Colour.light_gray())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" VOCÊ FOI MUTADO PELO: {guild.name} RAZÃO: {reason}")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você não tem permissões para usar esse comando.")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Silenciado")
        await member.remove_roles(mutedRole)
        embed = discord.Embed(title="Desmutado", description=f"{member.mention} você foi desmutado.", colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("você não tem permissões para usar esse comando.")

def setup(client):
    client.add_cog(Adm(client))
