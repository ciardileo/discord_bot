# imports

import os
from itertools import cycle

import discord
from discord.ext import commands, tasks

# bot config
# user discriminator = user code

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='>', intents=intents)


# events
# def to be executed when the bot starts

@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status=discord.Status.online, activity=discord.Game('Hello World! Ainda estou em progresso, confira com o ADM as funções que eu já tenho.'))
    print('Online')
    print(client.user.name)  # bot name
    print(client.user.id)  # id bot


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
    status = cycle(['Hello World! Ainda estou em progresso, confira com o ADM as funções que eu já tenho.',
                    'Python. Sim essa é minha linguagem, ainda estou em progresso, continue testando para logo mais eu ser o melhor bot de **TODOS**'])

    await client.change_presence(activity=discord.Game(next(status)))


# run the bot

client.run('ODEzNTAzNjY1NTgyNzY4MjAw.YDQQVA.ZHdSu7vT3puRogPm_rI2udbtlMw')  # bot token