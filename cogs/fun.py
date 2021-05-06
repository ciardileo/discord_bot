# imports

import random
import os
from discord import File
from discord.ext import commands


# cogs are like modules of a bot, that helps with the code organization

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

        # king kong ascii

        self.king = '''
          ════════════════════███████
         ═══════════════════█████████
         ══════════════════███████████
         ═════════════════███░░███░░███
         ════════════════███░░░░█░░░░░██
         ════════════█████░░░███████░░░████
         ═══════════█░░░████░█░█░█░█░███░░░█
         ═══════════█░░░███░░███░███░░██░░░█
         ═════════███░░░███░░░░░░░░░░░██░░░███
         ═════════█████░░░░░░░░███░░░░░░░█████
         ═══════██████░░░░░░░░░░░░░░░░░░░░██████
         ══════███████░░░░█████████████░░░███████
         ═══██████████░░░█░░░░░░░░░░░░░█░░████████
         ══██████████████░░░░░░░░░░░░░░░██████████
         ═███████████████░░░░░░░░░░░░░░░███████████
         ═█████████████████░░░░░░░░░░░░█████████████
         ═██████████████████░░░░░░░░░░██████████████
         ═██████████████████████████████████████████
         ═██████████████░░░██████████░░░████████████
         ══█████████████░░░░░░████░░░░░░████████████
         ═══█████████████░█░░░░██░░░░█░████████████
         ════█████████████░░░░░██░░░░░████████████
         ══════██████████░█░░░░██░░░░█░██████████
         ════════████████░█░░░░░░░░░░█░████████
         ═══════████████░░░░░░█░░█░░░░░░████████
         ═══════██████████████░░░░██████████████
         ══════███████████░░░░░░░░░░░░███████████
         ════█████████████░░░░█░█░░░░░████████████
         ═══███████████████░░█░█░█░░░██████████████
         ═══███████████████████████████████████████
         ═══███████████████████████████████████████
         ═══████████████████════════███████████████
         ════█████████████════════════████████████
         ════████████████══════════════███████████
         ═████░░███░░░██═══════════════██░░░███░░████
         █░░░░░█░░░░██░█═══════════════█░██░░░░█░░░░░█
         ██████████████═════════════════██████████████
          '''

    # commands
    # funny command

    @commands.command(aliases=['eusougay?'])
    async def eusougay(self, ctx):
        answers = ['Sim você é...', 'Sim, mas menos que o ricardo, porque não tem como ser mais...',
                   'Macho Alfa detectado',
                   'É amigo, você dá o cu', 'Não quero responder, boa noite', 'Você nao dá o cu', 'HOMOFOBICO!!!!',
                   'GAYYYYYYYY', 'VOCÊ NÃO É GAY, PARABÉNS']
        await ctx.send(random.choice(answers))

    # kong command

    @commands.command(aliases=['king kong', 'king'])
    async def kong(self, ctx):
        await ctx.send(self.king)
        await ctx.send('Aqui é a tropa do KONG porra')

    # alien cesure command

    @commands.command(aliases=['censure', 'csr'])
    async def censura(self, ctx):
        for time in range(1, 4):
            await ctx.send('https://tenor.com/view/bailar-moves-alien-grooves-dance-gif-16520672')

    @commands.command(aliases=['oqd'])
    async def oqdevofzr(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("Amigo, você deve piscar o cu bem devagar 😋")

    # .bat troll command

    @commands.command()
    async def maisfps(self, ctx):
        await ctx.send('Quer mais fps no seu MYNESCRAFTS amigo? Eu tenho a solução, é só baixar isso aí')
        await ctx.send(file=File('./cogs/fun/maisfps.bat'))

    @commands.command()
    async def memata(self, ctx):
        if ctx.message.author.id == 756287979902730272:
            await ctx.send('Ah lucas vai se fuder, essa porra de omori coisa de gay do caralho')
        else:
            ways = ['Na corda ou vai no prédio?', 'OK 🔫 POOOW, é...está morto...', 'Tá com depressor amigo?',
                    'Hoje o mundo ficará melhor']
            await ctx.send(random.choice(ways))

    @commands.command(aliases=['gemidao'])
    async def geme(self, ctx):
        await ctx.send(file=File('./cogs/fun/troll.mp3'))
        await ctx.send("😡 NÃO SOU SUA PUTA NÃO FDP")

    # send a random meme

    @commands.command()
    async def meme(self, ctx):
        await ctx.send('Shitpost saindo...')
        memes = random.choice(os.listdir('C:/Users/Léo Ciardi/OneDrive/Imagens/Saved Pictures/memes/videos'))
        await ctx.send(file=File(f'C:/Users/Léo Ciardi/OneDrive/Imagens/Saved Pictures/memes/videos/{memes}'))
        print('Meme requested')

    # send a morning video

    @commands.command(aliases=['bom_dia'])
    async def bomdia(self, ctx):
        await ctx.send('Bom dia puto')
        await ctx.send(file=File("C:/Users/Léo Ciardi/OneDrive/Imagens/Saved Pictures/memes/videos/Bom_dia_1_1-1-1-3-1.mp4"))


def setup(client):
    client.add_cog(Fun(client))
