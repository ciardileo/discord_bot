# imports

from discord.ext import commands
import random


class Others(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands

    # say hi
    @commands.command(aliases=['eae', 'eaí', 'salve', 'opa', 'eai', 'olá', 'ola'])
    async def oi(self, ctx):
        greetings = ['Eaí', 'Eae', 'Oi', 'Olá', 'Salve', 'Opa,', 'Fala aí']
        await ctx.send(f'{random.choice(greetings)} {ctx.author.mention} 👋🏻')




def setup(client):
    client.add_cog(Others(client))
