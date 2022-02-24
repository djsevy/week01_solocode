''' 
How to play TicTacToe
1) 2 players will play on a 9 square grid
2) Player 1 will choose a space 1-9 to place an "X". This ends their turn
3) Player 2 will choose a space 1-9 to place an "O". This ends their turn
4) The players will alternate turns untill one of them wins
5) The first player to have 3 consecutive "X's" or "O's" wins
6) If neither player is able to do this, the game ends in a tie.

functions I will be using:

main: This is there the game will be played

display grid: this will be the playing board

player 1: this will be the first players turn

player 2: this will be the second players turn

check win: this will check to see if one of the players has won

'''

grid = [' 1 ' , ' 2 ' , ' 3 ' ,
        ' 4 ' , ' 5 ' , ' 6 ' ,
        ' 7 ' , ' 8 ' , ' 9 ' ,]


#                 |      Horizontal         |    Diagonal     |        Vertical         |
winning_combos = ((0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8))

player1 = " X "
player2 = " O "

game_over = False

current_player = None

def main():
    print('\nThank you for playing TIC TAC TOE! Enjoy!\n')

    display_grid()
    
    while not game_over: 
        turn()
       
    

def display_grid():
    print('\n|-----|-----|-----|')
    print('| ' + grid[0] + ' | ' + grid[1] + ' | ' + grid[2] + ' | ')
    print('|-----|-----|-----|')
    print('| ' + grid[3] + ' | ' + grid[4] + ' | ' + grid[5] + ' | ')
    print('|-----|-----|-----|')
    print('| ' + grid[6] + ' | ' + grid[7] + ' | ' + grid[8] + ' | ')
    print('|-----|-----|-----|\n')


def player_1():
    global current_player
    
    choice = current_player
    choice = input('\nplayer 1, please choose a number between 1-9: ')
    choice = int(choice) - 1
    grid[choice] = player1



    display_grid()

def player_2():
    global current_player
    
    choice = current_player
    choice = input('player 2, please choose a number between 1-9: ')
    choice = int(choice) - 1
    grid[choice] = player2

    display_grid()

def turn():
    global current_player
    
    if current_player == player_1():
        current_player = player_2()
    elif current_player == player_2():
        current_player = player_1()



def check_winner():
    count = 0
    
    for i in winning_combos:
        if grid[i[0]] == [i[1]] == [i[2]] == 'X':
            print('The winner is Player 1\n')
            print('You did it!\n')
            return True
        elif grid[i[0]] == [i[1]] == [i[2]] == 'O':
            print('The winner is Player 2\n')
            print('You did it!\n')
            return True
    
    for i in range(9):
        if grid[i] == 'X' or grid[i] == 'O':
            count +1
        elif count == 9:
            print('The game is a tie!')
            return True 
main()
