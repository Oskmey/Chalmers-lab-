# /*
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29
#  *
#  */
from random import random,randint
result = 0
def run():
    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    welcome_msg(win_points) #Info
    players = get_players() #Ger spelare sina namn
    current = starting_player(players) #kallar på funktionen starting_player som väljer P1 eller P2 med index
    while not aborted: #Runda av spelet
        status_msg(players) #Ger spelaren poäng genom kallelse till fuktionen status_msg
        get_player_choice(current,result)
        round_msg(result,current, players)


    game_over_msg(current, aborted)




class Player:

    def __init__(self, name=''):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round


# ---- Game logic methods --------------
# TODO
#


# ---- IO Methods --------------
def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")

def status_msg(players):
    print("Points: ")
    for player in players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")

def round_msg(result, current, players):
    if result > 1:
        print("Got " + result + " running total are " + current.roundPts)
    else:
        print("Got 1 lost it all!")
        next_player(current,players)

def game_over_msg(player, is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + player.name + " with "
              + str(player.totalPts + player.roundPts) + " points")

def get_player_choice(current, result):
    player_action = input(f"It's {current.name}! do your want to roll, skip or quit? > ")
    while player_action.lower == "q":
        if player_action.lower == str(r):
            roll_dice(current)
            round_msg(result, current_player)
        elif player_action.lower == str(n):
            status_msg(players)
            next_player(current,players)
        elif player_action.lower == str(q):
            pass

def get_players():
     players = [Player(name=input("Player1 name: ")), Player(name=input("Player2 name: "))]
     return players

def starting_player(players): #väljer splare 1 eller 2 och skickar sedan till current
    start = randint(0, 1)
    start_player = players[start]
    return start_player

def roll_dice(current):
    result = randint(1, 6)
    current.roundPts = result + current.roundPts
    return result

def next_player(current,players):
    if players[0] == current:
        current = players[1]
    else:
        current = players[0]
    new_player_turn(current)

def new_player_turn(current):
    get_player_choice(current, result)


# ----- Testing -----------------
# Here you run your tests i.e. call your game logic methods
# to see that they really work (IO methods not tested here)
def test():
    # This is hard coded test data
    # An array of (no name) Players (probably don't need any name to test)
    test_players = [Player(), Player(), Player()]
    # TODO Use for testing of logical methods (i.e. non-IO methods)


if __name__ == "__main__":
    run()
