gagne=0
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player= 1


def show_board(board):
    print('   ', end='')
    for i in range(9): 
        if (i == 2 or i == 5 ): 
            
            print(" | "+str(board[i]))
            print("   -----------")
            print('   ', end='')
        else : 
            print(" | "+str(board[i]), end='')


show_board(board)

def tour(board, player):
    print("\n")
    print("player : "+str(player))
    li=input("box ? : ")
    print("played box : ("+li+"")

    while board[(int(li)-1)]!=" ":
        show_board(board)
        print("\n")
        print("box already played ! pls choose an other box ^^'")
        li=input("Enter box's number : ")
        print("You have chosen box number :"+li+",")

    if player==1 :
        board[(int(li)-1)]="X"
    if player==2 :
        board[(int(li)-1)]="O"
    show_board(board)

def win(board):
    if (board[0]==board[1]) and (board[0]==board[2]) and (board[0]!=" "):
        return 1
    if (board[3]==board[4]) and (board[3]==board[5]) and (board[3]!=" "):
        return 1
    if (board[6]==board[7]) and (board[6]==board[8]) and (board[6]!=" "):
        return 1
    if (board[0]==board[3]) and (board[0]==board[6]) and (board[0]!=" "):
        return 1
    if (board[1]==board[4]) and (board[1]==board[7]) and (board[1]!=" "):
        return 1
    if (board[2]==board[5]) and (board[2]==board[8]) and (board[2]!=" "):
        return 1
    if (board[0]==board[4]) and (board[0]==board[8]) and (board[0]!=" "):
        return 1
    if (board[2]==board[4]) and (board[2]==board[6]) and (board[2]!=" "):
        return 1





while gagne==0:
    tour(board,player)
    if win(board):
        print("\n")
        print("Player "+str(player)+" won the game")
        gagne=1

    if player == 1 :
        player = 2 
    elif player == 2 : 
        player = 1