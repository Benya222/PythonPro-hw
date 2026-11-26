def valid_username(username: str):
    starts_with_int = username[0].isdecimal()
    valid_len = len(username) >= 5
    has_spaces = ' ' in username

    if not starts_with_int and valid_len and not has_spaces:
        return True

    errors_explain = []

    if starts_with_int:
        errors_explain.append("Ім'я не може починатися з цифри")

    if not valid_len:
        errors_explain.append("ім'я повинно мати хоча б п'ять символів")

    if has_spaces:
        errors_explain.append("ім'я не повинно мати пробіли")


    
    return ", ".join(errors_explain)

def valid_email(email: str):
    return True if email.count("@") == 1 in email else "Електронна адреса повинна мати один символ '@'"

def valid_age(age: str):
    if age.isdecimal():
        return True if int(age) >= 16 else 'Вік має бути не менше 16'

    return  "Вік повинен складатися лише з цифр"


def valid_pass(password: str):
    valid_len = len(password) >= 8
    has_spaces = ' ' in password
    unique_chars = len(password) == len(set(password))

    if valid_len and not has_spaces and unique_chars:
        return True

    errors_explain = []

    if not valid_len:
        errors_explain.append('Пароль повинен мати хоча б 8 символів')

    if has_spaces:
        errors_explain.append('пароль не повинен мати пробіли')

    if not unique_chars:
        errors_explain.append('пароль не може складатись з одного й того ж символа')

    return ", ".join(errors_explain)            


def start_program():
    username = input("Им'я: ")
    email = input("Електронная адреса: ")
    age = input("Вік: ")
    password = input('Пароль: ')

    print("------ Перевірка --------------")
    print(f"Им'я: {valid_username(username)}")
    print(f"Електронная адреса: {valid_email(email)}")
    print(f"Вік: {valid_age(age)}")
    print(f"Пароль: {valid_pass(password)}")



start_program()

