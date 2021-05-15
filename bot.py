# imports

import os
from itertools import cycle
import discord
# from discord import Embed
from discord.ext import commands, tasks
import databases as db

# bot config
# user discriminator = user code}

# atributes

# bot
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='>', intents=intents)

# status list
status = cycle(['Hello World! Ainda estou em progresso, confira com o ADM as funções que eu já tenho.',
                'Python. Sim essa é minha linguagem, ainda estou em progresso, continue testando para logo mais eu '
                'ser o melhor bot de TODOS',
                'Fica flinstons aí que eu to chegando', 'Eu não pareço um sarigue?',
                'Não sou escravo de vocês, mas trabalho de grassa'])


# events
# def to be executed when the bot starts

@client.event
async def on_ready():
    change_status.start()
    # revive_chat.start()

    print('Online')
    print(client.user.name)  # bot name
    print(client.user.id)  # id bot

    guild = client.get_guild(823546618347257877)
    print()

    # embed = Embed(title='O Pai Ta On Família!', description='Super Bot Opressor está online.', colour=0xFF0000)
    # fields = [('Meus comandos', 'Mano, dá um `>help` pra saber mais', True),
    #           ('Se incomoda com essa mensagem?', '*FODASE*', True),
    #           ('Eu sou o melhor bot do mundo, não?', 'Definitivamente não ;-; MAS AINDA VOU SER', True)]
    # for name, value, inline in fields:
    #     embed.add_field(name=name, value=value, inline=inline)
    # embed.set_footer(text='Fica flinstons aí')
    # embed.set_author(name='Super Bot Opressor',
    #                  icon_url=guild.icon_url)
    # await channel.send(embed=embed)


# commands

# load a cog
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


# unload a cog
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


# load all cogs when the bot starts
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# background task that will be executed every 10 seconds

# change status
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# run the bot
client.run('ODEzNTAzNjY1NTgyNzY4MjAw.YDQQVA.ZHdSu7vT3puRogPm_rI2udbtlMw')  # bot token
