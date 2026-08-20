#For the recoed this script was meant to have all types of scorers for differnt games.

#Colors because plain text is boring.
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
PURPLE = "\033[95m"
RESET = "\033[0m"


def t_tennis(e_score: int):
    """Table tennis scorer: first to e_score with a two-point advantage."""
    #Vars: e_score = integer
    #Meant for stating at what score must you have in order to win
    print(f"{PURPLE}Game to {e_score}{RESET}")

    #Getting the names of the two people playing the game.
    #This is so we dont have to call them Home and Away the entire time.
    home_player = input(f"{BLUE}Home player/team: {RESET}")
    away_player = input(f"{YELLOW}Away player/team: {RESET}")

    #Finding out whether the names belong to a player or a team.
    #This is so the program knows whether to say "wins" or "win".
    game_type = input(
        f"{BLUE}Are you playing Singles or Doubles? (S/D): {RESET}"
    ).strip().lower()

    #initial starting points.
    #Nobody has scored yet because the game has not started.
    h = 0
    a = 0

    #Below are the contents of what happens during the game.
    #This is where the actual game is happening and stuff.

    while True:
        #As log as none of the players'/teams' scores are not equivalent, game continues.
        #The game will keep going until somebody wins.
        #Hopefully this doesnt become an infinite loop.

        p = input(f"P ({BLUE}h{RESET}/{YELLOW}a{RESET}): ").strip().lower()
        #Meant for user to input whoever gets the point.
        #Note: Probably should have used a toggle but who cares.
        #h means home and a means away incase you forgor.

        if p == "h":
            h += 1
            #Basically, If the point belongd to home team, home team gets the point.
            #One point has been awarded to the home player.
        
        elif p == "a":
            a += 1
            #The same thing happens here but in the favor of the away team.
            #Away player gets a point because they did the thing.

        else:
            print(f"{RED}Invalid input - enter 'h' or 'a'{RESET}")
            #If you type something stupid the program will tell you.
            #This is better than the program just exploding.

            continue
            #Go back and ask again because that input was not very usefull.

        print(
            f"{BLUE}{home_player}: {h}{RESET}",
            f"{YELLOW}{away_player}: {a}{RESET}"
        )
        #Statement of current scores
        #Prints the score so we know who is currently winning.

        if (h >= e_score or a >= e_score) and abs(h - a) >= 2:
            #This checks if somebody has reached the End Point AND is winning by two.
            #Because you cant win table tennis by just being one point ahead.
            #Very important rule or the game would be stupid.

            winner = home_player if h > a else away_player
            #Decides who won based on who has the higher score.
            #The person with more points is usually the winner.

            word = "wins" if game_type == "S" else "win"
            print(f"{GREEN}{winner} {word}{RESET}")
            #Finally tell the winner that they have won the game.
            #Congratulations you hit the ball better than the other guy.

            break
            #Game is over so we stop the loop.
            #No more points because someone already won.

        #This is in the case where the normal scoring system where both players are one point
        #below the End Point, the End Point gets increased by one only allowing  two point 
        #difference between the winner and loser.
        #This is also why the loop keeps going when both players are tied near the end.

    #And finally the winner determination.
    #The winner has already been determined above because I changed the code.
    #Leaving this comment here anyway.


if __name__ == "__main__":
    #This makes sure the scorer only starts when this file is actually run.
    #Python does some magic here that I dont fully understand.
    import sys

    #Default game score incase the user doesnt give one in the command line.
    target = 5

    if len(sys.argv) > 1:
        #If there is something after the file name, we assume its the score.
        try:
            target = int(sys.argv[1])
            #Turn whatever they typed into a integer so the scorer can use it.
        except ValueError:
            print(f"{RED}Invalid target score, using default 5{RESET}")
            #They typed something that isnt a number so we use 5 instead.
            #Because 5 is a perfectly respectable number.
    else:
        #If no score was given when starting the program, ask the user for one.
        #This makes it easier for people who dont know how to use command line stuff.
        try:
            target = int(input("What score should the game go to? "))
            #Turn the users answer into a integer because input is normally text.
        except ValueError:
            print(f"{RED}Invalid target score, using default 5{RESET}")
            #If they typed something that isnt a number we just use 5.
            #Because apparently numbers are hard.

    t_tennis(target)
    #Start the scorer with the target score.
    #LET THE GAMES BEGIN.
