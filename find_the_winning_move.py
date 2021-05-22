from sys import stdin, stdout

mem = {}


def is_moves_left(gameboard):
    for i in range(4):
        for j in range(4):
            if (gameboard[i][j] == '.'):
                return True
    return False


def evaluate(b):
    for i in range(4):
        if (b[i][0] == b[i][1] == b[i][2] == b[i][3]):
            if (b[i][0] == 'x'):
                return 10
            elif (b[i][0] == 'o'):
                return -10

        if (b[0][i] == b[1][i] == b[2][i] == b[3][i]):
            if (b[0][i] == 'x'):
                return 10
            elif (b[0][i] == 'o'):
                return -10

    if (b[0][0] == b[1][1] == b[2][2] == b[3][3]):
        if (b[0][0] == 'x'):
            return 10
        elif (b[0][0] == 'o'):
            return -10

    if (b[0][3] == b[1][2] == b[2][1] == b[3][0]):
        if (b[0][3] == 'x'):
            return 10
        elif (b[0][3] == 'o'):
            return -10

    return 0


def minimax(board, isMax):

    str_board = str(board)

    if str_board in mem.keys():
        return mem[str_board]

    score = evaluate(board)

    if (score == 10):
        mem[str_board] = score
        return score

    if (score == -10):
        mem[str_board] = score
        return score

    if (is_moves_left(board) == False):
        mem[str_board] = score
        return 0

    if (isMax):
        for i in range(4):
            for j in range(4):
                if (board[i][j] == '.'):
                    board[i][j] = 'x'
                    branch_res = minimax(board, not isMax)
                    board[i][j] = '.'
                    if branch_res == 10:
                        mem[str_board] = branch_res
                        return branch_res
        ret = -10
    else:
        for i in range(4):
            for j in range(4):
                if (board[i][j] == '.'):
                    board[i][j] = 'o'
                    branch_res = minimax(board, not isMax)
                    board[i][j] = '.'
                    if branch_res < 10:
                        mem[str_board] = branch_res
                        return branch_res
        ret = 10
    mem[str_board] = ret
    return ret


def findBestMove(board):
    for i in range(4):
        for j in range(4):
            if (board[i][j] == '.'):
                board[i][j] = 'x'
                moveVal = minimax(board, False)
                board[i][j] = '.'
                if (moveVal > 0):
                    return "("+str(i)+","+str(j)+")\n"

    return "#####\n"


def main():
    while (stdin.readline().strip() != '$'):
        gameboard = [[], [], [], []]
        for i in range(4):
            row = stdin.readline().strip()
            for j in row:
                gameboard[i].append(j)
        stdout.write(findBestMove(gameboard))


if __name__ == '__main__':
    main()
