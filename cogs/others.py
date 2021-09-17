# imports
import random
from rich.console import Console
from discord import Embed
from discord.ext import commands


# main class
class Others(commands.Cog):
    def __init__(self, client):
        # instances
        self.client = client
        self.console = Console()

    # commands
    # say hi
    @commands.command(aliases=['eae', 'eaí', 'salve', 'opa', 'eai', 'olá', 'ola'])
    async def oi(self, ctx):
        greetings = ['Eaí', 'Eae', 'Oi', 'Olá', 'Salve', 'Opa,', 'Fala aí']
        await ctx.send(f'{random.choice(greetings)} {ctx.author.mention} 👋🏻')
        self.console.log(f'Usuário [green]{ctx.author}[/] pediu um "oi"')

    # discloses our social media
    @commands.command(aliases=['div', 'divulgação'])
    async def divulgar(self, ctx):
        guild = self.client.get_guild(823546618347257877)
        embed = Embed(title='Nossas Redes Sociais:',
                      description='Nos siga lá pra dar uma moral e ainda ganhar <:opressor:824271851089297448>',
                      colour=0x7ED957)
        embed.add_field(name='Canal Principal',
                        value='[Link](https://www.youtube.com/channel/UCorA07IsPZvdB5G3sTvpFtw?sub_confirmation=1)',
                        inline=False)
        embed.add_field(name='Canal De Games',
                        value='[Link](https://www.youtube.com/channel/UCVkGZxHQdW8S9_kCrYZj9rA?sub_confirmation=1)',
                        inline=False)
        embed.add_field(name='Nosso Instagram', value='[Link](https://www.instagram.com/super_memes_opressores/)',
                        inline=False)
        embed.set_footer(text='Curte e Compartilha Tudo Irmão')
        embed.set_author(name='Super Memes Opressores', icon_url=ctx.author.guild.icon_url)
        await ctx.send(embed=embed)
        
        self.console.log(f'Usuário [green]{ctx.author}[/] divulgou nossas redes sociais')


# load the cog
def setup(client):
    client.add_cog(Others(client))
