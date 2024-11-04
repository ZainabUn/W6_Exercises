# Create a new script file named substrings.py.  
# ∗ Start by working with a variable containing a full name, e.g. name = ‘John Doe’ 
# ∗ Write code to find the space in the name, then extract the first and last name and 
# display the results. Output might look like: 
# Full Name: John Doe 
# First Name: John 
# Last Name: Doe 
# 2. Once you have the code working for one name, test your script with at least three times 
# with different names. The full output (full name, first name, last name) should be 
# printed for each name. Examples: 
# parse_and_display(‘John Doe’) 
# parse_and_display(‘Grace Flores’) 
# parse_and_display(‘JB Oinonen’)
# CHALLENGE:  
# ∗ Modify your script to work with names of one, two or three words. Output should 
# include middle name if applicable. Example names to use when testing your new 
# function: 
# Lorde 
# Billie Eilish 
# Megan Thee Stallion 


name= 'Zainab Unisa'

def parse_and_display(name):
    namesplit= name.split()

    print(f'first name: {namesplit[0]}')
    print(f'last name: {namesplit[1]}')
