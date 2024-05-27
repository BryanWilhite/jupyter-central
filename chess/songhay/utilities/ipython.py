from IPython import display
import chess
import chess.svg

def display_svg(svg):
    svg = ''.join([
        '<div id="svg-block" style="display: inline-block">',
        svg,
        '</div>',
    ])

    return svg

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
