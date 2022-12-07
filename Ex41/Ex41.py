# 1 - Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

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

def Prime_factors_number (num:int):
    '''
    Поиск простых множителей числа num вывод в список prime_factors 
    '''
    prime_factors=[]
    for i in range(2, num+1):
        if(num%i==0):
            count=1
            for j in range(2,(i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):    
                #print(i)
                prime_factors.append(i)
    return prime_factors

print()
number=Input_int('Введите целое положительное число): ')
prime_factors_num=[]
prime_factors_num=Prime_factors_number (number)
print(f'Простые множители числа',number)
print(prime_factors_num)

