# cs103a_pa02

#Charlotte Wang

a. script for pylint

************* Module tracker
tracker.py:60:0: R0914: Too many local variables (20/15) (too-many-locals)
tracker.py:62:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:60:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:60:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:60:0: R0915: Too many statements (55/50) (too-many-statements)
tracker.py:134:4: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 9.30/10 (previous run: 9.30/10, +0.00)

b. script for pytest

============================= test session starts ==============================
platform darwin -- Python 3.8.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/charlottewang/Desktop/COSI103a/cs103a_pa02/cs103a-pa02/pa02, configfile: pytest.ini
plugins: anyio-3.5.0, dash-2.0.0
collected 2 items                                                              

test_transaction.py ..                                                   [100%]

============================== 2 passed in 0.05s ===============================


c. script for tracker.py features

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

> 4


item #     amount     category   date       description          
----------------------------------------
1          100        food       20220130   hang out with friends         
> 5
item number: 2
transaction amount: 20
transaction category: book
transaction date: 20220131
transaction description: study material
> 4
item #     amount     category   date       description                   
----------------------------------------
1          100        food       20220130   hang out with friends         
2          20         book       20220131   study material                
> 6
the item_num of the deleted transaction: 2
> 4
item #     amount     category   date       description                   
----------------------------------------
1          100        food       20220130   hang out with friends         
> 10
transaction category:food
(END)


#Jiayi Wang
Script started on Thu Mar 24 18:26:33 2022

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
ESC[?1034hbash-3.2$ python3 tracker.py

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

> 7
transaction date: 20220220
no items to print
> 5
item number: 3
transaction amount: 60
transaction category: book
transaction date: 20220308
transaction description: prepare for the midterm
> 7
transaction date: 20220308


item #     amount     category   date       description                   
----------------------------------------
3          60         book       20220308   prepare for the midterm       
> 8
transaction month: 03


item #     amount     category   date       description                   
----------------------------------------
3          60         book       20220308   prepare for the midterm       
> 9
transaction year: 2022
item #     amount     category   date       description                   
----------------------------------------
1          100        food       20220130   hang out with friends         
3          60         book       20220308   prepare for the midterm       
> pylint tracker.py
choice pylint tracker.py not yet implemented
> 0
bye
bash-3.2$ pylint tracker.py
************* Module tracker
tracker.py:60:0: R0914: Too many local variables (20/15) (too-many-locals)
tracker.py:62:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:60:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:60:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:60:0: R0915: Too many statements (55/50) (too-many-statements)
tracker.py:134:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:152:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)




bash-3.2$ pytest
ESC[1m============================= test session starts ==============================ESC[0m
platform darwin -- Python 3.9.5, pytest-6.2.5, py-1.9.0, pluggy-0.12.0
rootdir: /Users/jiayiwang/Desktop/cs103a_pa02/cs103a-pa02/pa02, configfile: pytest.ini
ESC[1mcollecting ... ESC[0mESC[1m^Mcollected 6 items                                                              ESC[0m

test_category.py ESC[32m.ESC[0mESC[32m.ESC[0mESC[32m.ESC[0mESC[32m.ESC[0mESC[32m                                                    [ 66%]ESC[0m
test_transaction.py ESC[32m.ESC[0mESC[32m.ESC[0mESC[32m                                                   [100%]ESC[0m

ESC[32m============================== ESC[32mESC[1m6 passedESC[0mESC[32m in 0.15sESC[0mESC[32m ===============================ESC[0m
bash-3.2$ exit

Script done on Thu Mar 24 18:28:50 2022

pylint
tracker.py:60:0: R0914: Too many local variables (20/15) (too-many-locals)
tracker.py:62:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:60:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:60:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:60:0: R0915: Too many statements (55/50) (too-many-statements)
tracker.py:134:4: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 9.30/10 (previous run: 9.30/10, +0.00)