import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# get the time when the script ran (present date, present time, lol)
current_time = dt.datetime.now()

# generate random year to visit
random_year = randint(0,6000)
year_to_visit = dt.datetime(random_year, current_time.month, current_time.day, current_time.hour, current_time.minute, current_time.second)

# calculate price
time_diff = current_time.year - random_year
base_cost = Decimal('75.00')
cost_multiplier = Decimal('1.33')
total_cost = (Decimal(time_diff) * cost_multiplier + base_cost) * -1

# possible destinations
destinations = ['Tokyo', 'Jerusalem', 'Greece', 'Atlantis', 'Washington DC', 'The Moon!']
destination = choice(destinations)

custom_module.generate_time_travel_message(year_to_visit, destination, total_cost)