def score_word(word):
    print_total = 0
    for x in word:
        print_total += letters_to_points.get(x.upper(),0)
    return print_total

def play_word(player, word):
    if player in player_to_words:
        player_to_words.get(player).append(word)
    else:
        player_to_words[player] = [word]
    update_point_totals()

def update_point_totals():
    for player in player_to_words:
        player_points = 0
        for word in player_to_words.get(player):
            player_points += score_word(word) # meow
        player_to_points[player] = player_points
    print(player_to_points)

def show_winner():
    maxscore = 0
    for x in player_to_points:
        if player_to_points.get(x) > maxscore:
            maxscore = player_to_points[x]
            winner = x
        elif player_to_points.get(x) == maxscore:
            winner = winner + ' and ' + x
    print("The winner is:",winner)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
player_to_words = {"player1":['BLUE','TENNIS','EXIT'],"wordNerd":['EARTH','EYES','MACHINE'],'Lexi Con':['ERASER','BELLY','HUSKY'],'Prof Reader':['ZAP','COMA','PERIOD']}

letters_to_points = {key:value for key, value in zip(letters,points)}
letters_to_points[" "] = 0
player_to_points = {}

update_point_totals()
play_word('player1',"panda")
play_word('wordNerd','Sweet')
play_word('coco','zigzag')
play_word('coco','quite')
play_word('liu','exactly')
play_word('liu','perfect')
play_word('liu','cab')

show_winner()


