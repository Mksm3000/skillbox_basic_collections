def get_input_parameters():
    number = int(input('Введите число (N >= 1): '))
    if number <= 0:
        print('Ошибка ввода. Попробуйте еще раз')
        get_input_parameters()
    else:
        return number


def display_result(odd_numbers):
    print('Список из нечётных чисел от одного до N:', odd_numbers)


def get_odd_numbers(number):
    spisok = []
    for i in range (number + 1):
        if i % 2 != 0:
            spisok.append(i)
    return spisok


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат
