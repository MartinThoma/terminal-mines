from terminal_mines import Minefield, input_loop, render

minefield = Minefield(10, 10, {"3,3", "8,8", "5,2", "0,4", "6,0"})

x = 0
y = 0


def handle_key(key):
    global x, y

    if key == "w":
        y = (y - 1) % minefield.height
    elif key == "s":
        y = (y + 1) % minefield.height
    elif key == "a":
        x = (x - 1) % minefield.width
    elif key == "d":
        x = (x + 1) % minefield.width
    elif key == "e":
        minefield.flag_cell(x, y)
    elif key == "\n":
        minefield.reveal_cell(x, y)

    render(minefield, x, y)


render(minefield, x, y)
input_loop(handle_key)
