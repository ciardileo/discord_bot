# imports
import asyncio
import os
import random
import discord
from discord import File
from discord.ext import commands
from rich.console import Console
from rich.progress import track

# rename memes function
def rename_memes():
	memesdir = f'{os.environ["ONEDRIVE"].replace(os.sep, "/")}/Imagens/Saved Pictures/memes/videos'
	counter = 1
	sorted_memes = list()
	new_memes = list()

	for meme in os.listdir(memesdir):
		try:
			if len(meme) > 3:
				new_memes.append(meme[:-4])
			else:
				sorted_memes.append(int(meme[:-4]))
		except:
			new_memes.append(meme[:-4])

	sorted_memes = sorted(sorted_memes)

	for item in new_memes:
		sorted_memes.append(item)

	for meme in sorted_memes:
		try:
			os.rename(f'{memesdir}/{str(meme)}.mp4', f'{memesdir}/{str(counter)}.mp4')
		except:
			# print(f'Não consegui o meme {counter}')
			pass
		finally:
			counter += 1
	return memesdir


# main class
class Fun(commands.Cog):
	def __init__(self, client):
		# instances
		self.client = client
		self.console = Console()

		# fight status variables
		self.is_on_fight = False
		self.player1 = discord.Member
		self.player2 = discord.Member
		self.accepted = False
		self.player1_hp = 100
		self.player2_hp = 100
		self.round = discord.Member

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
		self.console.log(f'Usuário [green]{ctx.author}[/] quer testar a masculinidade')

	# kong command
	@commands.command(aliases=['king kong', 'king'])
	async def kong(self, ctx):
		await ctx.send(self.king)
		await ctx.send('Aqui é a tropa do KONG porra')
		self.console.log(f'Usuário [green]{ctx.author}[/] é do time KONG')

	# alien cesure command
	@commands.command(aliases=['censure', 'csr'])
	async def censura(self, ctx):
		for time in range(1, 4):
			await ctx.send('https://tenor.com/view/bailar-moves-alien-grooves-dance-gif-16520672')
		self.console.log(f'Usuário [green]{ctx.author}[/] pediu censura')

	# funny command
	@commands.command(aliases=['oqd'])
	async def oqdevofzr(self, ctx):
		await ctx.channel.purge(limit=1)
		await ctx.send("Amigo, você deve piscar o cu bem devagar 😋")
		self.console.log(f'Usuário [green]{ctx.author}[/] quer saber o que fazer')

	# funny command
	@commands.command()
	async def memata(self, ctx):
		if ctx.message.author.id == 756287979902730272:
			await ctx.send('Ah lucas vai se fuder, essa porra de omori coisa de gay do caralho')
		else:
			ways = ['Na corda ou vai no prédio?', 'OK 🔫 POOOW, é...está morto...', 'Tá com depressor amigo?',
			        'Hoje o mundo ficará melhor']
			await ctx.send(random.choice(ways))
		self.console.log(f'Usuário [green]{ctx.author}[/] quis se matar')

	# funny command
	@commands.command(aliases=['gemidao'])
	async def geme(self, ctx):
		await ctx.send(file=File('./cogs/fun/troll.mp3'))
		await ctx.send("😡 NÃO SOU SUA PUTA NÃO FDP")
		self.console.log(f'Usuário [green]{ctx.author}[/] pediu gemido')

	# 8ball command
	@commands.command(aliases=['8ball', 'pergunta'])
	async def advinhe(self, ctx, *, pergunta):
		answers = ['Sim', 'Não', 'Provavelmente', 'Acho que sim', 'Sei lá, porque perguntou pra mim?', 'COM CERTEZA', 'Óbvio que sim', 'Não quero falar, obrigado', 'TALVEZ...', 'Acho que não hein...', 'SIM KKKKKKKK', 'NÃO KKKKKKKK', 'Todo mundo sabe que isso é verdade...']
		await ctx.send(f'A RESPOSTA É.... {random.choice(answers)}')
		self.console.log(f'Usuário [green]{ctx.author}[/] quer saber minha resposta')

	# send a meme
	@commands.command()
	async def meme(self, ctx, num=None):
		path = rename_memes()
		if num is None:
			await ctx.send(f'Meme aleatório fresquinho saindo para {ctx.author.mention}...')
			await ctx.send(file=File(f'{path}/{random.choice(os.listdir(path))}'))
			self.console.log(f'Usuário [green]{ctx.author}[/] pediu meme')
		elif int(num) < 1:
			await ctx.send('Coloque números acima de zero amigão')
		elif int(num) > len(os.listdir(path)):
			await ctx.send(
				f'{ctx.author.mention}, eu só tenho {len(os.listdir(path))} memes no momento, continue mandando mais nos chats para ver esse número aumentar 🚀')
		else:
			await ctx.send(f'Shitpost {num} saindo...')
			await ctx.send(file=File(f'{path}/{num}.mp4'))
			self.console.log(f'Usuário [green]{ctx.author}[/] pediu meme {num}')

	# rpg fight system
	@commands.command(aliases=['luta', 'rinha', 'briga', 'treta', 'porrada'])
	async def fight(self, ctx, member: discord.Member):
		
		if self.is_on_fight:
			await ctx.send("Uma luta já foi iniciada, espere essa acabar para começar outra")
		else:
			self.is_on_fight = True
			self.player2 = member
			self.player1 = ctx.author

			await ctx.send(f'Diga "sim" para a aceitar a batalha {member.mention}')
			await asyncio.sleep(8)
			if self.accepted:
				await ctx.send(
					'Opções:\n`fugir` - sair da batalha\n`chute` - 20 a 40 de dano (70% de chance de acerto)\n`defesa` - +10 de hp\n`soco` - 10 de dano (100% de chance de acerto)\n`voadora` - HITKILL (8% de chance de acerto)')
				await ctx.send(f'{ctx.author.mention} começa')
				self.round = self.player1
				self.console.log(f'Usuário [green]{ctx.author}[/] pediu uma luta com [green]{member}[/]')
			else:
				await ctx.send("Você demorou demais para responder, saindo da batalha...")
				self.accepted = False
				self.is_on_fight = False
				self.player1 = discord.Member
				self.player2 = discord.Member
				self.console.log(f'Usuário [green]{ctx.author}[/] pediu uma luta com [green]{member}[/], mas ele não respondeu...')

	# fight verification
	@commands.Cog.listener()
	async def on_message(self, message):
		# # verify if isn't a bot
		# if not message.author.bot:

		# fight command
		if self.is_on_fight:

			# verify if accepted the fight
			if message.content.lower() == 'sim' and message.author.id == self.player2.id:
				self.accepted = True

			# verify the action
			if message.content.lower() == 'fugir' and message.author.id == self.round.id:
				if self.player1_hp < 1 or self.player2_hp < 1:
					await message.channel.send(f'FINISH HIM! {self.round.mention} VENCEU 🏆')
				else:
					await message.channel.send(f'A LUTA ACABOU, O OTÁRIO DO {message.author.mention} FUGIU')
				self.accepted = False
				self.is_on_fight = False
				self.player1 = discord.Member
				self.player2 = discord.Member
				self.player1_hp = 100
				self.player2_hp = 100
				self.round = discord.Member

			# verify the action
			if message.content.lower() == 'soco' and message.author.id == self.round.id:
				self.round = message.author
				if self.round.id == self.player2.id:
					self.player1_hp -= 10
					if self.player1_hp < 1:
						await message.channel.send(f'FINISH HIM! {self.round.mention} VENCEU 🏆')
						self.accepted = False
						self.is_on_fight = False
						self.player1 = discord.Member
						self.player2 = discord.Member
						self.player1_hp = 100
						self.player2_hp = 100
						self.round = discord.Member
					else:
						await message.channel.send(
							f'👊 {self.round.mention} deu um soco que causou 10 de dano em {self.player1.mention} deixando o com {self.player1_hp} de vida')
						self.round = self.player1
				else:
					self.player2_hp -= 10
					if self.player2_hp < 1:
						await message.channel.send(f'FINISH HIM! {self.round.mention} VENCEU 🏆')
						self.accepted = False
						self.is_on_fight = False
						self.player1 = discord.Member
						self.player2 = discord.Member
						self.player1_hp = 100
						self.player2_hp = 100
						self.round = discord.Member
					else:
						await message.channel.send(
							f'👊 {self.round.mention} deu um soco que causou 10 de dano em {self.player2.mention} deixando o com {self.player2_hp} de vida')
						self.round = self.player2

			# verify the action
			if message.content.lower() == 'defesa' and message.author.id == self.round.id:
				self.round = message.author
				if self.round.id == self.player2.id:
					self.player2_hp += 10
					await message.channel.send(
						f'💊 {self.round.mention} se curou e ficou com {self.player2_hp} de vida')
					self.round = self.player1
				else:
					self.player1_hp += 10
					await message.channel.send(
						f'💊 {self.round.mention} se curou e ficou com {self.player1_hp} de vida')
					self.round = self.player2

			# verify the action
			if message.content.lower() == 'chute' and message.author.id == self.round.id:
				damage = random.randint(20, 40)
				percentage = random.randint(1, 100)
				if percentage <= 70:
					if self.round.id == self.player2.id:
						self.round = message.author
						self.player1_hp -= damage
						if self.player1_hp < 1:
							await message.channel.send(f'FINISH HIM! {self.round.mention} VENCEU 🏆')
							self.accepted = False
							self.is_on_fight = False
							self.player1 = discord.Member
							self.player2 = discord.Member
							self.player1_hp = 100
							self.player2_hp = 100
							self.round = discord.Member
						else:
							await message.channel.send(
								f'🦶 {self.round.mention} chutou e causou {damage} de dano em {self.player1.mention} deixando o com {self.player1_hp} de vida')
							self.round = self.player1
					else:
						self.player2_hp -= damage
						if self.player2_hp < 1:
							await message.channel.send(f'FINISH HIM! {self.round.mention} VENCEU 🏆')
							self.accepted = False
							self.is_on_fight = False
							self.player1 = discord.Member
							self.player2 = discord.Member
							self.player1_hp = 100
							self.player2_hp = 100
							self.round = discord.Member
						else:
							await message.channel.send(
								f'🦶 {self.round.mention} chutou e causou {damage} de dano em {self.player2.mention} deixando o com {self.player2_hp} de vida')
							self.round = self.player2
				else:
					await message.channel.send(f'{message.author.mention} errou o chute')
					if self.round.id == self.player2.id:
						self.round = self.player1
					else:
						self.round = self.player2

			# verify the action
			if message.content.lower() == 'voadora' and message.author.id == self.round.id:
				if self.player1_hp < 1 or self.player2_hp < 1:

					await message.channel.send(f'☠️ FINISH HIM! {self.round.mention} VENCEU 🏆')
					self.accepted = False
					self.is_on_fight = False
					self.player1 = discord.Member
					self.player2 = discord.Member
					self.player1_hp = 100
					self.player2_hp = 100
					self.round = discord.Member
				else:
					percentage = random.randint(1, 100)
					if percentage <= 10:
						self.accepted = False
						self.is_on_fight = False
						self.player1_hp = 100
						self.player2_hp = 100
						if self.round.id == self.player2.id:
							self.round = message.author
							await message.channel.send(
								f'{self.round.mention} matou {self.player1.mention} com uma voadora\n VITÓRIA DE {self.round.mention} 🏆')
							self.round = discord.Member
							self.player1 = discord.Member
							self.player2 = discord.Member
						else:
							self.round = message.author
							await message.channel.send(
								f'{self.round.mention} matou {self.player2.mention} com uma voadora\n VITÓRIA DE {self.round.mention} 🏆')
							self.player1 = discord.Member
							self.player2 = discord.Member
					else:
						await message.channel.send(f'{message.author.mention} errou a voadora')
						if self.round.id == self.player2.id:
							self.round = self.player1
						else:
							self.round = self.player2


# load the cog
def setup(client):
	client.add_cog(Fun(client))
