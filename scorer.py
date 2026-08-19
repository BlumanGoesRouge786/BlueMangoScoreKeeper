#For the recoed this script was meant to have all types of scorers for differnt games.

def t_tennis(e_score: int):
    """Table tennis scorer: first to e_score with a two-point advantage."""
    #Vars: e_score = integer

    #Team name input
    HT=input("Home Player/Team: ")
    AT=input("Away Player/Team: ")
    
    #Meant for stating team names and at what score must you have in order to win
    print(f"{HT} vs {AT}")
    print("Game to", e_score)

    #initial starting points.
    h = 0
    a = 0

    #Below are the contents of what happens during the game.

    while True:
        #As log as none of the players'/teams' scores are not equivalent, game continues.

        p = input("P (h/a): ").strip().lower()
        #Meant for user to input whoever gets the point.
        #Note: Probably should have used a toggle but who cares.

        if p == "h":
            h += 1
            #Basically, If the point belongd to home team, home team gets the point.

        elif p == "a":
            a += 1
            #The same thing happens here but in the favor of the away team.

        else:
            print("Invalid input - enter 'h' or 'a'")
            continue

        print("Home:" + str(h), "Away:" + str(a))
        #Statement of current scores

        if (h >= e_score or a >= e_score) and abs(h - a) >= 2:
            winner = HT if h > a else AT
            if winner[-1] == s:
                verb = win
            else:
                verb = wins
            print(winner, verb)
            break

        #This is in the case where the normal scoring system where both teams are one point
        #below the End Point, the End Point gets increased by one only allowing  two point 
        #difference between the winner and loser.

    #And finally the winner determination.


if __name__ == "__main__":
    import sys
    target = 5

    if len(sys.argv) > 1:
        try:
            target = int(sys.argv[1])
        except ValueError:
            print("Invalid target score, using default 5")

    t_tennis(target)
