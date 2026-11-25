def deflaut_rectangle(h, w):
    string = "*" * int(w)
    for _ in range(0, int(h)):
        print(string)


# Я не зрозумів як має виглядати трикутник, якщо висота не дорівнює ширині. Так що тільки висота
def triangle(h):
    for num in range(1, (int(h)+1)):
        print('*' * num)


def inverted_triangle(h):
    for num in range(int(h), 0, -1):
        print("*" * num)


def square_bagle(h, w):
    string = '*' * int(w)
    print(string)
    for _ in range(0, (int(h)-2)):
        print(f"*{' '*(int(w)-2)}*")

    print(string)   


deflaut_rectangle(6, 4)
print("="*30)

triangle(4)
print("="*30)

inverted_triangle(2)
print("="*30)

square_bagle('7', '5')
