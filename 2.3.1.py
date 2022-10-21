############################################################################################
# Напишите программу, в которой создай две переменные name, surname. Первой переменной присвой 
# значение 'Александр', а второй значение 'Пушкин'. Выведи значения этих переменных на разных строках.
# Sample Input:
# Sample Output:   Александр
#                  Пушкин
#############################################################################################

name = 'Александр'
print(name)
surname = 'Пушкин'
print(surname)

#################################

name = 'Александр'
surname = 'Пушкин'
print(name)
print(surname)

####################################

name,surname = 'Александр', 'Пушкин'
print(name)
print(surname)

#####################################

name, surname = "Александр", "Пушкин"
print(name, surname, sep = "\n")

#####################################

name, surname = 'Александр Пушкин'.split()
print(name, surname, sep='\n')

#####################################################

print(name:='Александр', surname:='Пушкин', sep='\n')

#####################################################

print(f'Александр\nПушкин')