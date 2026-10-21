with open(input("Введите название csv с товарами: "), encoding='utf-8') as csv_file:
    reader = csv_file.readlines()
    with open("expensive.csv", 'w', encoding='utf-8') as new_f:
        for indx, line in enumerate(reader):
            if indx == 0:
                new_f.write(line)
                continue
            if int(line.split(',')[2]) >= 100:
                new_f.write(line)
    new_f.close()
