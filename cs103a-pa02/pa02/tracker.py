#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

'''

#from transactions import Transaction
#import sys
from category import Category
from transaction import Transaction


#transactions = Transaction('tracker.db')
category = Category('tracker.db')
transaction = Transaction('transaction.db')

# here is the menu for the tracker app

MENU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''
# show how to process the menu.
def process_choice(choice):
    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    # show transactions--Bohan & Charlotte
    elif choice == '4':
        items = transaction.select_all()
        print_transactions(items)
    # add transaction --Bohan
    elif choice == '5':
        item_num = input("item number: ")
        item_amount = input("transaction amount: ")
        item_category = input("transaction category: ")
        item_date = input("transaction date: ")
        item_desc = input("transaction description: ")
        transaction.add({'item_num': item_num, 'amount': item_amount,
                         'category': item_category,'date': item_date,'description': item_desc})
    # delete transaction--Bohan & Charlotte
    elif choice == '6':
        row = int(input("the item_num of the deleted transaction: "))
        transaction.delete(row)
    # summarize transactions by date --Jiayi
    elif choice =='7':
        date=input("transaction date: ")
        items=transaction.select_all()
        item_date=[item for item in items if item["date"]==date]
        print_transactions(item_date)
   # summarize transactions by month--Jiayi
    elif choice =='8':
        month=input("transaction month: ")
        items=transaction.select_all()
        item_month=[item for item in items if month in item["date"]]
        print_transactions(item_month)
   # summarize transactions by year--Jiayi
    elif choice=='9':
        year=input("transaction year: ")
        items=transaction.select_all()
        item_year=[item for item in items if year in item["date"]]
        print_transactions(item_year)

    #summarize transactiosn by category - Charlotte
    elif choice=='10':
        categoryselect=input("transaction category:")
        items=transaction.select_all()
        item_by_category=[item for item in items if item["category"]==categoryselect]
        print_transactions(item_by_category)

    #print this menu - Charlotte
    elif choice=='11':
        print(MENU)
    
    else:
        print("choice",choice,"not yet implemented")

    choice = input("> ")
    return choice
def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(MENU)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

#edit print_transactions helper method, take date as text - Charlotte
def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s"%(
        'item #','amount','category','date','description'))
    print('-'*40)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10d %-10s %-10s %-30s"%values)

def print_category(cat):
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))
# print all of the categories.
def print_categories(cats):
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)


# here is the main call!
toplevel()
