# imports
import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import has_permissions, bot_has_permissions
import databases as db
from rich.console import Console


# main class
class Reactions(commands.Cog):
    def __init__(self, client):
        # instances
        self.client = client
        self.reactions = db.fetchall('select * from reactions')
        self.console = Console()

    # on reaction
    @has_permissions(manage_roles=True)
    @commands.command()
    async def react(self, ctx, message_id, reaction, role: discord.Role):
        if "discord.com" in message_id:
            message_id.split('/')
            message_id = message_id[-1]
        # id - reaction, role - reaction, role - reaction, role...
        message = await ctx.channel.fetch_message(message_id)
        await ctx.channel.purge(limit=1)
        counter = 1
        counter2 = 1
        for item in self.reactions:
            if str(message_id) == item[0]:
                if reaction == item[1]:
                    if role == item[2]:
                        await ctx.send('Você já adicionou essa reação', delete_after=3)
                        self.console.log(f'[green]{ctx.author}[/] tentou adicionar a mesma reação 2 vezes')
                        break
                    else:
                        db.execute_args('update reactions set role_id = ? where message_id = ? and reaction = ?',
                                        (role.id, message_id, reaction))
                        await ctx.send('Reação atualizada', delete_after=3)
                        if counter2 == 1:
                            self.console.log(
                                f'[green]{ctx.author}[/] atualizou a reação para a mensagem [green]"{message.content}"[/]')
                        counter2 += 1
                        break
            else:
                await message.add_reaction(emoji=f'{reaction}')
                db.execute_args('insert into reactions (message_id, reaction, role_id) values (?, ?, ?)',
                                (message_id, reaction, role.id))
                if counter == 1:
                    self.console.log(
                        f'[green]{ctx.author}[/] adicionou uma reação para a mensagem [green]"{message.content}"[/]')
                counter += 1

    @has_permissions(manage_roles=True)
    @commands.command()
    async def remove_react(self, ctx, message_id, reaction):
        db.execute_args('delete from reactions where message_id = ? and reaction = ?', (message_id, reaction))
        await ctx.channel.purge(limit=1)
        await ctx.send('Reação removida com sucesso', delete_after=3)
        self.console.log(f'[green]{ctx.author}[/] removeu uma reação de uma mensagem')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.bot:
            pass
        else:
            self.reactions = db.fetchall('select * from reactions')
            for item in self.reactions:
                if str(payload.message_id) in item[0]:
                    if payload.emoji.name == item[1]:
                        guild = self.client.get_guild(payload.guild_id)
                        role = guild.get_role(int(item[2]))
                        await payload.member.add_roles(role, reason='Raw Reaction')
                        self.console.log(
                            f'[green]{payload.member}[/] reagiu a uma mensagem e ganhou o cargo [green]{role}[/]')
                        break

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        self.reactions = db.fetchall('select * from reactions')
        for item in self.reactions:
            if str(payload.message_id) in item[0]:
                if payload.emoji.name == item[1]:
                    guild = self.client.get_guild(payload.guild_id)
                    member = guild.get_member(payload.user_id)

                    # verifying if is it a bot
                    if member.bot:
                        break

                    role = guild.get_role(int(item[2]))
                    await member.remove_roles(role, reason='Raw Reaction')
                    self.console.log(
                        f'[green]{member}[/] tirou a reação de uma mensagem e perdeu o cargo [green]{role}[/]')
                    break


# loads the cog
def setup(client):
    client.add_cog(Reactions(client))
