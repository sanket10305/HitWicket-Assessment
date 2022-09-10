class Chess():
    def __init__(self):
        pass

    def promotion(self):
        pass

    def move(self):
        pass
class Board():

    def __init__(self):
        pass

    def print_board(self):
        pass

class Piece():

    def __init__(self):
        pass
        
    def is_valid_move(self):
        return False

    def is_white(self):
        pass

    def __str__(self):
        return ''

class Rook(Piece):
    def __init__(self, color):
        pass

    def is_valid_move(self, board, start, to):
        pass

class Knight(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class Bishop(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class Queen(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class King(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass
    
    def can_castle(self):
        pass

class GhostPawn(Piece):
    def __init__(self, color):
        pass

    def is_valid_move(self):
        return False

class Pawn(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

if __name__ == "__main__":
    chess = Chess()
    chess.board.print_board()

    while True:
        start = input("From: ")
        to = input("To: ")
        
        start = translate(start)
        to = translate(to)

        if start == None or to == None:
            continue

        chess.move(start, to)

        i = 0
        while i < 8:
            if not chess.turn and chess.board.board[0][i] != None and \
                chess.board.board[0][i].name == 'P':
                chess.promotion((0, i))
                break
            elif chess.turn and chess.board.board[7][i] != None and \
                chess.board.board[7][i].name == 'P':
                chess.promotion((7, i))
                break
            i += 1

        chess.board.print_board()