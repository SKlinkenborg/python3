#!/usr/bin/env python3

""" physics.py: Solutions for codecademy Functions Project """

__author__ = "Samuel Klinkenborg"
__copyright__ = "copyleft"

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below:
# Convert fahrenheit to celsius 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return(c_temp)
# find 100 f in C
f100_in_celsius = f_to_c(100)

# Convert Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return(f_temp)
# find 0 C in F
c0_in_fahrenheit = c_to_f(0)

# Calculate Force
def get_force(mass, acceleration):
  return(mass * acceleration)
# Calculate train's Force
train_force = (get_force(train_mass, train_acceleration))
print(f"The GE train supplies {train_force:.2f} Newtons of force.")

# Calculate energy
def get_energy(mass, c = 3*10**8):
  return(mass * (c ** 2))
# calculate bomb energy
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# Calculate Work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return(force * distance)
# Calculate train work
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")

'''
Output:
The GE train supplies 226800.00 Newtons of force.
A 1kg bomb supplies 90000000000000000 Joules.
The GE train does 22680000 Joules of work over 100 meters.
'''