def get_input_parameters():
    original_list = [1, 4, -3, 0, 10]
    return original_list

def display_result(sorted_list):
    print('отсортированный список:', sorted_list)

def sort_list(original_list):
  for j in range(len(original_list) - 1):
    for i in range(len(original_list) - 1 - j):
      if original_list[i] > original_list[i+1]:
        original_list[i],original_list[i+1]=original_list[i+1],original_list[i]
  return original_list

if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
