from database_operations.connection import *


def add_bot(bot_id='', mail='', password='', location='', table='list', adress='../database/bot_list.db'):
    con = connector(adress)
    parameters = (int(bot_id), mail, password, location)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO {} VALUES(?,?,?,?)".format(table), parameters)


def select_bot(id, table='list', adress='../database/bot_list.db'):
    con = connector(adress)
    with con:
        cur = con.cursor()
        mail = cur.execute("SELECT mail FROM {} WHERE id = \"{}\"".format(table, id)).fetchall()[0][0]
        password = cur.execute("SELECT password FROM {} WHERE id = \"{}\"".format(table, id)).fetchall()[0][0]
    return [mail, password]


