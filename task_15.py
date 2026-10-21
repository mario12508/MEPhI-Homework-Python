from io import StringIO


def count_lines(stream):
    return sum(1 for _ in stream)


print(count_lines(StringIO("first\nsecond\nthird")))

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("first\nsecond\nthird\n")

with open("data.txt", encoding="utf-8") as f:
    print(count_lines(f))
