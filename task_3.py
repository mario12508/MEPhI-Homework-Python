import csv


with open('students.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',', quotechar="'")
    data = list(reader)
    groups = dict()
    maxi = 0
    max_stud = ""
    sumn = 0
    for stud in data:
        if stud['group'] in groups:
            groups[stud['group']][0] += int(stud['score'])
            groups[stud['group']][1] += 1
        else:
            groups[stud['group']] = [0, 0]
            groups[stud['group']][0] = int(stud['score'])
            groups[stud['group']][1] = 1
        sumn += int(stud['score'])
        if maxi < int(stud['score']):
            maxi = int(stud['score'])
            max_stud = stud['name']
    print('Средний балл всех студентов: ', sumn / len(data))
    print('Студент с максимальным баллом: ', max_stud, maxi)
    print('Средний балл каждой группы:')
    for g in groups.items():
        print(f"\tСредний балл группы {g[0]}: {g[1][0] / g[1][1]}")
