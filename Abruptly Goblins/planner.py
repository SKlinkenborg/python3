# create a list to hold our gamers
gamers = []

# each gamer is a dictionary with two keys: "name" that holds their name and "availability": a list holding days of the week they're available to play
def add_gamer(gamer, gamers_list):
    if "name" in gamer.keys() and "availability" in gamer.keys():
        gamers_list.append(gamer)
    else:
        print(f"This function requires a name key and an availability key")


# populate our gamers list with players
kimberly = {"name": "kimberly", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for player in gamers_list:
        for day in player["availability"]:
            if day in available_frequency:
                available_frequency[day] += 1
            else:
                print("Oops. Check your days of the week.")

calculate_availability(gamers, count_availability)
# print(count_availability)

def find_best_night(availability_table):
    return max(availability_table.items(), key=lambda x: x[1])[0]


# rough breakdown of above lambda ^
# my_dict = {'a': 10, 'b': 5, 'c': 20}

# # Step 1: Get items as tuples
# items = my_dict.items()  # [('a', 10), ('b', 5), ('c', 20)]

# # Step 2: Find max tuple based on value (x[1])
# max_pair = max(items, key=lambda x: x[1])  # ('c', 20)

# # Step 3: Extract key
# result = max_pair[0]  # 'c'
# print(result)  # Output: 'c'

# alternative for find_best_night w/out lambda function, closer to what we've been taught sofar:
# def get_key_of_max_value(dictionary):
#     max_key = None
#     max_value = float('-inf')  # Start with smallest possible number
    
#     for key, value in dictionary.items():
#         if value > max_value:
#             max_value = value
#             max_key = key
    
#     return max_key

game_night = find_best_night(count_availability)
# print(game_night)
def available_on_night(gamers_list, day):
    attending_game_night = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            attending_game_night.append(gamer["name"])
    return(attending_game_night)

attending_game_night = available_on_night(gamers, game_night)

form_email = "Hey {name}, listen! We've been invited to play {game} this upcoming {day_of_week}!"
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        email = form_email.format(name = gamer, game = game, day_of_week = day)
        print(email)
send_email(attending_game_night, game_night, "Abruptly Goblins!")

unable_to_attend_best_night = []
for gamer in gamers:
    if not game_night in gamer["availability"]:
        unable_to_attend_best_night.append(gamer)
(unable_to_attend_best_night)

second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")