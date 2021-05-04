# imports

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

    # msg command

    @commands.command()
    async def msg(self, ctx, *, mensagem):
        await ctx.channel.purge(limit=1)
        await ctx.send(mensagem)

    # embed command

    @commands.command()
    async def embed(self, ctx):
        pass

    # user info command

    @commands.command()
    async def userinfo(self, ctx):
        pass

    # server info command

    @commands.command()
    async def serverinfo(self, ctx):
        pass


def setup(client):
    client.add_cog(System(client))
