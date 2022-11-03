####################################################################################################
# Приглашение
# Напишите программу, которая будет выводить приглашение.
# Входные данные: С клавиатуры вводится три строки: Имя
#                                                   Событие
# Выходные данные:                                  Место
# Выводится 2 строки, все пробелы и знаки препинания должны стоять как в примере:
# Дорогой {Имя} !
# Приглашаем вас на {Событие} , который состоится в {Место} !
# Sample Input: Иванов Иван
#               юбилей
#               ДК Агрегатный
# Sample Output: 
# Дорогой Иванов Иван !
# Приглашаем вас на юбилей , который состоится в ДК Агрегатный !
####################################################################################################

text_1 = input()
text_2 = input()
text_3 = input()
print('Дорогой', text_1, '!')
print('Приглашаем вас на', text_2, ', который состоится в', text_3,  '!')

#################################################

text_1 = input()
text_2 =input()
text_3 = input()
print(f"Дорогой, {text_1 } !\nПриглашаем вас на {text_2} , который состоится {text_3} !")

##################################################

a,b,c = input(),input(),input()
print('Дорогой', a,'!')
print('Приглашаем вас на', b ,', который состоится' , c,'!')

#################################################

print(f'Дорогой, {input()} !\nПриглашаем вас на {input()} , который состоится {input()} !')

##################################################

print(f'''Дорогой, {input()} !
Приглашаем вас на {input()} , который состоится {input()} !''')

#################################################

lst = [input() for _ in range(3)]
print(f'Дорогой {lst[0]} !\nПриглашаем вас на {lst[1]} , который состоится в {lst[2]} !')



