#Copyright - Arpith Athreyas HS , [Git link]github.com/Arpith3
'''tik tak toe is a game between two players . Here is the code to enable the game for those who want to play and learn ''' 

places = []

for i in range (0, 9) :
    places.append(str(i+1))

player_Turn = True
winner = False

#creating the board
def print_Board() :
    print( '\n -------')
    print( ' |' + places[0] + '|' + places[1] + '|' + places[2] + '|')
    print( ' -------')
    print( ' |' + places[3] + '|' + places[4] + '|' + places[5] + '|')
    print( ' -------')
    print( ' |' + places[6] + '|' + places[7] + '|' +places[8] + '|')
    print( ' -------\n')
"""
#Draw situation is not handled
#added a counter to avoid looping if draw
"""
#the main part of the program 
moves=0
while not winner and moves<9:
    print_Board()

    if player_Turn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        n = int(input(">> "))
        #removed index out of bound error if n>9
        if places[n - 1] == 'X' or places [n-1] == 'O':
            print("illegal move, plase try again")
            continue
    except:
        print("please enter a valid field")
        continue
    

    if player_Turn :
        places[n - 1] = 'X'
    else :
        places[n - 1] = 'O'

    player_Turn = not player_Turn
    moves+=1
    #checking for the possibility of winning 
    for i in range (0, 3) :
        j = i * 3
        if (places[j] == places[(j + 1)] and places[j] == places[(j + 2)]) :
            winner = True
            print_Board()
        if (places[i] == places[(i + 3)] and places[i] == places[(i + 6)]) :
            winner = True
            print_Board()

    if((places[0] == places[4] and places[0] == places[8]) or (places[2] == places[4] and places[4] == places[6])) :
        winner = True
        print_Board()

#if exit condition is moves, then winner will be false
#else if exit is because of Bool-winner, it will be True
if winner:
    print (str(int(player_Turn + 1)) + " wins the game:)!\n")
else:
    print("Draw match")
