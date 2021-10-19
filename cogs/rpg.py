# imports
import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import has_permissions, bot_has_permissions
import databases as db
from rich.console import Console


# main class
class RPG(commands.Cog):
    def __init__(self, client):
        # instances
        self.client = client


# loads the cog
def setup(client):
    client.add_cog(RPG(client))
