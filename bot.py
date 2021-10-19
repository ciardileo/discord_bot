# imports
import os
from itertools import cycle
import discord
from discord import Embed
from discord.ext import commands, tasks
import databases as db
from rich.console import Console
from rich.progress import track

# console
console = Console()

# bot
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='>', intents=intents)

# status list
status = cycle(['Fica flinstons aí que eu to chegando', 'Eu não pareço um sarigue?',
				'Dá um ">help" pra ver o que o melhor bot do mundo tem a oferecer ',
				'Dizem que tem um bot me copiando por aí...cópias são cópias, não chegam perto do original...'])


# events
# def to be executed when the bot starts
@client.event
async def on_ready():
	change_status.start()

	console.log('[green]Bot Online[/]')
	console.print(f'{client.user.name}')  # bot name
	console.print(f'ID: {client.user.id}')  # id bot
	console.print(f'Estou atualmente em {len(client.guilds)} servidores')
	console.print("=" * 25)

	for guild in client.guilds:
		configs = db.get_sv_config(guild.id)

		if configs[2] != "0":
			channel = client.get_channel(int(configs[1]))
			embed = Embed(title='O Pai Ta On Família!', description='Super Bot Opressor está online.', colour=0xFF0000)
			fields = [('Meus comandos', 'Mano, dá um `>help` pra saber mais', True),
					  ('Se incomoda com essa mensagem?', '*FODASE*', True),
					  ('Eu sou o melhor bot do mundo, não?', 'Definitivamente não ;-; MAS AINDA VOU SER', True)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			embed.set_footer(text='Fica flinstons aí')
			embed.set_author(name='Super Bot Opressor',
							 icon_url=guild.icon_url)
			await channel.send(embed=embed)
		else:
			pass
			console.print(f'Servidor [green]{guild.name}[/] não quer receber mensagens de online')



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
