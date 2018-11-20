
#%% Exercise 1
shopping_list = {"Guitar":1000,
               "Pick_box":5,
               "Guitar_string":10
               
               }
shopping_cart = ["Guitar", "Guitar_string" ]

def checkout(shopping_cart):
    
    final_price=0
    
    if shopping_cart == []:
        return None
    else:
        for item in shopping_cart:
            final_price = final_price +(shopping_list [item])
    return final_price
    
checkout (shopping_cart)


#%% Exercise 2
    
prices = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10, "Insurance":5, "Priority mail":10}

prices_cart = []
service_prices =[]

def checkout_blue(mycart):
 
    if "Insurance" in mycart:
            service_prices.append(prices["Insurance"])
    if "Priority mail" in mycart:
        service_prices.append(prices["Priority mail"])
    
    while "Insurance" in mycart:
        mycart.remove("Insurance")
    while "Priority mail" in mycart:
        mycart.remove("Priority mail")
    
    if mycart == []:
        return None
    
    else:
        for i in mycart: 

            prices_cart.append(prices[i])          
                
    return sum(prices_cart) + sum (service_prices)
    
checkout_blue([ "Insurance","Insurance","Insurance", "Guitar"])

#%% Exercise 3
    
prices = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10, "Insurance":5, "Priority mail":10}
tiers = {"Normal": 1, "Silver": 0.98, "Gold": 0.95}

prices_cart = []
service_prices =[]

def checkout_black(tier, mycart):
 
    if "Insurance" in mycart:
            service_prices.append(prices["Insurance"])
    if "Priority mail" in mycart:
        service_prices.append(prices["Priority mail"])
        
    while "Insurance" in mycart:
        mycart.remove("Insurance")
    while "Priority mail" in mycart:
        mycart.remove("Priority mail")
    
    
    if tier == "Silver":
        for i in mycart: 
            prices_cart.append(prices[i]) 
        return sum(prices_cart) * (tiers["Silver"]) + sum(service_prices)
        
    if tier == "Gold":
        for i in mycart: 
            prices_cart.append(prices[i])
        return (sum(prices_cart) + sum (service_prices)) * (tiers["Gold"])
    if tier == "Normal":
        for i in mycart: 
            prices_cart.append(prices[i])
        return (sum(prices_cart) + sum (service_prices))
    
    if mycart == []:
        return None
    
    else:
        for i in mycart: 
            prices_cart.append(prices[i])

    return (sum(prices_cart) + sum (service_prices))
    

#checkout_black("Gold", ["Pick Box", "Insurance", "Insurance", "Priority mail", "Priority mail"])
checkout_black("Silver", ["Guitar Strings", "Insurance","Insurance", "Priority mail", "Priority mail"])