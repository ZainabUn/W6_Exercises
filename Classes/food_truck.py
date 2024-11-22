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


class FoodTruck(Restaurant):
    '''Describes a mobile food truck'''

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'
        self.truck_location = ''
    
    def accepts_private_bookings(self):
        bookings = input('Does this food truck accept private bookings? Y/N ')
        self.private_bookings = bookings
        if bookings == 'Y':
            accepts = 'accepts'
        else:
            accepts = 'does not accept'
        print(f'This food truck currently {accepts} private bookings')
    
    def relocate_truck(self):
        location = input("What is the truck's current location? ")
        self.truck_location = location
        print(f"Truck is currently located at {location}")

taco_baco_mobile = FoodTruck('Taco Baco on Wheels', 'tacos and more')

taco_baco_mobile.accepts_private_bookings()

taco_baco_mobile.relocate_truck()