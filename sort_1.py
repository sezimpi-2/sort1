from random import randint as generator

def bubble_sort(lst):
    length = len(lst)
    for num in range(length - 1):
        for i in range(length - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def binary_search(find_obj, lst):
    pos = 0
    resultOK = False
    first = 0
    last = len(lst) - 1
    while first <= last:
        middle = (first + last) // 2
        if lst[middle] == find_obj:
            first = middle
            last = first - 1
            resultOK = True
            pos = middle
        elif find_obj > lst[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if resultOK:
        print("Элемент найден в позиции ", pos)
    else:
        print("Элемент не найден (")


my_list = []
for num in range(11):
    my_list.append(generator(0, 101))
print("Неотсортированный список: ", my_list)
sorted_list = bubble_sort(my_list)
print("Отсортированный список:", sorted_list)
search = int(input("Ваш объект поиска: "))
binary_search(search, sorted_list)