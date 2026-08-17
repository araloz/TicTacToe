
def display_grid(grid):
    print("\n"*100)
    print('   |   |')
    print(' ' + grid[7] + ' | ' + grid[8] + ' | ' + grid[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + grid[4] + ' | ' + grid[5] + ' | ' + grid[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + grid[1] + ' | ' + grid[2] + ' | ' + grid[3])
    print('   |   |')

def user_input():
    while True:
        next_move = input("Where yo you want to play your next move? 1-9")
        if next_move.isdigit() and int(next_move) in range(1, 10):
            return int(next_move)
        print("Please enter a number between 1 and 9.")

def win_check(grid,mark):
    
    return ((grid[7] == mark and grid[8] == mark and grid[9] == mark) or # across the top
    (grid[4] == mark and grid[5] == mark and grid[6] == mark) or # across the middle
    (grid[1] == mark and grid[2] == mark and grid[3] == mark) or # across the bottom
    (grid[7] == mark and grid[4] == mark and grid[1] == mark) or # down the middle
    (grid[8] == mark and grid[5] == mark and grid[2] == mark) or # down the middle
    (grid[9] == mark and grid[6] == mark and grid[3] == mark) or # down the right side
    (grid[7] == mark and grid[5] == mark and grid[3] == mark) or # diagonal
    (grid[9] == mark and grid[5] == mark and grid[1] == mark)) # diagonal

def reset_grid(grid):
    grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return grid

grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ready = input("Are you ready to start? Yes/No\n")
count = 0

if ready.lower() == "yes":
    ready = True

while ready == True:
    display_grid(grid)
    if count % 2 == 0:
        grid[user_input()] = 'X'
        XorO = 'X'
    else:
        grid[user_input()] = 'O'
        XorO = 'O'

    if win_check(grid,XorO) == True:
        display_grid(grid)
        play_again = input("Do you want to play again? Yes/No")
        if play_again.lower() == "no":
            ready = False
        else:
            #grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            grid = reset_grid(grid)
        


    count += 1
    
print("GAME OVER")
    
