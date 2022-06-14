def hello():
    print(' Приветствуем')
    print('    в игре   ')
    print('крестики-нолики')


def matrix():
    print(f'  0 1 2')
    print(f'0 {field[0][0]} {field[0][1]} {field[0][2]}')
    print(f'1 {field[1][0]} {field[1][1]} {field[1][2]}')
    print(f'2 {field[2][0]} {field[2][1]} {field[2][2]}')


def move():
    while True:
        cords = input('Ваш ход:').split()
        if len(cords) != 2:
            print('Введите 2 координаты')
            continue
        a, b = cords
        if not (a.isdigit()) or not (b.isdigit()):
            print('Введите числа')
            continue
        a, b = int(a), int(b)
        if 0 > a or a > 2 or 0 > b or b > 2:
            print('Координаты вне диапазона')
            continue
        if field[a][b] != ' ':
            print('Клетка занята')
            continue
        return a, b


def win_check():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for comb in win_comb:
        symb = []
        for i in comb:
            symb.append(field[i[0]][i[1]])
        if symb == ['X', 'X', 'X']:
            print('Поздравляем! выиграл X')
            return True
        if symb == ['0', '0', '0']:
            print('Поздравляем! выиграл 0')
            return True
    return False


hello()
field = [[' '] * 3 for i in range(3)]
numb = 0
while True:
    numb += 1
    matrix()
    if numb % 2 == 1:
        print('Ходит крестик:')
    else:
        print('Ходит нолик:')
    x, y = move()
    if numb % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'
    if win_check():
        break

    if numb == 9:
        print('Ничья!')
        break
