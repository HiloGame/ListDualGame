import random

playing = False
fastest_round = 0

def game():
    print("game started.")
    agression = random.randint(4,6) #higher value = higher agression
    cowardice = random.randint(3,8) #lower value = higher guarding
    turn = 0
    player_ammo = True
    enemy_ammo = True
    player_distance = 0
    enemy_distance = 0

    #print("agression: ", agression)
    #print("cowardice: ", cowardice)

    field = ["*","-","-","-","-","-","-","%"]

    while playing == True:
        print(field)
        print("                ^map^")
        #Enemy decision
        enemy_action = "guard"

        enemy_stat = random.randint(0, 10)
        if enemy_stat <= agression:
            if enemy_ammo == False:
                enemy_action = "reload"
            else:
                enemy_action = "shoot"

        else:
            enemy_stat = random.randint(0, 10)
            if enemy_stat > cowardice:
                enemy_action = "move"
            else: enemy_action = "guard"
        #print(enemy_action)

        #Player action
        print("----------\n! Your turn !\n\n")
        if player_ammo:
            print("You have a bullet in the chamber.")
        else: print("Your gun is empty.")
        action = input("act: ")
        if action == "1":
            if player_ammo == False:
                print("*Click!* : Your gun is empty.")

            #shooting logic

            player_ammo = False
            tally = 0
            #print("Player distance:", player_distance)
            for i in range(player_distance, (len(field))):
                if i == "%":
                    break
                tally += 1
            print("Shot fired from ",tally, "meters.", 10-tally,"/10 chance of hitting.")
            shot = random.randint(10-tally,10)
            #print("Roll:", shot)
            if shot <= 10-tally:
                if enemy_action == "guard":
                    print("Shot hit: Opponent guarded.")
                else:
                    print("Shot hit. You win!")
                    return(turn)
            else:
                print("Shot missed.")
            tally = 0

        if action == "2":
            guarded = True
        
        #moving logic

        if action == "3":
            for i in range(len(field)):
                if field[i+1] == "%":
                    print("You are face to face with the enemy!")
                    break
                if field[i] == "*":
                    field[i] = "-"
                    field[i+1] = "*"
                    player_distance = player_distance + 1
                    print("You moved forward.")
                    break

        if action == "4":
            if player_ammo == True:
                print("Your gun was already loaded.")
            else:
                player_ammo = True
                print("You reloaded your gun.")
            

        #Enemy action
        print("----------\nOpponent's turn.\n")
        if enemy_action == "shoot":
            if enemy_ammo == True:
                count = 0
                #print(range(player_distance,len(field)))
                for i in range(player_distance, len(field)):
                    if i == "%":
                        #print(field[i])
                        break
                    count += 1
                #print("opponent count:", count)
                shot = random.randint(10-count,10)
                #print("Enemy Roll:", shot)
                if shot <= 10-count:
                    if action == "3":
                        print("Your opponent shot you, but you guarded.")
                    else:
                        print("You were shot by your opponent. You lose.")
                        return(turn)
                else:
                    print("Your opponent shot at you, but missed.")
                count = 0
            enemy_ammo = False
    
        if enemy_action == "reload":
            enemy_ammo = True
            print("You hear your opponent reloading.")
        
        if enemy_action == "guard":
            print("Your opponent protected themselves.")
        
                    
        print("Turn end.\n----------\n")


if fastest_round == 0:
    print("\nWelcome! The aim of the game is to elimate your opponent. Each turn, you have three choices. \n1:Shoot \n2:Guard \n3:Move \n4:Reload")
    play = input("Please type anything to play:")
    if play != "":
        playing = True
        game()

