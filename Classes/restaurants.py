class Restaurant:
    '''Describes a restaurant'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []
    
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')
    
    def rest_open(self):
        print(f'{self.rest_name} is open')

    def add_num_served(self):
        how_many = int(input(f'How many customers served today for {self.rest_name}? '))
        self.number_served += how_many
    
    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers')

    def customer_rating(self):
        cust_rating = int(input('How would you rate your experience today on a scale of 1-5 (5 being excellent)? '))
        self.customer_ratings.append(cust_rating)
        avg_rating = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f'Your rating was {cust_rating}. The average rating for this restaurant is {avg_rating}')

taco_baco = Restaurant('Taco Baco', 'fast food tacos and more')
weedys = Restaurant('Weedy\'s', 'hurgusburgus')
applebapples = Restaurant('Applebapple\'s', 'American grib and bib')

weedys.customer_rating()
weedys.customer_rating()
weedys.customer_rating()
weedys.customer_rating()
weedys.customer_rating()