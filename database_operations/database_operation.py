from database_operations.connection import *


def add_bot(bot_id, mail, password, location, table='list', adress='database\\bot_list.db'):
    con = connector(adress)
    parameters = (bot_id, mail, password, location)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO {} VALUES(?,?,?,?)".format(table), parameters)


add_bot(1, 'dupa@o2.pl', 'koteg', '55:45')