import re
import turtle

print('\n\nСмайлик:')
print('*','','','*','','','','','','','','','','*','*','','','','*')
print('','*','*','','','','','','','','','','','*','','','','','','','*')
print('','','*','','','*','*','*','','*','*','','','','','','','','*')
print('','*','*','','','','','','','','','','','*','','','','','','','','','*')
print('*','','','*','','','','','','','','','','*','*','','','','','','','','*')

turtle.right(60)
turtle.forward(100)
turtle.left(180)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.left(180)
turtle.forward(100)
turtle.left(180)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(20)
turtle.left(180)
turtle.forward(20)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(20)
turtle.right(60)
turtle.forward(120)
turtle.exitonclick()

test_1 = 'dfsffX-{\ehfhfefhefhhhuhhefhuehfheX-{\deffefX-}'
test_2 = 'dfsffX-{\ehfhfefhefhhhuhhefhuX-{\X-{\X-{\X-{\X-{\X-{\ehfheX-{\deffefX-}'
test_3 = 'dfsffX-{\ehfhfefhefhhhuhheX-{\X-{\hhuehfheX-{\deffefX-}'
test_4 = 'dfsffX-{\ehfhfefhefhhhuhX-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\hefhuehfheX-{\deffefX-}'
test_5 = 'dererX-{\sX-{\ehfhfefhefhhX-{\X-{\X-{\X-{\X-{\X-{\X-{\X-{\huhhefhuehfheX-{\deffefX-}'

print('\n\nПервое задание:\n')
print('Строка:',test_1)
print('Число вхождений:',len(re.findall(r"X\-\{\\", test_1)))
print('\nСтрока:',test_2)
print('Число вхождений:',len(re.findall(r"X\-\{\\", test_2)))
print('\nСтрока:',test_3)
print('Число вхождений:',len(re.findall(r"X\-\{\\", test_3)))
print('\nСтрока:',test_4)
print('Число вхождений:',len(re.findall(r"X\-\{\\", test_4)))
print('\nСтрока:',test_5)
print('Число вхождений:',len(re.findall(r"X\-\{\\", test_5)))

print('\n\nВторое задание:\n')
test_6 ='А ты знал, что ВТ – лучшая кафедра ИТМО?'
print('Строка:',test_6)
print('Ответ:',re.findall(r"(ВТ{1}[\s[\w\–]{0,}]{0,4}\sИТМО)", test_6))
test_7 ='ВТ – любовь к ИТМО'
print('\nСтрока:',test_7)
print('Ответ:',re.findall(r"(ВТ{1}[\s[\w\–]{0,}]{0,4}\sИТМО)", test_7))
test_8 ='оказывается ВТ – одна из самых в ИТМО'
print('\nСтрока:',test_8)
print('Ответ:',re.findall(r"(ВТ{1}[\s[\w\–]{0,}]{0,4}\sИТМО)", test_8))
test_9 ='ВТ – сложная штука в ИТМО'
print('\nСтрока:',test_9)
print('Ответ:',re.findall(r"(ВТ{1}[\s[\w\–]{0,}]{0,4}\sИТМО)", test_9))
test_10 ='ВТ – загадка ИТМО'
print('\nСтрока:',test_10)
print('Ответ:',re.findall(r"(ВТ{1}[\s[\w\–]{0,}]{0,4}\sИТМО)", test_10))

def cgange(st):
    s=''
    MATH = []
    data = re.findall(r"[-+]?\d+",st)
    math = re.findall(r"\D",st)
    for i in math:
        if i != ' ':
            MATH.append(i)
    MATH.append("")
    DATA = list(map(int,data))
    for i in range(len(DATA)):
        DATA[i] = 3*DATA[i]**2+5
        s = s + str(DATA[i]) + MATH[i]
    return s

test_11 = '20 + 22 = 42'
test_12 = '222 + 333 = 555'
test_13 = '1111 + 2222 = 3333'
test_14 = '44444 + 55555 = 99999'
test_15 = '666666 + 777777 = 1444443'
print('\n\nТретье задание:\n')
print('Выражение:',test_11)
print('Ответ:',cgange(test_11))
print('\nВыражение:',test_12)
print('Ответ:',cgange(test_12))
print('\nВыражение:',test_13)
print('Ответ:',cgange(test_13))
print('\nВыражение:',test_14)
print('Ответ:',cgange(test_14))
print('\nВыражение:',test_15)
print('Ответ:',cgange(test_15))
