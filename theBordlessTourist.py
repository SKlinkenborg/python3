destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ['historical site', 'art']]

attractions = [[], [], [], [], []]

# find the Destination in the destinations list by index number
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# find a traveler's destination by index number
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)