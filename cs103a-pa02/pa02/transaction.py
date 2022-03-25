'''
transaction.py will store financial transactions with the fields
'''

import sqlite3

#to_trans_dict -- Charlotte
def to_trans_dict(trans_tuple):
    ''' trans is a transaction tuple ( item_num, amount, category, date, description)'''
    tran = {'item_num':trans_tuple[0], 'amount':trans_tuple[1], 'category':trans_tuple[2],
    'date':trans_tuple[3],'description':trans_tuple[4]}
    return tran

#to_trans_dict_list -- Charlotte
def to_trans_dict_list(trans_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_trans_dict(tran) for tran in trans_tuples]

class Transaction:
    ''' connects with the sqlite database and create add, select, and delete methods --Bohan'''

    def __init__(self, dbfile):
        '''connect to the database and create the five fields:
        item_num, amount, category, date, description'''
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num text, amount int, category text, date int, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        '''return all the transactions in the database'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT * from transactions""")
        rows = cur.fetchall()
        con.close()
        return to_trans_dict_list(rows)

    def select_one(self, item_id):
        '''return one transaction in the database'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT * FROM transactions WHERE item_num = ?""", (item_id,))
        row = cur.fetchall()
        con.close()
        return to_trans_dict(row[0])

    def add(self, item):
        '''add a transaction to the database'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""INSERT INTO transactions VALUES(?,?,?,?,?)""",
                    (item['item_num'], item['amount'], item['category'],
                    item['date'], item['description']))
        con.commit()
        con.close()

    def delete(self, item_id):
        '''delete a transaction from the database'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""DELETE FROM transactions WHERE item_num = ?""", (item_id,))
        con.commit()
        con.close()
