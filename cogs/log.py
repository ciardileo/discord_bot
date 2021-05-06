# imports

from datetime import datetime

import discord
from discord.ext import commands
from discord import Embed
import random


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    # on member update

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = self.client.get_channel(823881567893585960)
        if before.display_name != after.display_name:

            name = str(before).split('#')
            embed = Embed(title=f'{name[0]} mudou o perfil', description='Mudou apelido', colour=after.colour,
                          timestamp=datetime.utcnow())

            embed.set_author(name=before.name, icon_url=before.avatar_url)

            fields = [('Antes', f'`{before.display_name}`', False), ('Depois', f'`{after.display_name}`', False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            print(channel)

            await channel.send(embed=embed)

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
