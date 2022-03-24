'''
transaction.py will store financial transactions with the fields
'''

import sqlite3

def to_trans_dict(trans_tuple):
    ''' trans is a transaction tuple ( item_num, amount, category, date, desc)'''
    tran = {'item_num':trans_tuple[0], 'amount':trans_tuple[1], 'category':trans_tuple[2], 'date':trans_tuple[3],'desc':trans_tuple[4]}
    return tran

def to_trans_dict_list(trans_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_trans_dict(tran) for tran in trans_tuples]

class Transaction:
    ''' connects with the sqlite database and create add, select, and delete methods --Bohan'''

    # connect to the database and create the five fields: item_num, amount, category, date, description
    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num text, amount int, category text, date text, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    # return all the transactions in the database 
    def select_all(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT * from transactions""")
        rows = cur.fetchall()
        con.close()
        #return [dict(row) for row in rows]
        return to_trans_dict_list(rows)


    # return one transaction in the database
    def select_one(self, id):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT * FROM transactions WHERE id = ?""", (id,))
        row = cur.fetchall()
        con.close()
        #return dict(row)
        return to_trans_dict(row)


    # add a transaction to the database
    def add(self, item):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""INSERT INTO transactions VALUES(?,?,?,?,?)""",
                    (item['item_num'], item['amount'], item['category'], item['date'], item['description']))
        con.commit()
        con.close()

    # delete a transaction from the database
    def delete(self, id):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""DELETE FROM transactions WHERE id = ?""", (id,))
        con.commit()
        con.close()
