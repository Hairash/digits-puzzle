WIDTH = 5
HEIGHT = 4
FIELD_WIDTH = WIDTH * 2 + 1
FIELD_HEIGHT = HEIGHT * 2 + 1

class LogicError(Exception):
    pass


field = [[1] * FIELD_WIDTH for _ in range(FIELD_HEIGHT)]
field = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
figure = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
]

def rotate_figure(figure):
    # 0 0 - 0 1
    # 0 1 - 1 1
    # 0 2 - 2 1
    # 0 3 - 3 1


    rotated_figure = [list(el)[::-1] for el in zip(*figure)]
    return rotated_figure


def put_figure(field, figure, x, y):
    try:
        figure_width = len(figure)
        figure_height = len(figure[0])
        for fld_x in range(x, x + figure_width):
            for fld_y in range(y, y + figure_height):
                fig_x = fld_x - x
                fig_y = fld_y - y
                if figure[fig_x][fig_y] and field[fld_x][fld_y]:
                    raise LogicError('Cell occupied')
        for fld_x in range(x, x + figure_width):
            for fld_y in range(y, y + figure_height):
                fig_x = fld_x - x
                fig_y = fld_y - y
                if figure[fig_x][fig_y]:
                    field[fld_x][fld_y] = figure[fig_x][fig_y]
    except (IndexError, LogicError) as e:
        print(str(e))



def output_field(field):
    transposed_field = [list(el) for el in zip(*field)]
    for y in range(FIELD_HEIGHT):
        for x in range(FIELD_WIDTH):
            if x % 2 and not y % 2 and transposed_field[x][y]:
                print('-', end=' ')
            elif not x % 2 and y % 2 and transposed_field[x][y]:
                print('|', end=' ')
            else:
                print(' ', end=' ')
        print()


def output_figure(figure):
    transposed_field = [list(el) for el in zip(*figure)]
    for y in range(len(transposed_field[0])):
        for x in range(len(transposed_field)):
            if x % 2 and not y % 2 and transposed_field[x][y]:
                print('-', end=' ')
            elif not x % 2 and y % 2 and transposed_field[x][y]:
                print('|', end=' ')
            else:
                print(' ', end=' ')
        print()


output_field(field)
put_figure(field, figure, 0, 4)
output_field(field)
# print('figure')
# output_figure(figure)
figure1 = rotate_figure(figure)
put_figure(field, figure1, 2, 4)
output_field(field)

# print('figure')
# output_figure(figure1)
# figure2 = rotate_figure(figure1)
# print('figure')
# output_figure(figure2)
# figure3 = rotate_figure(figure2)
# print('figure')
# output_figure(figure3)
