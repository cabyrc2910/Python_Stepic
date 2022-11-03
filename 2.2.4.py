####################################################################################################
### Текст лесенкой
# Напишите программу выводящую текст лесенкой.
# Входные данные: 
# Выходные данные:  Выводится 5 строк.
# Hello                 
# Hello Hello
# Hello Hello Hello             
# Hello Hello Hello Hello             
# Hello Hello Hello Hello Hello
####################################################################################################

print('Hello')
print('Hello Hello')
print('Hello Hello Hello')
print('Hello Hello Hello Hello')
print('Hello Hello Hello Hello Hello')

##################################################

print("""Hello
Hello Hello
Hello Hello Hello
Hello Hello Hello Hello
Hello Hello Hello Hello Hello""")

##################################################

print('Hello')
print('Hello ' * 2)
print('Hello ' * 3)
print('Hello ' * 4)
print('Hello ' * 5)

##################################################

s = 'Hello'
print(*[s])
print(*[s] * 2)
print(*[s] * 3)
print(*[s] * 4)
print(*[s] * 5)

##################################################

for i in range(1,6):
    print('Hello '*(i-1)+'Hello')

##################################################

for i in range(5):
    print('Hello ' * i + 'Hello')

##################################################

[print('Hello '*(i+1)) for i in range(5)]

##################################################

print(*['Hello ' * i for i in range(1, 6)], sep='\n')

##################################################

[print("Hello " * i) for i in [1, 2, 3, 4, 5]]




