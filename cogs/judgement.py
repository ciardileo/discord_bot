# imports

from discord.ext import commands


# main class
class Judgment(commands.Cog):
    def __init__(self, client):
        self.client = client


# loads the cog
def setup(client):
    client.add_cog(Judgment(client))
