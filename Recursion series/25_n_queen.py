# def is_safe(board, r, c):
#     # check vertical
#     for i in range(r):
#         if board[i][c]:
#             return False
#
#     # check left diagonal
#     max_left = min(r,c)
#     # we are starting from 1 because if we start from 0, it will check the current row where the queen is placed now.
#     # And it will give true. So if condition will pass and return False
#     for i in range(1, max_left + 1):
#         if board[r-i][c-i]:
#             return False
#
#     # check right diagonal
#     max_right = min(r, len(board)-c-1)
#     for i in range(1, max_right + 1):
#         if board[r-i][c+i]:
#             return False
#
#     return True
#
# def print_board(board):
#     for row in board:
#         for el in row:
#             if el:
#                 print("Q ", end="")
#             else:
#                 print("X ", end="")
#         print()
#
# def n_queen(board, r):
#     if r == len(board):
#         print_board(board)
#         print()
#         return 1
#
#     count = 0
#     for i in range(len(board)):
#         if is_safe(board, r, i):
#             board[r][i] = True
#             count += n_queen(board, r+1)
#             board[r][i] = False
#
#     return count

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False

    max_left = min(row, col)
    for i in range(1, max_left + 1):
        if board[row - i][col - i] == "Q":
            return False

    max_right = min(row, len(board) - col - 1)
    for i in range(1, max_right + 1):
        if board[row - i][col + i] == "Q":
            return False

    return True


def nQueen(board, row):
    if row == len(board):
        res = [["".join(r) for r in board]]
        # print(f"res = {res}")
        return res

    final_res = []
    for i in range(len(board)):
        if is_safe(board, row, i):
            board[row][i] = "Q"
            final_res.extend(nQueen(board, row + 1))
            # print(f"final = {final_res}")
            board[row][i] = "."
    return final_res


def solveNQueens(n: int):
    board = [["." for _ in range(n)] for _ in range(n)] #
    return nQueen(board, 0)


n = 5
chess_board = [[False for _ in range(n)] for _ in range(n)]
# print(n_queen(chess_board, 0))
print(solveNQueens(4))