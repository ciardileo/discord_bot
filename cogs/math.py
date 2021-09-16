# imports
from discord.ext import commands
from rich.console import Console


# main class
class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands
    # count command
    @commands.command(aliases=['count'])
    async def conta(self, ctx, number1, operator, number2):
        if operator == '+':
            try:
                await ctx.send(f'{number1} + {number2} = {round(float(number1) + float(number2))}')
                self.console.log(f'Usuário [green]{ctx.author}[/] quer saber quanto é {number1} + {number2}')
            except:
                await ctx.send('Você tem que colocar números!\nTenta de novo')
        if operator == '-':
            try:
                await ctx.send(f'{number1} - {number2} = {round(float(number1) - float(number2))}')
                self.console.log(f'Usuário [green]{ctx.author}[/] quer saber quanto é {number1} - {number2}')
            except:
                await ctx.send('Você tem que colocar números!\nTenta de novo')
        if operator == ':' or operator == '/':
            try:
                await ctx.send(f'{number1} : {number2} = {round(float(number1) / float(number2))}')
                self.console.log(f'Usuário [green]{ctx.author}[/] quer saber quanto é {number1} / {number2}')
            except:
                await ctx.send('Você tem que colocar números!\nTenta de novo')
        if operator == 'x' or operator == '.' or operator == '*':
            try:
                await ctx.send(f'{number1} x {number2} = {round(float(number1) * float(number2))}')
                self.console.log(f'Usuário [green]{ctx.author}[/] quer saber quanto é {number1} * {number2}')
            except:
                await ctx.send('Você tem que colocar números!\nTenta de novo')


# laod the cog
def setup(client):
    client.add_cog(Math(client))
