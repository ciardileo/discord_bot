# imports

from discord.ext import commands


class System(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!...espera, isso não é muito genérico? Ah deixa pra lá, seu ping é {round(self.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(System(client))
