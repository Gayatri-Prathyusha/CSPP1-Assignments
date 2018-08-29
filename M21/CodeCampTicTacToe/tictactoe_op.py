""" program  for the tic - tac - toe game"""
def is_valid_game(game_grid):
    '''check's whether game isvalid'''
    x_count, o_count = 0, 0
    for each_row in game_grid:
        for each_box in each_row:
            if each_box == 'x':
                x_count += 1
            elif each_box == 'o':
                o_count += 1
            elif each_box == '.':
                pass
            else:
                return "invalid input"
    if abs(o_count - x_count) != 1:
        return "invalid game"

    return None

def horizontal_check(game_grid):
    '''checks for horizontal conditions'''
    for each_row in game_grid:
        if each_row.count(each_row[0]) == 3 and each_row[0] != '.':
            return each_row[0]
    return None

def vertical_check(game_grid):
    '''checks vertical'''
    win_c = 0
    win_n = game_grid[0][0]
    grid_l = len(game_grid)
    for i in range(grid_l):
        if win_c == 3:
            break
        win_c = 0
        win_n = game_grid[0][i]
        if win_n == '.':
            continue
        for j in range(grid_l):
            if game_grid[j][i] == win_n:
                win_c += 1
            else:
                break
    if win_c == 3:
        return win_n
    return None

def diagonal_left_to_right(game_grid):
    '''checks diagonal left to right'''
    grid_l = len(game_grid)
    win_n = game_grid[0][0]
    win_c = 0
    if win_n != '.':
        for i in range(grid_l):
            if game_grid[i][i] == win_n:
                win_c += 1
            else:
                break
    if win_c == 3:
        return win_n
    return None

def diagonal_right_to_left(game_grid):
    '''checks diagonal right to left'''
    grid_l = len(game_grid)
    win_n = game_grid[0][-1]
    win_c = 0
    if win_n != '.':
        for i in range(grid_l):
            if game_grid[i][-i-1] == win_n:
                win_c += 1
            else:
                break
    if win_c == 3:
        return win_n
    return None

def play_game(game_grid):
    '''its playing game'''
    return is_valid_game(game_grid) or horizontal_check(game_grid) or \
    vertical_check(game_grid) or diagonal_left_to_right(game_grid) or \
    diagonal_right_to_left(game_grid) or "draw"


def main():
    """ Main function"""
    grid_lines = 3
    input_grid = []
    for _ in range(grid_lines):
        input_grid.append(input().split())
    print(play_game(input_grid))
main()
