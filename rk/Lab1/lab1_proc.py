import sys
import math

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0 and -b / (2.0*a) > 0:
        root1 = math.sqrt(-b / (2.0*a))
        root2 = - root1
        result.append(root1)
        result.append(root2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        temp1 = (-b + sqD) / (2.0*a)
        temp2 = (-b - sqD) / (2.0*a)
        if temp1 > 0:
            result.append(math.sqrt(temp1))
            result.append(-math.sqrt(temp1))
        if temp2 > 0:
            result.append(math.sqrt(temp2))
            result.append(-math.sqrt(temp2))
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# roots_proc.py 1 0 -4