import csv
import io
from datetime import datetime

def csv_handler(read_file, id):
    read_file = io.TextIOWrapper(read_file, encoding='utf-8')
    reader = csv.reader(read_file)
    data = {}
    row1 = next(reader)
    date_to = datetime.strptime('1900-01-01 01:01:01.000001', '%Y-%m-%d %H:%M:%S.%f')
    date_from = datetime.strptime('3001-01-01 01:01:01.000001', '%Y-%m-%d %H:%M:%S.%f')
    # создание словаря с общей потраченной суммой каждого пользователя, а также со множеством купленных камней
    for row in reader:
        if row[0] not in data:
            data[row[0]] = {
                'spent_money': 0,
                'gems': set()
            }
        data[row[0]]['spent_money'] += int(row[2])
        data[row[0]]['gems'].add(row[1])
        d = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f')
        date_from = d if d < date_from else date_from
        date_to = d if d > date_to else date_to
    # создание и сорторвка по потраченным средтвам списка из кортежей
    # для поиска 5 клиентов, потративших максимальные суммы
    maximum = [(data[i]['spent_money'], i) for i in data]
    maximum = sorted(maximum, reverse=True)[:5]

    # создание словаря с подсчетом кол-ва клиентов из выбранных 5, которые купили определенный камень
    gems = {}
    for i in maximum:
        for j in data[i[1]]['gems']:
            if j not in gems:
                gems[j] = 0
            gems[j] += 1

    # формирование и сохранение окончательного результата в файл
    with open('files/csv_files/deals_' + str(id)+'.csv', mode='w', encoding='utf-8') as w:
        file_writer = csv.writer(w, delimiter=',', lineterminator='\r')
        file_writer.writerow(['username', 'spent_money', 'gems'])
        for i in maximum:
            customer_gems = []
            for j in data[i[1]]['gems']:
                if gems[j] > 1:
                    customer_gems.append(j)
            file_writer.writerow([i[1], i[0], ' '.join(customer_gems)])
    return ('csv_files/deals_' + str(id)+'.csv', date_from, date_to)
