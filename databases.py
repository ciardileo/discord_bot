import sqlite3 as sql

con = sql.connect('bot.db')
cursor = con.cursor()

reactions_table = 'create table if not exists reactions(' \
				  'message_id char(18) not null,' \
				  'reaction varchar(20),' \
				  'role_id char(18)' \
				  ');'

judge_table = 'create table if not exists judge(' \
			  'user_id char(18) not null,' \
			  'mute_time varchar(6),' \
			  'warns int(1)' \
			  ');'

server_config_table = 'create table if not exists sv_config(' \
					  'server_id varchar(18) not null,' \
					  'online_id varchar(18) default "0",' \
					  'welcome_id varchar(18) default "0",' \
					  'bye_id varchar(18) default "0",' \
					  'log_id varchar(18) default "0"' \
					  ');'

fight_ranking_table = 'create table if not exists fight_ranking(' \
					  'player_id char(18) not null,' \
					  'flyers int(3) default 0,' \
					  'escapes int(3) default 0,' \
					  'wins int(3) default 0,' \
					  'matches int(3) default 0' \
					  ');'


def execute(command):
	cursor.execute(command)
	con.commit()


def fetchall(command):
	cursor.execute(command)
	con.commit()
	return cursor.fetchall()


def execute_args(command, args):
	cursor.execute(command, args)
	con.commit()


def ranking_add(type, player_id):
	ranking = fetchall('select * from fight_ranking')
	is_register = False
	for player in ranking:
		if player[0] == str(player_id):
			execute(f'update fight_ranking set {str(type)} = {type} + 1 where player_id = {str(player_id)}')
			is_register = True
		else:
			pass

	if not is_register:
		execute(f'insert into fight_ranking (player_id, {type}) values ({str(player_id)}, 1)')


def get_sv_config(sv_id):
	configs = fetchall(f'select * from sv_config where server_id = {sv_id}')
	configs = configs[0]
	return configs
