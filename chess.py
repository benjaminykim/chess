class Board(object):
    board_dimension = 8

    w_pieces = [    [ 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P' ],
                    [ 'R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R' ]  ]

    b_pieces = [    [ 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p' ],
                    [ 'r', 'n', 'b', 'k', 'q', 'b', 'n', 'r' ]  ]

    piece_id_key = {
        'p' :   lambda x_coord, y_coord: Pawn('p', x_coord, y_coord, False),
        'P' :   lambda x_coord, y_coord: Pawn('P', x_coord, y_coord, True),
        'r' :   lambda x_coord, y_coord: Rook('r', x_coord, y_coord, False),
        'R' :   lambda x_coord, y_coord: Rook('R', x_coord, y_coord, True),
        'n' :   lambda x_coord, y_coord: Knight('n', x_coord, y_coord, False),
        'N' :   lambda x_coord, y_coord: Knight('N', x_coord, y_coord, True),
        'b' :   lambda x_coord, y_coord: Bishop('b', x_coord, y_coord, False),
        'B' :   lambda x_coord, y_coord: Bishop('B', x_coord, y_coord, True),
        'k' :   lambda x_coord, y_coord: King('k', x_coord, y_coord, False),
        'K' :   lambda x_coord, y_coord: King('K', x_coord, y_coord, True),
        'q' :   lambda x_coord, y_coord: Queen('q', x_coord, y_coord, False),
        'Q' :   lambda x_coord, y_coord: Queen('Q', x_coord, y_coord, True)
    }

    def __init__(self):
        self.board = self.__generate_board()
        self.__populate_board()

    def display(self):
        spacer = '    '
        for x_coord in range(self.board_dimension):
            row = ''
            for y_coord in range(self.board_dimension):
                row += spacer + (self.board[x_coord][y_coord]).display()
            row += '\n'
            print(row)

    def __generate_board(self):
        return [([ Square(',', x, y) for y in range(self.board_dimension)]) for x in range(self.board_dimension)]

    def __populate_board(self):
        # black pawns
        for index in range(self.board_dimension):
            self.board[1][index] = self.piece_id_key[self.b_pieces[0][index]](0, index)

        # black major pieces
        for index in range(self.board_dimension):
            self.board[0][index] = self.piece_id_key[self.b_pieces[1][index]](1, index)

        # white pawns
        for index in range(self.board_dimension):
            self.board[6][index] = self.piece_id_key[self.w_pieces[0][index]](6, index)

        # white major pieces
        for index in range(self.board_dimension):
            self.board[7][index] = self.piece_id_key[self.w_pieces[1][index]](7, index)


class Square(object):

    def __init__(self, piece_id, x_coord, y_coord):
        self.piece_id = piece_id
        self.x_coord = x_coord
        self.y_coord = y_coord

        if self.piece_id.islower():
            self.color_is_white = False
        else:
            self.color_is_white = True

    def display(self):
        return self.piece_id


class Pawn(Square):
    value = 1
    def __init__(self, piece_id, x_coord, y_coord, color_is_white=True):
        Square.__init__(self, piece_id, x_coord, y_coord)



class Rook(Square):
    value = 5
    def __init__(self, piece_id, x_coord, y_coord, color_is_white=True):
        Square.__init__(self, piece_id, x_coord, y_coord)


class Knight(Square):
    value = 3
    def __init__(self, piece_id, x_coord, y_coord, color_is_white=True):
        Square.__init__(self, piece_id, x_coord, y_coord)


class Bishop(Square):
    value = 3
    def __init__(self, piece_id, x_coord, y_coord, color_is_white=True):
        Square.__init__(self, piece_id, x_coord, y_coord)


class Queen(Square):
    value = 9
    def __init__(self, piece_id, x_coord, y_coord, color_is_white=True):
        Square.__init__(self, piece_id, x_coord, y_coord)
        self.id = 1


class King(Square):
    value = 0
    def __init__(self, piece_id, x_coord, y_coord, color_is_white=True):
        Square.__init__(self, piece_id, x_coord, y_coord)
        self.id = 1


if __name__ == '__main__':
    board = Board()
    board.display()
