def get_input_parameters():
    number = int(input('Сколько фильмов хотите добавить? '))
    new_favorite_films = []
    for film in range (number):
        print('Введите название фильма:', end = ' ')
        film = input('')
        new_favorite_films.append(film)
    return new_favorite_films


def display_result(favorite_films, errors):
    print()
    for err in errors:
        print('Ошибка: фильма', err, 'у нас нет: (')

    print('\nВаш список любимых фильмов:', end = ' ')
    print(*favorite_films, sep = ', ')


def add_favorite_film(new_favorite_films, available_films):
    favorite_films = []
    errors = []
    for new in new_favorite_films:
        if new in available_films:
            favorite_films.append(new)
        else:
            errors.append(new)
    return favorite_films, errors


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(new_favorite_films, available_films)  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
