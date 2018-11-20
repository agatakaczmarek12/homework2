
#%% Exercise 1
from exercises import checkout

def test_emptylist_returns_none ():
    values = []
    for case in values:

        assert checkout(case) == None
        
def test_list_returns_one_item_price():
    values = [["Guitar"]]
    for case in values:
        assert checkout(case)==1000
        
def test_list_returns_two_items():
    values =[["Guitar","Guitar_string"]]
    for case in values: 
        assert checkout(case)==1010
    
#%%Exercise 2
    
from exercises import checkout_blue

def test_empty_returns_none():
    values = []
    for case in values:
        assert checkout_blue(case) == None
        
def test_one_guitar():
    values= [["Guitar"]]
    for case in values:
        assert checkout_blue(case) == 1000
        
def test_multipleinsurance_returns_only_one():
    values= [["Insurance","Insurance","Insurance", "Guitar"]]
    for case in values:
        assert checkout_blue(case) == 1005

def test_multiplemail_returns_only_two ():
    values=[["Guitar", "Priority mail", "Priority mail"]]
    for case in values:
        assert checkout_blue (case) == 1010

#%% Exercise 3
        
from exercises import checkout_black

def test_emptycart_returns_none ():
    values = []
    for case in values:
        assert checkout_black(case) == None
     
def test_checkout_black_gold():
    
    mycart = ["Pick Box", "Insurance", "Insurance", "Priority mail", "Priority mail"]
    
    for case in mycart:
        assert checkout_black("Gold",mycart) == 19
    
def test_checkout_black_silver ():
    mycart = ["Guitar Strings", "Insurance","Insurance", "Priority mail", "Priority mail"] 
    
    for case in mycart:
        assert checkout_black("Silver",mycart) == 24.8