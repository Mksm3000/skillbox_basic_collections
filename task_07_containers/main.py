def get_input_parameters():
    count = int(input('Количество контейнеров: '))
    print()
    list_container_weights = []
    for num in range(count):
        print('Введите вес контейнера:', end = ' ')
        weight = int(input())
        list_container_weights.append(weight)

    new_container_weight = int(input('\nВведите вес нового контейнера: '))

    return list_container_weights, new_container_weight


def display_result(serial_number_new_container):
    print('Номер, который получит новый контейнер:', serial_number_new_container)


def search_serial_number_new_container(list_container_weights, new_container_weight):
    serial_number_new_container = 0
    for i, char in enumerate(list_container_weights):
        if char < new_container_weight:
            serial_number_new_container = i + 1
            break
    return serial_number_new_container

if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
