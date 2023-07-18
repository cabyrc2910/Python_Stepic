####################################################################################################
### Приглашение
# Напишите программу, которая будет выводить приглашение.
# Входные данные: С клавиатуры вводится три строки: Имя - Иванов Иван
#                                                   Событие - юбилей
# Выходные данные:                                  Место - ДК Агрегатный
# Выводится 2 строки, все пробелы и знаки препинания должны стоять как в примере:
# Дорогой {Имя} !
# Приглашаем вас на {Событие} , который состоится в {Место} !
####################################################################################################

text_1 = input()
text_2 = input()
text_3 = input()
print('Дорогой', text_1, '!')
print('Приглашаем вас на', text_2, ', который состоится в', text_3,  '!')

#################################################

a,b,c = input(),input(),input()
print('Дорогой', a,'!')
print('Приглашаем вас на', b, ',' ,'который состоится в', c, '!')

##################################################

a,b,c = input(),input(),input()
print(f"Дорогой {a } !\nПриглашаем вас на {b} , который состоится {c} !") # '\n' - перенос строки

#################################################

lst = [input() for _ in range(3)]    # Списки позволяют использовать ломтик обозначение , как lst[start:end:step]
print(f'Дорогой {lst[0]} !\nПриглашаем вас на {lst[1]} , который состоится в {lst[2]} !')

##################################################

print(f'''Дорогой {input()} !
Приглашаем вас на {input()} , который состоится {input()} !''')

#################################################

print(f'Дорогой {input()} !\nПриглашаем вас на {input()} , который состоится {input()} !')



