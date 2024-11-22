class RewardsProgram:
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = 0

    def profile(self):
        print(f'Name: {self.cust_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')

    def thank_you(self):
        print(f'Thank you, {self.cust_name}, for visiting our restaurant!')
    
    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))
    
    def visit_rest(self):
        rest_name = input("Name of restaurant: ")
        if rest_name not in self.restaurants_visited:
            cust_list.append(rest_name)
        amount = float(input("What was the total food bill for this visit? $"))
        self.rewards_points += int(amount)
        print(f'Points for this visit: {int(amount)}')
        print(f'Total rewards points earned: {self.rewards_points}')
        print(f'Thank you for visiting {rest_name}')
   

cust_list = []

sample = RewardsProgram('Jane Sample', '630-689-5555', 'janesample@mail.com')
sample.profile()
sample.thank_you()
sample.add_to_cust_list()

# print(cust_list)

sample2 = RewardsProgram('Bob Garcia', '414-689-5555', 'bob_garcia@bobmail.com')
sample2.profile()
sample2.thank_you()
sample2.add_to_cust_list()

print(cust_list)

sample.visit_rest()

sample.visit_rest()