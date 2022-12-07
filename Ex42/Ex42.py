# 2 - Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import random
def Input_int(input_string):
    '''
    Ввод числа с пояснением
    '''
    while True:
        try:
            num=int(input(input_string))
            return num
        except ValueError:
            print('Введено не число. Давайте попробуем еще раз')

def Random_list (length_list, down_border, up_border):
    '''
    Задаем список случайных целых чисел в диапазоне между down_border и up_border
    длиной length_list
    '''
    rand_list=[]
    for i in range(0,length_list):
        rand_list.append(random.randint(down_border,up_border))
    return rand_list

def Non_repeating_elements(repeating_list):
    '''
    Ищем уникальные элементы в списке repeating_list результат помещаем в список unique_list
    '''
    unique_list=[]
    for item in repeating_list:
        item_exist = False
        for x in unique_list:
            if x == item: 
                item_exist = True
                break 
        if not item_exist:
            unique_list.append(item)
    return unique_list

print()
number=Input_int('Введите число элементов в последовательности (целое положительное число): ')
source_list=Random_list (number, 0, 5) 
print('Исходный список')
print(source_list)
non_repeating_list=Non_repeating_elements(source_list)
non_repeating_list.sort()
print('Список неповторяющихся элементов')
print(non_repeating_list)
