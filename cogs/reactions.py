# imports
import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions, bot_has_permissions
import databases as db


# main class
class Reactions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.messages_id = list()

    # on reaction add
    @commands.command()
    async def react(self, ctx, message_id, reaction, role):
        # id - reaction, role - reaction, role - reaction, role...
        message = await ctx.channel.fetch_message(message_id)
        await message.add_reaction(emoji=f'{reaction}')
        print(reaction)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload)


# loads the cog
def setup(client):
    client.add_cog(Reactions(client))
