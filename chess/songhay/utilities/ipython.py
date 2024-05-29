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

def display_svgs(svgs):
    html = list()
    for svg in svgs:
        html.append(display_svg(svg))
    return display.HTML(''.join(html))

def display_taken(taken):
    svgs = list()
    for piece in taken:
        svgs.append(chess.svg.piece(chess.Piece.from_symbol(piece), size=24))
    return display_svgs(svgs)

def get_board_and_push(board, move, black_taken, white_taken):
    board.push(move)
    html = ''.join([
        '<div id="svg-board-block" style="display: inline-block; margin:.5em">',
        f'    <div>{display_taken(black_taken)}</div>',
        chess.svg.board(board, size=240),
        f'    <div>{display_taken(white_taken)}</div>',
        '</div>',
    ])

    return html
