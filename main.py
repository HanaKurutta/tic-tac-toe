def output(field):
    print("    |  1  |  2  |  3  |")
    print("----|-----|-----|-----|")
    for i in range(3):
        print("", i+1, " ", end="|")
        for j in range(3):
            print(" ", field[i][j], " ", end="|")
        print("\n----|-----|-----|-----|")


def step(field, char):
    print("Сейчас ход игрока '" + char + "', введите строку и столбец ячейки:")
    x, y = int(input()) - 1, int(input()) - 1
    if x > 2 or x < 0 or y > 2 or y < 0:
        print("Координаты вне диапазона")
        step(field, char)
    elif field[x][y] == "-":
        field[x][y] = char
    else:
        print("Вы не можете походить в уже заполненное поле, выберите другую ячейку")
        step(field, char)


def check():
    win_cord = [((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != "-":
            return True
    return False


field = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

step_counter = 0

output(field)
while True:
    step(field, "X")
    step_counter += 1
    output(field)
    if check():
        print("Победили крестики!!!!")
        break
    if step_counter == 9:
        print("Ничья!!!!")
        break
    step(field, "0")
    step_counter += 1
    output(field)
    if check():
        print("Победили нолики!!!!")
        break