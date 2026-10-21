with open("numbers.txt", encoding='utf-8') as f:
    try:
        numbers = list(map(int, f.readlines()))
        mini = min(numbers)
        maxi = max(numbers)
        mean = sum(numbers) / len(numbers)
    except ValueError:
        print('Файл содержит не только числа или не по одному числу в строке')
        quit(1)
    except Exception as e:
        print(e)
        quit(1)

with open("result.txt", 'w', encoding='utf-8') as f:
    f.write(f"Минимум: {mini}\n")
    f.write(f"Максимум: {maxi}\n")
    f.write(f"Среднее арифметическое: {mean}")
f.close()
