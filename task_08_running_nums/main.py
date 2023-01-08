def get_input_parameters():
    shift = int(input('Сдвиг: '))
    # number = int(input('Количество элементов в списке: '))
    original_list = [1, 4, -3, 0, 10]
    # print('Вводите элементы:')
    # for num in range(number):
    #     num = int(input())
    #     original_list.append(num)
    # print('Изначальный список:', original_list)
    return shift, original_list

def display_result(shifted_list):
    print('Сдвинутый список:', shifted_list)


def shift_list(shift, original_list):
    count = len(original_list)
    shifted_list = []
    for i, num in enumerate(original_list):
        if i >= count - shift:
            shifted_list.append(num)
    for i, num in enumerate(original_list):
        if i < count - shift:
            shifted_list.append(num)
    return shifted_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
