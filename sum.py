def sum_fun(s=None, d=None, launch_number=1, prev=None, flag=False):
    prev = prev or list()
    if flag:
        print(f'Запуск №: {launch_number}\n{"Аргумент не передан" if d is None else "Переданный аргумент: " + str(d)}\n'
              f'Значение суммы: {s}\nВсе предыдущие аргументы и суммы: {prev}\n----------------------------------')
        prev.append((d, s))
        return lambda num=None: sum_fun(s, num, launch_number + 1, prev, True) if num is None \
            else sum_fun(num + s, num, launch_number + 1, prev, True)
    else:
        print(f'Запуск №: {launch_number}\n{"Аргумент не передан" if s is None else "Переданный аргумент: " + str(s)}\n'
              f'Значение суммы: {s or 0}\nВсе предыдущие аргументы и суммы: {prev}\n----------------------------------')
        prev.append((s, s or 0))
        return lambda num=None: sum_fun(num if s is None else num + s, num, launch_number + 1, prev,
                                        False if s is None else True)


sum_fun()()(1)(7)(3)(100)(-45)()(0)
