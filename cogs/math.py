# imports

from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands

    # take a "*" on parameters means that the next parameter has multiple arguments as one
    # count command

    @commands.command(aliases=['count'])
    async def conta(self, ctx, number1, operator, number2):
        if operator == '+':
            try:
                await ctx.send(f'{number1} + {number2} = {round(float(number1) + float(number2))}')
            except:
                await ctx.send('Você tem que colocar números!\nTenta de novo')
        if operator == '-':
            try:
                await ctx.send(f'{number1} - {number2} = {round(float(number1) - float(number2))}')
            except:
                await ctx.send('Você tem que colocar números!\nTenta de novo')
        if operator == ':' or operator == '/':
            try:
                await ctx.send(f'{number1} : {number2} = {round(float(number1) / float(number2))}')
            except:
                await ctx.send('Você tem que colocar números!\nTenta de novo')
        if operator == 'x' or operator == '.' or operator == '*':
            try:
                await ctx.send(f'{number1} x {number2} = {round(float(number1) * float(number2))}')
            except:
                await ctx.send('Você tem que colocar números!\nTenta de novo')


def setup(client):
    client.add_cog(Math(client))
