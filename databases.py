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
