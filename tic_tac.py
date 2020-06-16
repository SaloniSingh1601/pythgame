board=[' ' for x in range(10)]  #This is designing the empty boardcopy
import time

def insertLetter(letter,pos):
    board[pos]=letter            #This places the character on the board

def isSpaceFree(pos):
    return board[pos]==' '     #This tells whether that specified position in the board is empty

def printboard(board):

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('------------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('------------')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
                                                                   #This function designs the board

def isboardfull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
                                                               #This function checks if the board is full

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))
                                                             #This function is used to decide winner

def playermove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Observe carefully, this space is occupied')
            else:
                print("I guess you didn't get it please type a number between 1 and 9")

        except:
            print('Arey yaar type a NUMBER!!!')


def computermove():
    possiblemoves=[x for x,letter in enumerate(board) if letter == ' ' and x != 0]
    move=0
    for let in ['O','X']:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if IsWinner(boardcopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possiblemoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edgesOpen = []
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(li):
    import random
    l=len(li)
    r=random.randrange(0,l)
    return li[r]
dec=True
while (dec==True):

    print("Hola!!!Let's start playing")
    time.sleep(1)
    printboard(board)
    time.sleep(1)

    while not(isboardfull(board)):
        #if isboardfull(board):
        #    print('The game is tied.But I want to get this finished')

        if not(IsWinner(board,'O')):
            playermove()
            time.sleep(1)
            printboard(board)
        else:
            print('Hahaha!You lose!')
            break
        if not(IsWinner(board,'X')):
            move=computermove()
            if move==None:
                print(" ")
            else:
                insertLetter('O',move)
                print('Computer Ji has placed O on',move,'now you place')
                time.sleep(2)
                printboard(board)
        else:
            print('You win!!Maybe you got lucky -_-')
            break
    if isboardfull(board):
        print('The game is tied.But I want to get this finished')


    x=input('Wanna give it another try?? (y/n)')
    time.sleep(1)
    if x.lower()=='y':
        board = [' ' for x in range(10)]
        print('-------------------')
        print('Get Set Go!')
        time.sleep(1)
        dec=True
    else:
        print('Get lost and find yourself')
        break
