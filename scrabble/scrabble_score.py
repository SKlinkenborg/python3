# define letters and points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# create a dictionary of letters to points using zip and comprehensions
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

# create a function to score words
def score_word(word):
    point_total = 0
    for letter in list(word):
        if letter in letter_to_points.keys():
            point_total += letter_to_points[letter]
    return point_total

# # test function
# brownie_points = score_word("BROWNIE")
# print(brownie_points)
# blue = score_word("BLUE")
# print(blue)
# # 15

# dictionary of players and words played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], 
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
# track player scores
player_to_points = {}

# calculate each player's score
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
        # print(word + " " + str(player_points))
    player_to_points[player] = player_points
print(player_to_points)
# {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

# If you want extended practice, try to implement some of these ideas with the Python you’ve learned:
#     * play_word() — a function that would take in a player and a word, and add that word to the list
#          of words they’ve played
#     * update_point_totals() — turn your nested loops into a function that you can call any time a word
#          is played
#     * make your letter_to_points dictionary able to handle lowercase inputs as well