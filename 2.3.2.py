############################################################################################
# Напишите программу, в которой создай две переменные text_1, text_2. Присвойте этим переменным такие значения, 
# чтобы при выполнении команды print(text_1, text_2) программа вывела на экран «Hello, world!» без кавычек.
# Sample Input:
# Sample Output:   Hello, world!
#############################################################################################

text_1 = 'Hello,'
text_2 = 'world!'
print(text_1, text_2)

#################################

text_1 = 'Hello, world!'
text_2 = ''
print(text_1, text_2)

##################################

name, surname = 'Hello', 'world'
print(name, surname, sep=', ', end='!')

####################################

text_1, text_2 = "Hello, world!".split()
print(text_1, text_2)

#####################################

[print(text_1,text_2) for [text_1,text_2] in [['Hello,','world!']]]


