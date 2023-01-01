def display_result(participants_names):
    print('Первый день:', participants_names)


def get_participants_names(names):
    evenNames = []
    for i,char in enumerate(names):
        if i % 2 == 0:
            evenNames.append(char)
    return evenNames


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_participants_names и display_result
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
