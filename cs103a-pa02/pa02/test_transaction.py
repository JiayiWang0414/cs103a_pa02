import pytest
from transaction import Transaction


@pytest.fixture
def dbfile(tmpdir):
    '''create a database file in a temporary file'''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    '''create an empty database'''
    d_b = Transaction(dbfile)
    yield d_b

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat1 = {'item_num': '1', 'amount': 10, 'category': 'food', 'date': 20220320, 'description': 'groceries and takeout '}
    cat2 = {'item_num': '2', 'amount': 2, 'category': 'car', 'date': 20220320, 'description': 'gas and repairs'}
    cat3 = {'item_num': '3', 'amount': 5, 'category': 'fun', 'date': 20220320, 'description': 'movies and dining out'}
    id1 = empty_db.add(cat1)
    id2 = empty_db.add(cat2)
    id3 = empty_db.add(cat3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.mark.add
def test_add(small_db):
    '''test the add method in the transaction class'''
    cat0 = {'item_num': '4', 'amount': 15, 'category': 'food', 'date': 20220320, 'description': 'testing'}
    
    
@pytest.mark.delete
def test_delete(small_db):
    '''test the delete method in the transaction class'''
    # the initial table
    cats0=small_db.select_all()## original length
    # add this to the table
    cat0 = {'item_num': '0', 'amount': 2, 'category': 'test', 'date': 20220326, 'description': 'test'}
    id0=small_db.add(cat0)
    cat=small_db.select_all()##+1
    #delete this 
    small_db.delete(id0)
    cat00=small_db.select_all()##-1
    assert len(cat00)==len(cats0)
    assert len(cat00)==len(cat)-1
