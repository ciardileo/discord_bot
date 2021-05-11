# imports

from datetime import datetime
from discord import Embed
from discord.ext import commands


# main class
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
        if before.name != after.name:
            embed = Embed(title='Membro mudou o perfil', description='Mudou o nome', colour=after.colour,
                          timestamp=datetime.utcnow())
            embed.add_field(name='Antes', value=f'```{before.name}```', inline=False)
            embed.add_field(name='Depois', value=f'```{after.name}```', inline=False)
            await channel.send(embed=embed)

    # on member update
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = self.client.get_channel(823881567893585960)
        if before.display_name != after.display_name:

            embed = Embed(title=f'Membro mudou o perfil', description='Mudou apelido', colour=after.colour,
                          timestamp=datetime.utcnow())

            embed.set_author(name=f'{before.name}#{before.discriminator}', icon_url=before.avatar_url)
            embed.set_footer(text=f'ID do usuário: {before.id}')

            fields = [('Antes', f'```{before.display_name}```', False),
                      ('Depois', f'```{after.display_name}```', False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            print(channel)

            await channel.send(embed=embed)

        elif before.roles != after.roles:
            channel = self.client.get_channel(823881567893585960)
            embed = Embed(title=f'Membro mudou o perfil', description='Mudou de cargo', colour=after.colour,
                          timestamp=datetime.utcnow())

            embed.set_author(name=f'{before.name}#{before.discriminator}', icon_url=before.avatar_url)
            embed.set_footer(text=f'ID do usuário: {before.id}')

            fields = [('Antes', '\n'.join([role.mention for role in before.roles]), False),
                      ('Depois', '\n'.join([role.mention for role in after.roles]), False)]

            # list comprehension

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            print(channel)

            await channel.send(embed=embed)

    # on message edit
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            channel = self.client.get_channel(823881567893585960)
            if before.content != after.content:

                embed = Embed(title=f'{after.author.name} editou a mensagem',
                              description=f'Mensagem editada no canal: {after.channel.mention}',
                              colour=after.author.colour,
                              timestamp=datetime.utcnow())

                embed.set_author(name=f'{before.author.name}#{before.author.discriminator}',
                                 icon_url=before.author.avatar_url)
                embed.set_footer(text=f'ID do usuário: {before.author.id}')

                fields = [('Antes', f'```{before.content}```', False),
                          ('Depois', f'```{after.content}```', False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                print(channel)

                await channel.send(embed=embed)

    # on message delete
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            channel = self.client.get_channel(823881567893585960)
            embed = Embed(title=f'{message.author.name} deletou uma mensagem',
                          description=f'Mensagem deletada no canal: {message.channel.mention}',
                          colour=message.author.colour,
                          timestamp=datetime.utcnow())

            embed.set_author(name=f'{message.author.name}#{message.author.discriminator}',
                             icon_url=message.author.avatar_url)
            embed.set_footer(text=f'ID do usuário: {message.author.id}')

            embed.add_field(name='Mensagem', value=f'```{message.content}```', inline=False)

            print(channel)

            await channel.send(embed=embed)


# load the cog
def setup(client):
    client.add_cog(Logs(client))
