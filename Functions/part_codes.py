#Exercise 1A lab 2
# 2. Create a script that parses a part code in the following format:
# supplier:productcode-size
# Examples:
# ACME:123-L Part #123, size large, supplied by Acme
# DI:12345-M Part #12345, size medium, supplied by DI
# ACE:1-12 Part #1, size 12, supplied by Ace
# 3. Sketch your ideas for the functions below on a piece of paper:
# get_supplier_code()  returns all characters before the :
# get_product_num()  returns all characters between the : and -
# get_size()  returns all characters after the -
# Perform initial code review of each other’s ideas with a classmate. Then, code each
# function.
# 4. Once you have your functions ready, create variables to hold the three example part
# codes from above. Call all three functions for each part code and display the results.
# ∗ CHALLENGE: Try creating a variable that contains all three part codes as a list. How
# can you get your script to work with this list input?
# 5. Remember to commit changes when you are done!



def getsuppliercode(inp):
    semicolon=inp.find(':')
    return inp[:semicolon]
def getproductnum(inp):
    semicolon=inp.find(':')
    dash=inp.find('-')
    return inp[semicolon:dash]
    
def getsize(inp):
    afterdash=inp.rfind('-')
    return inp[afterdash:]
    
input=str( input("Enter supplier as :product:code-size "))


   
print(f'Supplier code:{getsuppliercode(input)} ')
print(f'Product Name : {getproductnum(input)}')
print(f'Size: {getsize(input)}')