def printcross(place):
    print('   |   |   ')
    print(f' {place[6]} | {place[7]} | {place[8]} ')
    print('   |   |   ')
    print('___________')
    print('   |   |   ')
    print(f' {place[3]} | {place[4]} | {place[5]} ')
    print('   |   |   ')
    print('___________')
    print('   |   |   ')
    print(f' {place[0]} | {place[1]} | {place[2]} ')
    print('   |   |   ')

def winornot(place):
    for i in 'XO':
        for j in [0,3,6]:
            if place[j] == i and place[j + 1] == i and place[j + 2] == i:
                return True
        for j in [0,1,2]:
            if place[j] == i and place[j + 3] == i and place[j + 6] == i:
                return True
        if place[0] == i and place[4] == i and place[8] == i:
            return True
        elif place[2] == i and place[4] == i and place[6] == i:
            return True
    else:
        return False
    
while True:    
    ch = input('Player 1 choose your symbol O/X')
    if ch == 'o':
        p1 = 'O'
        p2 = 'X'
    elif ch == 'x':
        p1 = 'X'
        p2 = 'O'
    else:
        ch = input('Please choose either O or X\nPlayer 1 choose your symbol O/X')
    mymaze = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    printcross(mymaze)
    itrate = 1
    chance = ''

    while not winornot(mymaze):
        if itrate%2 == 1:
            chance = p1
        else:
            chance = p2
        inpt = int(input(f'player {chance} its your turn'))
        if mymaze[inpt - 1] == ' ':
            mymaze[inpt - 1] = chance
        else:
            print('You cant mark there')
            break
        printcross(mymaze)
        if winornot(mymaze):
            print(f'YOU WIN PLAYER {chance}!!')

        itrate += 1
    else:
        cont = input('Do you wanna play again Y/N ?')
        if cont == 'n':
            print('Thanks for playing')
            break
