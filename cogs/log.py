# imports

from datetime import datetime
from discord.ext import commands
from discord import Embed
import random


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel = self.client.get_channel(813408123444264964)

    # on member update

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.display_name != after.display_name:
            embed = Embed(title='Membro mudou o perfil', description='Mudou Nickname', colour=after.colour,
                          timestamp=datetime.utcnow())

            fields = [('Antes', before.display_name, False), ('Depois', after.display_name, False)]

    # on message edit

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            pass

    # on message delete

    @commands.Cog.listener()
    async def on_message_delete(self, before, after):
        if not after.author.bot:
            pass


def setup(client):
    client.add_cog(Logs(client))
