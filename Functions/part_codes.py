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

input= input("Enter as supplier:productcode-size ")

def getsuppliercode(inp):
    semicolon=input.split(' : ')
    print(semicolon)
def getproductnum(inp):
    next=input.split('-')
    print(next)
def getsize(inp):
    next2=input.split('-')
    print(next2)

   
getsuppliercode(input)
getproductnum(input)
getsize(input)