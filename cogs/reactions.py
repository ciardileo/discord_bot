# imports
import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions, bot_has_permissions
import databases as db


# main class
class Reactions(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.reactions = db.fetchall('select * from reactions')

	# on reaction
	@has_permissions(manage_roles=True)
	@commands.command()
	async def react(self, ctx, message_id, reaction, role: discord.Role):
		# id - reaction, role - reaction, role - reaction, role...
		message = await ctx.channel.fetch_message(message_id)
		await ctx.channel.purge(limit=1)
		for item in self.reactions:
			if str(message_id) == item[0]:
				if reaction == item[1]:
					if role == item[2]:
						await ctx.send('Você já adicionou essa reação', delete_after=3)
					else:
						db.execute_args('update reactions set role_id = ? where message_id = ? and reaction = ?', (role.id, message_id, reaction))
						await ctx.send('Reação atualizada', delete_after=3)
			else:
				await message.add_reaction(emoji=f'{reaction}')
				db.execute_args('insert into reactions (message_id, reaction, role_id) values (?, ?, ?)', (message_id, reaction, role.id))

	@has_permissions(manage_roles=True)
	@commands.command()
	async def remove_react(self, ctx, message_id, reaction):
		db.execute_args('delete from reactions where message_id = ? and reaction = ?', (message_id, reaction))
		await ctx.send('Reação removida com sucesso', delete_after=3)

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		self.reactions = db.fetchall('select * from reactions')
		print(payload)
		for item in self.reactions:
			if str(payload.message_id) in item[0]:
				if payload.emoji.name == item[1]:
					print(payload.member.guild)
					guild = self.client.get_guild(payload.guild_id)
					print(guild)
					print(item[2])
					role = guild.get_role(int(item[2]))
					print(type(role))
					await payload.member.add_roles(role, reason='Raw Reaction')


# loads the cog
def setup(client):
	client.add_cog(Reactions(client))
