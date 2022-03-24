'''
transaction.py will store financial transactions with the fields
'''

import sqlite3

class Transaction:
    ''' connects with the sqlite database and create add, select, and delete methods --Bohan'''


    def __init__(self, dbfile):
        '''connect to the database and create the five fields: item_num, amount, category, date, description'''
        con = sqlite3.connect(dbfile)
        cur = con.cursor
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num text, amount int, category text, date int, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    
    def select_all(self):
        '''return all the transactions in the database '''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT * from transactions""")
        rows = cur.fetchall()
        con.close()
        return [dict(row) for row in rows]

    
    def select_one(self, id):
        '''return one transaction in the database'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""SELECT * FROM transactions WHERE id = ?""", (id,))
        row = cur.fetchall()
        con.close()
        return dict(row)

    
    def add(self, item):
        '''add a transaction to the database'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""INSERT INTO transactions VALUES(?,?,?,?,?)""",
                    (item['item_num'], item['amount'], item['category'], item['date'], item['description']))
        con.commit()
        con.close()

    
    def delete(self, id):
        '''delete a transaction from the database'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("""DELETE FROM transactions WHERE id = ?""", (id,))
        con.commmit()
        con.close()
