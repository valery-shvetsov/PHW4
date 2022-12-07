# 3 - В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:

# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

def names_highlighting (list_names:list, criteria: str) ->list:
    '''
    Анализируем список и символы элементов,
    в которых встречается строка criteria,
    переводим в верхний регистр (заглавные буквы)
    Аргументы: список list_names и строка criteria
    Результат: измененный list_names 

    '''
    for i in range(len(list_names)):
        if criteria in list_names[i]:
            list_names[i]=list_names[i].upper()
    return list_names

def list_from_file (file_name: str) ->list[str]:
    '''
    Из файла с именем file_namе получаем список с его содержимым
    Аргумент: название файла (file_name) задаем полный путь через /
    '''
    with open(file_name, encoding='utf-8') as file:
        return file.read().split('\n')

list_name_mark=list_from_file('C:/Users/S9057/Desktop/PYTHON\PHW4/Ex43/name_mark.txt')
list_name_mark=names_highlighting(list_name_mark,'5')

# перезаписываем файл с измененными именами
with open ('C:/Users/S9057/Desktop/PYTHON/PHW4/Ex43/name_mark.txt','w', encoding='utf-8') as data:
    for i in range(len(list_name_mark)):
        data.writelines(f'{list_name_mark[i]}\n')