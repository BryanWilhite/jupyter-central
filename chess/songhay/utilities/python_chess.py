from urllib import request
from io import StringIO 
import chess, chess.pgn, chess.svg

full_move_number = 0
last_turn = 1
last_san = ""
move_list = []
black_taken = []
white_taken = []

def get_board_html(board,move_index=0,
                   taken='',
                   board_size=240,
                   taken_size=24,
                   arrows=[],
                   orientation=chess.WHITE,
                   is_question=False):
    '''Gets the HTML to display the python-chess Board.'''

    global full_move_number, last_turn, last_san, move_list, black_taken, white_taken

    move = move_list[move_index]
    san = last_san
    is_white_move = last_turn
    is_white_orientation = orientation == chess.WHITE

    if(len(board.move_stack) == move_index):
        san = board.san(chess.Move.from_uci(move.uci()))
        last_san = san
        is_white_move = board.turn == 1
        last_turn = board.turn
        board.push(move_list[move_index])

        if move_index % 2 == 0:
            full_move_number = full_move_number + 1
        else:
            pass

        if taken and not is_white_move:
            black_taken.append(taken)

        if taken and is_white_move:
            white_taken.append(taken)

        if is_question:
            arrows.append(
                chess.svg.Arrow(move_list[move_index].to_square,
                                move_list[move_index].to_square,
                                color='#cf1020'))

    html = ''.join([
        '<div id="svg-board-block" style="display: inline-block; margin:.5em">',
        '<h2>',
        '    <small style="color:rgba(217, 217, 217, 0.5)" title="exchange number">',
        f'{full_move_number}:</small>',
        '    <small style="color:rgba(217, 217, 217, 0.5)" title="exchange number">',
        f'{"White" if is_white_move else "Black"}</small> {san}',
        f'{"<span style=""color:#cf1020"">?!</span>" if is_question else ""}',
        '</h2>',
        '    <div>',
        f'{get_taken_html(black_taken if is_white_orientation else white_taken,size=taken_size)}',
        '    </div>',
        chess.svg.board(board,orientation=orientation,
                        arrows=arrows,lastmove=move_list[move_index],size=board_size),
        '    <div>',
        f'{get_taken_html(white_taken if is_white_orientation else black_taken,size=taken_size)}',
        '    </div>',
        '</div>',
    ])

    arrows.clear()

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

def request_lichess_pgn(id, game_type='game/export'):
    '''
    Request lichess.org PGN data.
        known `game_type=` values: 'game/export' (default), 'study'
    '''

    uri = f'https://lichess.org/{game_type}/{id}?literate=1'

    if game_type == 'study':
        uri = f'https://lichess.org/{game_type}/{id}.pgn'

    resp = request.urlopen(uri)

    return resp.read().decode('UTF-8')

def set_game_moves(game):
    '''Sets the global move list of the specified python-chess Game.'''

    global move_list
    move_list = list(game.mainline_moves())
