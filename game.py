import random

class Game:
    def __init__(self, width=12, height=12, moves_left=24, colors=None):
        if colors is None:
            colors = ['red', 'orange', 'purple', 'blue', 'green', 'yellow']
        self.width = width
        self.height = height
        self.colors = colors
        self.board = [[random.choice(colors) for _ in range(self.width)] for _ in range(self.height)]
        self.moves_left = moves_left

    def change_color(self, new_color):
        current_color = self.board[0][0]
        if self.moves_left > 0 and new_color != current_color and self.is_adjacent_color(new_color):
            Game.flood_fill(0, 0, current_color, new_color, self.board)
            self.moves_left -= 1
            if not self.check_win_condition and self.moves_left == 0:
                print("laba-5.recolor_dnlksnvv Over! You've run out of moves.")

    def is_adjacent_color(self, color, x=0, y=0, checked=None):
        if checked is None:
            checked = set()
        key = (x, y)
        if key in checked or x < 0 or y < 0 or x >= self.width or y >= self.height or self.board[x][y] != self.board[0][0]:
            return False
        checked.add(key)
        if (x > 0 and self.board[x-1][y] == color) or \
           (y > 0 and self.board[x][y-1] == color) or \
           (x < self.width-1 and self.board[x+1][y] == color) or \
           (y < self.height-1 and self.board[x][y+1] == color):
            return True
        return self.is_adjacent_color(color, x+1, y, checked) or \
               self.is_adjacent_color(color, x-1, y, checked) or \
               self.is_adjacent_color(color, x, y+1, checked) or \
               self.is_adjacent_color(color, x, y-1, checked)

    @staticmethod
    def flood_fill(x, y, old_color, new_color, board):
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board) or board[y][x] != old_color or board[y][x] == new_color:
            return
        board[y][x] = new_color
        Game.flood_fill(x+1, y, old_color, new_color, board)
        Game.flood_fill(x-1, y, old_color, new_color, board)
        Game.flood_fill(x, y+1, old_color, new_color, board)
        Game.flood_fill(x, y-1, old_color, new_color, board)

    @property
    def check_win_condition(self):
        first_color = self.board[0][0]
        return all(first_color == self.board[x][y] for x in range(self.height) for y in range(self.width))
