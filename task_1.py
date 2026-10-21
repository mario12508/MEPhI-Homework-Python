with open(input("Введите расположение файла: "), encoding='utf-8') as f:
    strs = 0
    words = 0
    symbols = 0
    maxi = 0
    for line in f:
        strs += 1
        words += len(line.split())
        symbols += len(line.rstrip('\n'))
        maxi = max(maxi, len(line))

print('Всего строк: ', strs)
print('Всего слов: ', words)
print('Всего символов: ', symbols)
print('Длина наибольшей строки: ', maxi)
