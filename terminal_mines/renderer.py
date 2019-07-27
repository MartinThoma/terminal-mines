from itertools import chain

from click import clear, style, echo

from .game_model import GameState, CellState

color_mapping = {
    CellState.FLAG: "bright_green",
    CellState.WARN1: "bright_cyan",
    CellState.WARN2: "cyan",
    CellState.WARN3: "bright_blue",
    CellState.WARN4: "bright_magenta",
    CellState.WARN5: "magenta",
    CellState.WARN6: "bright_yellow",
    CellState.WARN7: "bright_yellow",
    CellState.WARN8: "bright_yellow",
    CellState.EXPLODED: "bright_red"
}


def render(minefield, x, y):
    clear()

    def render_cell(iter_x, iter_y):
        state = minefield.get_cell(iter_x, iter_y).state

        bg = "red" if iter_x == x and iter_y == y else None
        fg = color_mapping.get(state, None)

        return style(state.value, bg=bg, fg=fg)

    def gen_lines():
        yield chr(0x250C) + chr(0x2500) * (minefield.width * 2 + 1) + chr(0x2510)

        for iter_y in range(minefield.height):
            iter_cells = (render_cell(iter_x, iter_y) for iter_x in range(minefield.width))
            yield " ".join(chain(chr(0x2502), iter_cells, chr(0x2502)))

        yield chr(0x2514) + chr(0x2500) * (minefield.width * 2 + 1) + chr(0x2518)

        if minefield.state == GameState.WON:
            yield " Game won"
        elif minefield.state == GameState.LOST:
            yield " Game lost"
        else:
            yield " Flags remaining: {}".format(minefield.flags_remaining)

    echo("\n".join(gen_lines()))