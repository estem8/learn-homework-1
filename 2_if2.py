"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def checker(input_a, input_b):
    if not isinstance(input_a, str) or not isinstance(input_b, str):
      return 0    
    if input_a == input_b:
      return 1
    if input_a != input_b and len(input_a) > len(input_b):
      return 2
    if input_a != input_b and input_b == 'learn':
      return 3


def main():
    print(checker(1,'text'))
    print(checker('text','text'))
    print(checker('text-1','text'))
    print(checker('text','learn'))
    
    
if __name__ == "__main__":
    main()