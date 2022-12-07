#Дешифровка сообщения методом Цезаря

def cesar (message_def, lang_list_def, action_def, smeshenie_def:int):
    '''
    Шифрование/дешифрование методом Цезаря.
    Аргументы: 
    message_def - исходное сообщение
    lang_list_def - текстовая переменная необходимого алфавита
    action_def - действие, которое надо производить (1-шифровка, -1 - дешифровка)
    smeshenie_def - смещение в алфавите
    результат:
    itog - текстовая переменная

    '''
    itog=''
    new_mesto=0
    for i in message_def:
        mesto = lang_list_def.find(i)       
        if action_def==1:   
            new_mesto = mesto - smeshenie_def
        else: 
            new_mesto = mesto + smeshenie_def    
        if i in lang_list_def:
            itog += lang_list_def[new_mesto]
        else:
            itog += i
    return itog

#Определяем алфавиты
alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

print()
lang = int(input('Выберите язык 1-русский/2-английский: '))
lang_list=[]
if lang==1:
    lang_list=alfavit_RU
else:
    lang_list=alfavit_EU
action= int(input('Что нужно сделать? 1-зашифровать/2-дешифровать: '))
if action==2:
    action=-1  
smeshenie = int(input('Шаг шифровки/дешифровки (целое число): '))
message = input("Сообщение для шифровки/дешифровки: ").upper()
resalt = cesar (message, lang_list, action, smeshenie )
print()
print ('Результат шифрования/дешифрования: ',resalt) 

with open('C:/Users/S9057/Desktop/PYTHON/PHW4/Ex44/resalt.txt','w', encoding='utf-8') as resalt_text:
    resalt_text.write(resalt)