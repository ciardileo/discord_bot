# imports
from datetime import datetime
import discord
from discord.ext import commands
from rich.console import Console


# main class
class System(commands.Cog):
	def __init__(self, client):
		# instances
		self.console = Console()
		self.client = client

	# commands
	# ping command
	@commands.command()
	async def ping(self, ctx):
		await ctx.send(
			f'Pong!...espera, isso não é muito genérico? Ah deixa pra lá, seu ping é {round(self.client.latency * 1000)}ms')
		self.console.log(f'Usuário [green]{ctx.author}[/] quer saber a latência')

	# msg command
	@commands.command()
	async def msg(self, ctx, *, mensagem):
		await ctx.channel.purge(limit=1)
		await ctx.send(mensagem)
		self.console.log(
			f'Usuário [green]{ctx.author}[/] mandou a mensagem [green]"{mensagem}"[/] no canal [green]{ctx.channel}[/]')

	# msg command error
	@msg.error
	async def msg_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Você tem que escrever uma mensagem BURRO!')

	# direct message command
	@commands.command()
	async def dm(self, ctx, member: discord.Member, *, message):
		await ctx.channel.purge(limit=1)
		await member.send(message)
		self.console.log(
			f'Usuário [green]{ctx.author}[/] mandou DM para [green]{member}[/] com a mensagem [green]"{message}"[/]')

	# dm command error
	@dm.error
	async def dm_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Você tem marcar alguém e escrever uma mensagem BURRO!')

	# get profile photo command
	@commands.command()
	async def avatar(self, ctx, member: discord.Member = 0):
		if member == 0 or member.id == ctx.author.id:
			embed = discord.Embed(title=f'Seu avatar, {ctx.author.name}', colour=ctx.author.color,
								  description='Você é MUITO feio...')
			embed.set_image(url=ctx.author.avatar_url)
			embed.set_author(name=ctx.author.name + "#" + ctx.author.discriminator, icon_url=ctx.author.avatar_url)
			embed.set_footer(text=f'{ctx.author.name} pediu o própio avatar, quanto ego...')
			await ctx.send(embed=embed)
			self.console.log(f'Usuário [green]{ctx.author}[/] pediu avatar dele mesmo')
		else:
			embed = discord.Embed(title=f'Avatar de {member.name}', colour=member.color,
								  description='Você é MUITO feio...')
			embed.set_image(url=member.avatar_url)
			embed.set_author(name=member.name + "#" + member.discriminator, icon_url=member.avatar_url)
			embed.set_footer(text=f'Avatar pedido por {ctx.author.name}')
			await ctx.send(embed=embed)
			self.console.log(f'Usuário [green]{ctx.author}[/] pediu avatar de [green]{member}[/]')

	# avatar command error
	@avatar.error
	async def avatar_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(f'Você tem que mencionar um membro {ctx.author.mention}!')

	# # embed command
	# @commands.command()
	# async def embed(self, ctx):
	# 	pass

	# user info command
	@commands.command(aliases=['rg', 'hack'])
	async def userinfo(self, ctx, member: discord.Member = 0):
		if member == 0 or member.id == ctx.author.id:
			member = ctx.author
		joined_at = member.joined_at  # .split('-')
		created_at = member.created_at  # .split('-')

		# joined_at = f'{joined_at[2].split(" ")[0]}/{joined_at[1]}/{joined_at[0]}'
		# created_at = f'{created_at[2].split(" ")[0]}/{created_at[1]}/{created_at[0]}'

		# this code can be simplified:
		joined_at = joined_at.strftime('%d/%m/%Y')
		created_at = created_at.strftime('%d/%m/%Y')

		embed = discord.Embed(title=f'Stalkeando amigão??', description='Aqui as informações...')
		embed.set_author(name=f'{member.name}{member.discriminator}', icon_url=member.avatar_url)
		embed.add_field(name='Entrou no servidor em:', value=joined_at, inline=True)
		embed.add_field(name='Criou a conta em:', value=created_at, inline=True)
		embed.add_field(name='Maior cargo:', value=f'{member.top_role.mention}', inline=False)
		embed.add_field(name='ID', value=f'{member.id}', inline=True)
		embed.set_thumbnail(url=member.avatar_url)
		await ctx.send(embed=embed)
		self.console.log(f'Usuário [green]{ctx.author}[/] quer ver o rg de [green]{member}[/]')

	# server info command
	@commands.command(aliases=['sv', 'if', 'hacksv', 'server'])
	async def serverinfo(self, ctx):
		embed = discord.Embed(title='Informações do server', description='O melhor servidor do discord',
							  timestamp=datetime.utcnow())
		embed.set_thumbnail(url=ctx.guild.icon_url)

		status = [len(list(filter(lambda m: str(m.status) == 'online', ctx.guild.members))),
				  len(list(filter(lambda m: str(m.status) == 'idle', ctx.guild.members))),
				  len(list(filter(lambda m: str(m.status) == 'dnd', ctx.guild.members))),
				  len(list(filter(lambda m: str(m.status) == 'offline', ctx.guild.members)))]

		fields = [(f'Nome:', f'{ctx.guild.name}', False),
				  (f'Criado em:', f'{ctx.guild.created_at.strftime("%d/%m/%Y")}', True),
				  (f'Donos:', f'{ctx.guild.owner}', True),
				  (f'Membros:', f'{len(list(filter(lambda m: not m.bot, ctx.guild.members)))} membros', True),
				  # o filter retorna apenas os valores True da função lambda
				  (f'Bots:', f'{len(list(filter(lambda m: m.bot, ctx.guild.members)))} bots', True),
				  (f'Membros Banidos:', f'{len(await ctx.guild.bans())} membros banidos', True),
				  (f'Canais de Voz:', f'{len(ctx.guild.voice_channels)} canais de voz', True),
				  (f'Canais de Texto:', f'{len(ctx.guild.text_channels)} canais de texto', True),
				  (f'Status dos membros:', f'🟢   {status[0]}   🟡   {status[1]}   🔴   {status[2]}   ⚪   {status[3]}',
				   True),
				  (f'Cargos', f'{len(ctx.guild.roles)} cargos', True)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
		embed.set_footer(text='Fica flinstons aí')

		await ctx.send(embed=embed)
		self.console.log(
			f'Usuário [green]{ctx.author}[/] pediu para ver as informações do servidor [green]{ctx.guild.name}[/]')

	# polls command
	@commands.command(aliases=['enquete'])
	async def poll(self, ctx, *, options):
		# poll(titulo, "opção")
		parameters = options.split('"')
		title = parameters[1]
		answers = parameters[2]
		answers = answers.split(',')
		embed = discord.Embed(title=title)
		embed.set_footer(text=f'Enquete por {ctx.author}')
		emoji = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣']
		if len(answers) > 8:
			await ctx.send('O limite de opções é 8 mano!')
		else:
			counter = 1
			used = 0
			for answer in answers:
				used += 1
				embed.add_field(name=f'{emoji[counter - 1]} {answer.strip()}', value=f'Reaja com {counter}',
								inline=False)
				counter += 1
			message = await ctx.send(embed=embed)
			counter = 0
			for answer in answers:
				await message.add_reaction(emoji=f'{emoji[counter]}')
				counter += 1
			self.console.log(f'Usuário [green]{ctx.author}[/] fez uma enquete com {len(answers)} opções')


# laod the cog
def setup(client):
	client.add_cog(System(client))
