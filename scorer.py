#For the recoed this script was meant to have all types of scorers for differnt games.

def t_tennis(e_score: int):
#Vars: e_score = integer
#Meant for stating at what score must you have in order to win
    print ("Game to", e_score)
    
#initial starting points.
    h = 0
    a = 0

#Below are the contents of what happens during the game.

    while not (h or a) == e_score:
#As log as none of the players'/teams' scores are not equivalent, game continues.
        
        p = input("P: ")
#Meant for user to input whoever gets the point.
#Note: Probably should have used a toggle but who cares.

        if p == "h":
            h = h + 1
#Basically, If the point belongd to home team, home team gets the point.
        
        if p == "a":
            a = a + 1
#The same thing happens here but in the favor of the away team.

        print("Home:"+str(h),"Away:"+str(a))
#Statement of current scores

        if (h and a) == e_score - 1 and h == a:
            e_score = e_score + 1
            print ("Game to", e_score)

#This is in the case where the normal scoring system where both teams are one point
#below the End Point, the End Point gets increased by one only allowing  two point 
#difference between the winner and loser.

    if h == e_score :
        w = "Home"
    if a == e_score:
        w = "Away"
#And finally the winner determination.
    print (w,"Player wins")
