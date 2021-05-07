# imports
import discord
from discord.ext import commands
import bot


class System(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands
    # ping command

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(
            f'Pong!...espera, isso não é muito genérico? Ah deixa pra lá, seu ping é {round(self.client.latency * 1000)}ms')
        print(f'Usuário {ctx.author} quer saber a latência')

    # msg command

    @commands.command()
    async def msg(self, ctx, *, mensagem):
        await ctx.channel.purge(limit=1)
        await ctx.send(mensagem)
        print(f'Usuário {ctx.author} mandou a mensagem "{mensagem}"')

    @msg.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Você tem que escrever uma mensagem BURRO!')

    # direct message command

    @commands.command()
    async def dm(self, ctx, member: discord.Member, *, message):
        await member.send(message)
        print(f'Usuário {ctx.author} mandou DM para {member}')

    @dm.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Você tem marcar alguém e escrever uma mensagem BURRO!')

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        await ctx.send(f'{member.avatar_url}')
        print(f'Usuário {ctx.author} pediu avatar de {member}')

    # embed command

    @commands.command()
    async def embed(self, ctx):
        pass

    # user info command

    @commands.command(aliases=['rg'])
    async def userinfo(self, ctx, member: discord.Member):
        joined_at = str(member.joined_at).split('-')
        created_at = str(member.created_at).split('-')

        joined_at = f'{joined_at[2].split(" ")[0]}/{joined_at[1]}/{joined_at[0]}'
        created_at = f'{created_at[2].split(" ")[0]}/{created_at[1]}/{created_at[0]}'

        embed = discord.Embed(title=f'Stalkeando amigão??', description='Aqui as informações...')
        embed.set_author(name=f'{member.name}{member.discriminator}', icon_url=member.avatar_url)
        embed.add_field(name='Entrou no servidor em:', value=joined_at, inline=True)
        embed.add_field(name='Criou a conta em:', value=created_at, inline=True)
        embed.add_field(name='Maior cargo:', value=f'@{member.top_role}', inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

    # server info command

    @commands.command()
    async def serverinfo(self, ctx):
        pass


def setup(client):
    client.add_cog(System(client))
