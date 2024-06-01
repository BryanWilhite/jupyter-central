from urllib import request
from io import StringIO 
import chess, chess.pgn, chess.svg

move_list = []
black_taken = []
white_taken = []

def get_board_html(board,move_index=0,
                   next_black_taken='',
                   next_white_taken='',
                   board_size=240,
                   taken_size=24,
                   arrows=[]):
    '''Gets the HTML to display the python-chess Board.'''

    global black_taken
    global white_taken

    move = move_list[move_index]

    if(len(board.move_stack) == move_index):
        board.push(move_list[move_index])

        if next_black_taken:
            black_taken.append(next_black_taken)

        if next_white_taken:
            white_taken.append(next_white_taken)

    html = ''.join([
        '<div id="svg-board-block" style="display: inline-block; margin:.5em">',
        '<h2>',
        f'    <small>exchange {board.fullmove_number}:</small>',
        f'    {"black" if board.turn else "white"} {move.uci()}',
        f'    {" [check]" if board.is_check() else ""}',
        '</h2>',
        f'    <div>{get_taken_html(white_taken,size=taken_size)}</div>',
        chess.svg.board(board, arrows=arrows, size=board_size) if len(arrows) > 0 else chess.svg.board(board, size=board_size),
        f'    <div>{get_taken_html(black_taken,size=taken_size)}</div>',
        '</div>',
    ])

    return html

def get_game_from_pgn_data(data):
    '''
        Gets the python-chess Game from the PGN data.
        See “Extract Data from PGN Files Using the Chess Library in Python”
        [https://www.geeksforgeeks.org/extract-data-from-pgn-files-using-the-chess-library-in-python/]
    '''

    pgn = StringIO(data)

    return chess.pgn.read_game(pgn)

def get_game_summary_html(game):
    '''Gets the HTML to display selected data from the python-chess Game.'''

    global move_list

    html = ''.join([
        f'<span><label>game moves:</label> {len(move_list)}</span>',
        '<span>&#160;|&#160;</span>',
        f'<span><label>no game errors:</label> {len(game.errors) == 0}</span>',
    ])

    return html

def get_taken_html(taken: "list[str]", size=24):
    '''Gets the HTML to display taken pieces from the python-chess Piece.'''

    html = list()
    for piece in taken:
        html.append(chess.svg.piece(chess.Piece.from_symbol(piece), size=size))

    return f'<div style="background-color:rgba(217, 217, 217, 0.5);margin:.5em">{"".join(html)}</div>'

def request_lichess_pgn(id):
    '''Request lichess.org PGN data.'''

    uri = f'https://lichess.org/game/export/{id}?literate=1'
    resp = request.urlopen(uri)

    return resp.read().decode('UTF-8')

def set_game_moves(game):
    '''Sets the global move list of the specified python-chess Game.'''

    global move_list
    move_list = list(game.mainline_moves())
