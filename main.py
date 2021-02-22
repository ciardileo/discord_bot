import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Online')
    print(client.user.name) # bot name
    print(client.user.id) # id bot

@client.event
async def on_message(message):
    if message.content.lower().startswith('>test'):
        channel = message.channel
        await channel.send('Olá mundo')
    if message.content.lower().startswith('>coin'):
        choice = random.randint(1, 2)



client.run('ODEzNTAzNjY1NTgyNzY4MjAw.YDQQVA.ZHdSu7vT3puRogPm_rI2udbtlMw') # bot token