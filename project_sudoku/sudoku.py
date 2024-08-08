board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def solve(bod):

    find = find_empty(bod)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bod, i, (row, col)):
            bod[row][col] = i

            if solve(bod):
                return True

            bod[row][col] = 0

    return False


def valid(bod, num, pos):

    # check row
    for i in range(len(bod[0])):
        if bod[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bod)):
        if bod[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bod[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bod):

    for i in range(len(bod)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bod[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(bod[i][j])

            else:
                print(str(bod[i][j]) + " ", end="")


def find_empty(bod):
    for i in range(len(bod)):
        for j in range(len(bod[0])):
            if bod[i][j] == 0:
                return (i, j)  # row, col

    return None


print_board(board)
solve(board)
print("________________________\n")
print_board(board)
