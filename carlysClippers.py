#!/usr/bin/env python3

""" carlysClippers.py: Solutions for codecademy Loops Project """

__author__ = "Samuel Klinkenborg"
__copyright__ = "copyleft"

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_revenue = 0
# Calculate total price of all haircuts
for price in prices: total_price = total_price + price
# create a variable called average_price that is the total_price divided by the number of prices, then print it
average_price = total_price / len(prices)
print(f"Average Haircut Price: {average_price}")
# use a list comprehension to reduce all prices by 5, then print the new prices
new_prices = [price - 5 for price in prices]
print(f"New Prices: {new_prices}")
# calculate total revenue (+= revenue at index i + number of cuts at index i)
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: {total_revenue}")
# find the average daily revenue
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: {average_daily_revenue}")
# list the haircuts under $30 w a list comprehension
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(f"Haircuts under $30: {cuts_under_30}")

"""
Sample Output:

Average Haircut Price: 31.875
New Prices: [25, 20, 35, 15, 15, 30, 45, 30]
Total Revenue: 1085
Average Daily Revenue: 155.0
Haircuts under $30: ['bouffant', 'pixie', 'crew', 'bowl']

"""