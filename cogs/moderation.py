# imports

import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands
    # kick members

    @has_permissions(ban_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} foi expulso')

    # ban members

    @has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} foi **B-A-N-I-D-O**')

    # unban members

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_code = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_code):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} foi desbanido')
                return

    # clear messages

    @commands.command(aliases=['cls', 'limpar'])
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    # when someone join the server

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} se juntou ao time')

    # when someone left the server

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} se juntou ao lado negro da força')


def setup(client):
    client.add_cog(Moderation(client))
