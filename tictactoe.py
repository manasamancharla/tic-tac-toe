
def printboard(xState,zState):
    zero  = 'X' if xState[0] else ('O' if zState[0] else 0)
    one   = 'X' if xState[1] else ('O' if zState[1] else 1)
    two   = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four  = 'X' if xState[4] else ('O' if zState[4] else 4)
    five  = 'X' if xState[5] else ('O' if zState[5] else 5)
    six   = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    print(f"     {zero} | {one} | {two} ")
    print(f"    ---|---|---")
    print(f"     {three} | {four} | {five} ")
    print(f"    ---|---|---")
    print(f"     {six} | {seven} | {eight} ")

def win(xState,zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(xState[win[0]]+xState[win[1]]+xState[win[2]] == 3):
            print("Winner is Player 1")
            return 1
        if(zState[win[0]]+zState[win[1]]+zState[win[2]] == 3):
            print("Winner is Player 2")
            return 0
    return -1

def play():
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1
    while(True):
        print(" ---Tic Tac Toe---")
        printboard(xState,zState)
        print("")
        if(turn == 1): #Player 1 is X
            print("Player 1 Chance:")
            value = int(input("Please enter a value "))
            xState[value] = 1
        else: #Player 2 is O
            print("Player 2 Chance:")
            value = int(input("Please enter a value "))
            zState[value] = 1
        z = win(xState,zState)
        if(z == -1):
            turn = 1 - turn
            continue
        else:
            break

def Game():
    print("TIC TAC TOE")
    print("1. Play")
    print("2. Exit")
    choice = int(input("Enter an option: "))
    if(choice == 1):
        play()
    if(choice == 2):
        print("Have a nice day")

if __name__ == "__main__":
    Game()
