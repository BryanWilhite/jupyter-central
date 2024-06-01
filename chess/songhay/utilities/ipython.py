from IPython import display
import chess
import chess.svg

def display_html_from_list(htmlList: "list[str]"):
    '''
        Uses IPython.display.HTML to display a list of HTML strings.

        This is useful for folks who do not see the usefulness
        of approaches based on HBox (see “The VBox and HBox helpers”
        [https://ipywidgets.readthedocs.io/en/7.6.3/examples/Widget%20Styling.html#The-VBox-and-HBox-helpers]).
    '''

    html = list()
    for htmlFragment in htmlList:
        html.append(htmlFragment)

    return display.HTML(''.join(html))

def get_board_and_push(board,move,black_taken = [],white_taken = [],size=240,arrows = []):
    #if move not in board.move_stack:
    board.push(move)
    html = ''.join([
        '<div id="svg-board-block" style="display: inline-block; margin:.5em">',
        f'    <h2><small>exchange {board.fullmove_number}:</small> {move.uci()}{" [check]" if board.is_check() else ""}</h2>',
        f'    <div>{get_taken(white_taken)}</div>',
        chess.svg.board(board, arrows=arrows, size=size) if len(arrows) > 0 else chess.svg.board(board, size=size),
        f'    <div>{get_taken(black_taken)}</div>',
        '</div>',
    ])

    return html

def get_taken(taken: "list[str]", size=24):
    html = list()
    for piece in taken:
        html.append(chess.svg.piece(chess.Piece.from_symbol(piece), size=size))

    return f'<div style="background-color:rgba(217, 217, 217, 0.5);margin:.5em">{"".join(html)}</div>'
