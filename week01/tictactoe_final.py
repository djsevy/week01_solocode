
grid = [' 1 ' , ' 2 ' , ' 3 ' ,
        ' 4 ' , ' 5 ' , ' 6 ' ,
        ' 7 ' , ' 8 ' , ' 9 ' ,]

player1 = " X "
player2 = " O "

game_over = False

current_player = None

winner = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def main():
    print('\nThank you for playing TIC TAC TOE! Enjoy!\n')

    while not game_over: 
        turn()
        winner = check_winner()
        if winner == True:
            
            turn()
        
        elif game_over == True:
            play_again = input("play again? (y/n):\n").upper 
            if play_again == 'Y':
                main()
            else:
                print('Thank you for playing. Goodbye!')

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
    for i in winner:
        if grid[i[0]] == grid[i[1]] == grid[i[2]] == ' X ':
            print('Congrats, Player 1 is the winner.\n')
            return True
        
        if grid[i[0]] == grid[i[1]] == grid[i[2]] == ' O ':
                print("Congrats, Player 2 is the Winner!\n")
                return True


def draw(grid):
    for i in range(9):
        if grid[i] != player1 and grid[i] != player2:
            return False
    return True
    
main()