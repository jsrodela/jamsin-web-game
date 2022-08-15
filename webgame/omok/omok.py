import numpy as np
import os


def clear():
    return os.system('cls')


def game_rule(board, player):

    game_result = 0

    diag_line = np.zeros(5)

    # 가로 다섯 줄 감지 코드
    for i_idx in range(len(board)):
        for j_idx in range(len(board)-4):
            pl = (board[i_idx, j_idx:j_idx+5] == player)

            if pl.sum() == 5:
                game_result = 1

                return game_result

    # 세로 다섯 줄 감지 코드
    for i_idx in range(len(board)-4):
        for j_idx in range(len(board)):
            pl = (board[i_idx:i_idx+5, j_idx] == player)

            if pl.sum() == 5:
                game_result = 1

                return game_result

    # 대각선 다섯 줄 감지 코드
    for i_idx in range(len(board)-4):
        for j_idx in range(len(board)-4):

            diag_line[0] = board[i_idx+0, j_idx+0]
            diag_line[1] = board[i_idx+1, j_idx+1]
            diag_line[2] = board[i_idx+2, j_idx+2]
            diag_line[3] = board[i_idx+3, j_idx+3]
            diag_line[4] = board[i_idx+4, j_idx+4]

            pl = (diag_line == player)

            if pl.sum() == 5:

                game_result = 1
                return game_result


size_of_board = 7
board_array = np.zeros((size_of_board, size_of_board))

max_turn = size_of_board*size_of_board

for i in range(max_turn):
    if i % 2 == 0:  # 흑돌이 돌을 둠
        position = input('흑돌 차례입니다:')

        sub_p = position.split(' ')
        pos_H = int(sub_p[0])
        pos_W = int(sub_p[1])

        board_array[pos_H, pos_W] = 1  # 1은 흑돌

    else:  # 백돌이 돌을 둠
        position = input('백돌 차례입니다:')

        sub_p = position.split(' ')
        pos_H = int(sub_p[0])
        pos_W = int(sub_p[1])

        board_array[pos_H, pos_W] = 2  # 2는 백돌

    print(board_array)
