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
        channel = self.client.get_channel(823881567893585960)
        if before.avatar_url != after.avatar_url:
            embed = Embed(title='Membro mudou perfil', description='Mudou foto de perfil (a de baixo é a nova)',
                          colour=after.colour, timestamp=datetime.utcnow())
            embed.set_image(url=after.avatar_url)
            embed.set_thumbnail(url=before.avatar_url)
            embed.set_author(name=after.name, icon_url=after.avatar_url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = self.client.get_channel(823881567893585960)
        if before.display_name != after.display_name:

            embed = Embed(title=f'Membro mudou o perfil', description='Mudou apelido', colour=after.colour,
                          timestamp=datetime.utcnow())

            embed.set_author(name=f'{before.name}{before.discriminator}', icon_url=before.avatar_url)
            embed.set_footer(text=f'ID do usuário: {before.id}')

            fields = [('Antes', f'```{before.display_name}```', False),
                      ('Depois', f'```{after.display_name}```', False)]

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
