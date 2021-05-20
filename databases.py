import sqlite3 as sql

con = sql.connect('bot.db')
cursor = con.cursor()

reactions_table = 'create table if not exists reactions(' \
                  'message_id char(18) not null,' \
                  'reaction varchar(20),' \
                  'role_id char(18)' \
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
