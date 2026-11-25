def deflaut_rectangle(h, w):
    string = "*" * int(w)
    for _ in range(0, h):
        print(string)


# Я не зрозумів як має виглядати трикутник, якщо висота не дорівнює ширині. Так що тільки висота
def triangle(h):
    for num in range(1, (h+1)):
        print('*' * num)


def inverted_triangle(h):
    for num in range((h), 0, -1):
        print("*" * num)


def square_bagle(h, w):
    string = '*' * w
    print(string)
    for _ in range(0, (h-2)):
        print(f"*{' '*(w-2)}*")

    print(string)   


deflaut_rectangle(6, 4)
print("="*30)

triangle(4)
print("="*30)

inverted_triangle(2)
print("="*30)

square_bagle(8, 5)
