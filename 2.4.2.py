####################################################################################################
# Повторение х 3
# Напишите программу, которая считывает 3 строки с клавиатуры, а затем выводит их в том же порядке.
# Входные данные: Вводится три строки.
# Выходные данные: Выводится три строки.
# Sample Input 1: ау                 Sample Output 1: ау
#                 ты                                  ты
#                 кто                                 кто
####################################################################################################

text1 = input()
text2 = input()
text3 = input()
print(text1)
print(text2)
print(text3)

##################################################

print(input())
print(input())
print(input())

#################################################

text_1 = input();  text_2 = input();  text_3 = input()
print(text_1, text_2, text_3, sep = '\n')

####################################################

text1, text2, text3 = str(input()), str(input()), str(input())
print(text1, text2, text3, sep = '\n')

##################################################

print(input(), input(), input(), sep = '\n')

#################################################

print(*[input() for _ in range(3)], sep = '\n')

#################################################

print(f'{input()}\n{input()}\n{input()}')

#################################################

a = input()  #  = это оператор присваивания
b = input()
c = input()
print(a, b, c, sep='\n')  #  необязательный параметр sep команды print() позволяет 
     #  установить строку, с помощью которой будут разделены аргументы при печати.
##########################################

a, b, c = input(), input(), input()
print(a, b, c, sep="\n")          # sep=' ' пробел,  end='\n' # перевод строки

############################################

a,b,c = input(), input(), input()
print(f'{a}\n{b}\n{c}')

#############################################

[print(input()) for _ in "abc"]

##############################################

[print(input()) for _ in range(3)]

#############################################

for i in range(3):print(input())

#############################################

def a():
    print(input())
    print(input())
    print(input())
a()

#############################################

def func():
    x,y,z = input(),input(),input()
    return x,y,z
print(*func(),sep="\n")



