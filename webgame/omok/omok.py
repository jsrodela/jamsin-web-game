import numpy as np


class OmokGame():
    def __init__(self, size: int = 19) -> None:
        self.create_board(size)

        # 1: black, 2: white
        self.turn = 1

        self.ply = 0

    def create_board(self, size: int) -> None:
        self.size = size
        self.board = np.zeros((self.size, self.size))
        self.max_turn = self.size*self.size

    def check_win(self, player: int) -> bool:
        game_result = False
        diag_line = np.zeros(5)

        # 가로 다섯 줄 감지 코드
        for i_idx in range(self.size):
            for j_idx in range(self.size-4):
                pl = (self.board[i_idx, j_idx:j_idx+5] == player)

                if pl.sum() == 5:
                    game_result = True
                    return game_result

        # 세로 다섯 줄 감지 코드
        for i_idx in range(self.size-4):
            for j_idx in range(self.size):
                pl = (self.board[i_idx:i_idx+5, j_idx] == player)

                if pl.sum() == 5:
                    game_result = True
                    return game_result

        # 대각선 다섯 줄 감지 코드
        for i_idx in range(self.size-4):
            for j_idx in range(self.size-4):

                diag_line[0] = self.board[i_idx+0, j_idx+0]
                diag_line[1] = self.board[i_idx+1, j_idx+1]
                diag_line[2] = self.board[i_idx+2, j_idx+2]
                diag_line[3] = self.board[i_idx+3, j_idx+3]
                diag_line[4] = self.board[i_idx+4, j_idx+4]

                pl = (diag_line == player)

                if pl.sum() == 5:
                    game_result = True
                    return game_result

        return game_result

    def check_result(self) -> int:
        # Draw
        if self.ply == self.max_turn:
            return 3
        # Black wins
        if self.check_win(1):
            return 1
        # White wins
        if self.check_win(2):
            return 2
        # Game goes on
        return 0

    def move(self, x: int, y: int) -> bool:
        if self.board[x][y] != 0:
            return False
        self.board[x][y] = self.turn
        self.turn ^= 3
        self.ply += 1
        return True


if __name__ == '__main__':
    game = OmokGame()
    print(game.board)
    while True:
        while True:
            try:
                x, y = map(int, input(
                    f"{['','흑','백'][game.turn]}돌 차례입니다:").split())
                if game.move(x, y):
                    break
            except ValueError:
                pass
            print('잘못된 수입니다')
        print(game.board)
        result = game.check_result()
        if result == 1:
            print('흑돌 승')
            break
        elif result == 2:
            print('백돌 승')
            break
        elif result == 3:
            print('무승부')
            break
