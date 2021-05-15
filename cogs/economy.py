# imports

from discord.ext import commands


# main class
class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def give_m(self):
        pass


# loads the cog
def setup(client):
    client.add_cog(Economy(client))
