def get_input_parameters():
    word = input('Введите слово: ')
    return word


def display_result(is_palindrome):
    print('Является палиндромом:', is_palindrome)


def check_palindrome(word):
    wordRev = ''
    flag = False
    for letter in word:
        wordRev = letter + wordRev

    if word == wordRev:
        flag = True

    return flag


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
