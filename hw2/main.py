# Домашнее задание

#1. Создать 3 переменных с одинаковыми данными с одинаковыми идентификаторами
a = 'kirill'
b = 'kirill'
c = 'kirill'

print('a', id(a))
print('b', id(b))
print('c', id(c))

#2. Создать 2 перменных с одинаковыми данными с разными идентификаторами
a1 = ['kir']
b1 = ['kir']

print('a1', id(a1))
print('b1', id(b1))


#3. *Поменять их типы так, чтобы у 1х трех были разные идентификаторы,
# а у 2х последних были одинаковые
a = list(a)
b = list(b)
c = list(c)
print('new a', id(a))
print('new b', id(b))
print('new c', id(c))

a1 = bool(a1)
b1 = bool(b1)
print('new a1', id(a1))
print('new b1', id(b1))
