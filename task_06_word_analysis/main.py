def get_input_parameters():
    word = input('Введите слово: ')
    return word


def display_result(number_unique_letters):
    print('Количество уникальных букв в слове:', number_unique_letters)


def count_number_unique_letters(word):
    count = 0
    countDouble = 0
    for letter in word:
        for letterDouble in word:
            if letter == letterDouble:
                countDouble += 1
#                print(letter, countDouble)
        if countDouble < 2:
            count += 1
        countDouble = 0
    return count


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
