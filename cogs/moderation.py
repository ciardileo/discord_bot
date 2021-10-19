# imports
import discord
from discord import member
from discord.ext import commands
from discord.ext.commands.core import has_permissions, bot_has_permissions
import random
from rich.console import Console
import databases as db


# main class
class Moderation(commands.Cog):
    def __init__(self, client):
        # instances
        self.client = client
        self.console = Console()

    # commands
    # kick members
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        self.console.log(f'[green]{member}[/] foi expulso por [green]{ctx.author}[/]')
        await member.kick(reason=reason)

    # kick command error
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Você não mencionou que membro quer expulsar')

    # ban members
    @has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        self.console.log(f'[green]{member}[/] foi banido por [green]{ctx.author}[/]')
        await member.ban(reason=reason)

    # ban command error
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Você não mencionou que membro quer banir')

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
                self.console.log(f'[green]{user.name}#{user.discriminator}[/] foi desbanido por [green]{ctx.author}[/]')
                return

    # unban command error
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Você não mencionou que membro quer desbanir')

    # give a role to a member
    @commands.command()
    @has_permissions(manage_roles=True)
    async def give_role(self, ctx, role, member: discord.Member):

        role = role[3:-1]
        role = ctx.guild.get_role(int(role))
        await member.add_roles(role, reason='Mudando os cargos')
        self.console.log(f'[green]{ctx.author}[/] deu o cargo [green]{role}[/] para [green]{member}[/]')

    # clear messages
    @commands.command(aliases=['cls', 'limpar'])
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        self.console.log(f'[green]{ctx.author}[/] apagou {amount} mensagens')

    # when someone join the server
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        configs = db.get_sv_config(str(member.guild.id))
        channel = self.client.get_channel(int(configs[2]))
        
        welcome = ['Chega mais', 'Eai', 'Salve', 'Opa']

        embed = discord.Embed(title='👋🏻 Bem Vindo(a)',
                              description=f'{random.choice(welcome)} {member.mention}, bem vindo(a) ao\n Super Gamers Opressores, leia as regras\n e vai se fuder 😜!')

        embed.set_author(name=f'{member.display_name}#{member.discriminator}', icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_image(
            url="https://media.discordapp.net/attachments/823546618862108707/825399357675143226/Ednaldo.gif")
        embed.set_footer(text=f'ID do usuário: {member.id}. Fica flintons aí')
        await channel.send(embed=embed)
        self.console.log(f'[green]{member}[/] entrou no servidor [green]{member.guild}[/]')

    # when someone left the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        configs = db.get_sv_config(str(member.guild.id))
        channel = self.client.get_channel(int(configs[3]))

        await channel.send(f'{member.mention} se juntou ao lado negro da força')

    # dm to all members
    @has_permissions()
    @commands.command()
    async def dm_all(self, ctx, *, message):
        count = 0
        for member in ctx.guild.members:
            try:
                await member.send(message)
                count += 1
            except:
                pass

        await ctx.send(f'Mensagem enviada para {count} membros 🤠')
        self.console.log(f'Usuário [green]{ctx.author}[/] mandou a mensagem "{message}" em DM para todos')

    # send a message in all channels
    @commands.command()
    async def msg_all(self, ctx, *, message):
        for channel in ctx.guild.channels:
            try:
                await channel.send(message)
            except:
                pass

        self.console.log(f'Usuário [green]{ctx.author}[/] mandou a mensagem "{message}" para todos os canais do servidor')

    # use with careful
    # @commands.command(aliases=['sim'])
    # async def nuke(self, ctx):

    #     await ctx.send('sim')
    
    #     for channel in ctx.guild.channels:
    #         try:
    #             await channel.delete(reason='Balane nao quis devolver a conta')
    #         except:
    #             print(f"I can't delete {channel}")
    
    #     for member in ctx.guild.members:
    #         try:
    #             await member.kick(reason='Sim')
    #         except:
    #             print(f"I can't kick {member}")


# load the cog
def setup(client):
    client.add_cog(Moderation(client))
