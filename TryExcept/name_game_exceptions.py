name = input('Enter a name: ').lower()

def trunc_name(nam):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    n = nam[0]
    n2 = nam[1]
    if n in vowels:
        return nam
    elif n2 not in vowels:
        return nam[2:]
    else:
        return nam[1:]
    
# print(trunc_name(name))

trunc_n = trunc_name(name)

def name_game(n):
    yield f'{n.capitalize()}, {n.capitalize()}, bo-b{trunc_n}'
    yield f'banana fana fo-f{trunc_n}'
    yield f'me my mo-m{trunc_n}'
    yield f'{n.capitalize()}'

print('Original results:')

for i in name_game(name):
    print(i)



# BONUS: accounting for special rules for b, f, and m

def name_game_b(b):
    yield f'{b.capitalize()}, {b.capitalize()}, bo-{trunc_n}'
    yield f'banana fana fo-f{trunc_n}'
    yield f'me my mo-m{trunc_n}'
    yield f'{b.capitalize()}!'

def name_game_f(f):
    yield f'{f.capitalize()}, {f.capitalize()}, bo-b{trunc_n}'
    yield f'banana fana fo-{trunc_n}'
    yield f'me my mo-m{trunc_n}'
    yield f'{f.capitalize()}!'

def name_game_m(m):
    yield f'{m.capitalize()}, {m.capitalize()}, bo-b{trunc_n}'
    yield f'banana fana fo-f{trunc_n}'
    yield f'me my mo-{trunc_n}'
    yield f'{m.capitalize()}!'

print("Bonus print results:")

name = input('Enter a name: ').lower()

def print_results():
    if name[0] == 'b':
        for i in name_game_b(name):
            print(i)
    elif name[0] == 'f':
        for i in name_game_f(name):
            print(i)
    elif name[0] == 'm':
        for i in name_game_m(name):
            print(i)
    else:
        for i in name_game(name):
            print(i)


# Exercise 3.B, Lab 2 

print('Incorporating Try-Except logic...')

name = None

while name == None:
    try:
        name = input('Name? ').lower()
        int(name)
    except ValueError:
        pass
    else:
        print("Not a valid name (must be 2 or more letters)")
        name = None

n = None
while n == None:
    try:
        n = name[0]
    except IndexError:
        print(f"Error:. '{name}' is not a valid name.")
        name = None

n2 = None
while n2 == None:
    try:
        n2 = name[1]
    except IndexError:
        print(f"Error:. '{name}' is not a valid name.")
        name = None

trunc_n = trunc_name(name)

print_results()