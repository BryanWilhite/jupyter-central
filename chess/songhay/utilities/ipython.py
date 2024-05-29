from IPython import display
import chess
import chess.svg

def display_html_from_list(htmlList):
    html = list()
    for htmlFragment in htmlList:
        html.append(htmlFragment)
    return display.HTML(''.join(html))

def display_svg(html):
    html = ''.join([
        '<div id="svg-block" style="display: inline-block">',
        html,
        '</div>',
    ])

    return html

def display_taken(taken, size=24):
    return display.HTML(get_taken(taken, size=size))

def get_board_and_push(board, move, black_taken = [], white_taken = [], size=240, arrows = []):
    board.push(move)
    html = ''.join([
        '<div id="svg-board-block" style="display: inline-block; margin:.5em">',
        f'    <h2>{move.uci()}{": check " if board.is_check() else ""}</h2>',
        f'    <div>{get_taken(white_taken)}</div>',
        chess.svg.board(board, arrows=arrows, size=size) if len(arrows) > 0 else chess.svg.board(board, size=size),
        f'    <div>{get_taken(black_taken)}</div>',
        '</div>',
    ])

    return html

def get_taken(taken, size=24):
    svgs = list()
    for piece in taken:
        svgs.append(chess.svg.piece(chess.Piece.from_symbol(piece), size=size))

    return f'<div style="background-color:rgba(255, 255, 255, 0.5);margin:.5em">{"".join(svgs)}</div>'
