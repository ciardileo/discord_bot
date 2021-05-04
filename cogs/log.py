# imports

from datetime import datetime
from discord.ext import commands
from discord import Embed
import random


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel = self.client.get_channel(823881567893585960)

    # on member update

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.display_name != after.display_name:
            embed = Embed(title='Membro mudou o perfil', description='Mudou apelido', colour=after.colour,
                          timestamp=datetime.utcnow())

            fields = [('Antes', before.display_name, False), ('Depois', after.display_name, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.channel.send(embed=embed)
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
