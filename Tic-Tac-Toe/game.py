class TicTacToe:
    def __init__(self):
        # use a single list to rep 3X3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep on track the winner

    def print_board(self):
        # this is for getting the row
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print(print('| '+' | '.join(row)+' |'))

    def available_moves(self):
        return []
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x','x','o'] --> [(0,'x'),(1,'x'),(2,'0')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
