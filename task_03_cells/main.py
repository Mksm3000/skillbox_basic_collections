def get_input_parameters():
    count = int(input('Количество клеток: '))
    print()
    param_cells = []
    for i in range(count):
        print('Эффективность', i + 1, 'клетки:', end = ' ')
        param = int(input())
        param_cells.append(param)
    return param_cells

def display_result(cells):
    print('\nНеподходящие значения:', end = ' ')
    for i in (cells):
        print(i, end = ' ')


def select_cells(cells):
    spisok = []
    for i,char in enumerate(cells):
        if char < i:
            spisok.append(char)
    return spisok


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
