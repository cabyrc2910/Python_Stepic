####################################################################################################
### Повторение х 3 на одной строке
# Напишите программу, которая считывает 3 строки с клавиатуры, а затем выводит их в том же порядке.
# Входные данные: С клавиатуры вводится три строки.
# Выходные данные: Выводится одна строка.
# Sample Input 1: ау      Sample Output 1:  ау ты кто
#                 ты
#                 кто
####################################################################################################

text1 = input()
text2 = input()
text3 = input()
print(text1,text2,text3)

##################################################

a = input(); b = input(); c = input()
print(a, b, c)

#################################################

print(input(), input(), input())

#################################################

a, b, c = [input()for i in range(3)]
print(a, b, c)

#################################################

print(input(), input(), input(), end=' ')
# end — это строка, которая добавляется после последнего значения. По умолчанию — это перенос на новую строку (\n). С помощью аргумента end программист может самостоятельно определить окончание

#################################################

# print(*[input() for _ in range(3)])

# #################################################

# print(*[input() for _ in '_'*3])

# #################################################

# text1, text2, text3 = str(input()), str(input()),str(input())
# print(text1, text2, text3)



