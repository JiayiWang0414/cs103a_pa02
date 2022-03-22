'''
transaction.py will store financial transactions with the fields
'''

import sqlite3

class Transaction:
    ''' connects with the sqlite database and create add, select, and delete methods --Bohan'''

    # connect to the database and create the five fields: item_num, amount, category, date, description
    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num text, amount int, category text, date int, description text)''')
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
        return [dict(row) for row in rows]

    # return one transaction in the database
    def select_one(self, id):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT * FROM transactions WHERE id = ?""", (id,))
        row = cur.fetchall()
        con.close()
        return dict(row)

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
        con.commmit()
        con.close()
