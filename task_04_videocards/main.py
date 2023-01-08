def get_input_parameters():
    count = int(input('Количество видеокарт: '))
    print()
    modelList = []
    for i in range(count):
        print(i + 1, 'Видеокарта:', end =' ')
        model = int(input())
        modelList.append(model)
    return modelList


def display_result(old_video_cards, new_video_cards):
    print('Старый список видеокарт:', old_video_cards)
    print('Новый список видеокарт:', new_video_cards)


def select_video_cards(video_cards):
    max = 0
    for model in (video_cards):
        if model >= max:
            max = model

    new_modelList = []

    for i in (video_cards):
        if i != max:
            new_modelList.append(i)
    return new_modelList


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
