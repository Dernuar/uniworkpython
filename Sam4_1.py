from datetime import datetime # импортирует datetime
from math import sqrt # импортирует sqrt

def main(**kwargs): # задается функция main()
    for key in kwargs.items(): # задается цикл
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) # задается значение переменной result 
        print(result) # выводится переменная result

if __name__ == '__main__': # задается условие которое выполняется при вызове main() напрямую
    start_time = datetime.now() # задается переменная start_time которая является датой на момент запуска программы
    main( 
        one = [10, 3],
        two = [5, 4],
        three = [15, 13],
        four = [93, 53],
        five = [133, 15],
    ) # вызов функции main() в которой задается значения 5 спискам
    time_costs = datetime.now() - start_time # задается переменная time_costs которая является результатом вычитания из даты на данный момент переменной start_time
    print(f'Время выполнения программы: {time_costs}') # выводится значение time_costs являеющееся временем затраченным на выполнения программы