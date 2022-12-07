# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol

from os import path
from itertools import groupby

def text_compression():
    with open('C:/Users/S9057/Desktop/PYTHON/PHW4/Ex45/source_text.txt','r', encoding='utf-8') as sourse_text:
        with open('C:/Users/S9057/Desktop/PYTHON/PHW4/Ex45/archived_text.txt','w', encoding='utf-8') as archived_text:    
            sourse_list=list(sourse_text.readline())
            result=[]
            for i,j in groupby(sourse_list):
                result.append(str(len(list(j))))
                result.append(i)
                result_string=''
            for i in result:
                if i!='1': 
                    result_string +=i
            archived_text.write(result_string)
            print(result_string)        
    return print('Сжатие завершено. Результат в файле archived_text.txt')

def text_decompression():
    with open('C:/Users/S9057/Desktop/PYTHON/PHW4/Ex45/archived_text.txt','r', encoding='utf-8') as archived_text:
        with open('C:/Users/S9057/Desktop/PYTHON/PHW4/Ex45/restored_text.txt','w', encoding='utf-8') as restored_text:      
            archived_list=list(archived_text.readline())    
            temporary_lst=['']
            k=0
            for i in range(len(archived_list)):
                if archived_list[i].isdigit():
                    temporary_lst[k]+=archived_list[i]
                else:
                    temporary_lst.append(archived_list[i])
                    temporary_lst.append('')
                    if temporary_lst[k]=='':
                        temporary_lst[k]='1'
                    restored_text.write(f'{int(temporary_lst[k])*temporary_lst[k+1]}')
                    k+=2
    return print('Восстановление завершено. Результат в файле restored_text.txt')                

print()
print('Запишите сжимаемый текст в файл sourse_text.txt')
ready=input('Готово? Для начала сжатия нажмите Enter')
text_compression()
ready=input('Для начала восстановления нажмите Enter')
text_decompression()


