def if_checker(user_input):
    if user_input == 'red':
        print('зупинитися')
    elif user_input == 'yellow':
        print('очикувати або підготоватися відповідно до навчальної моделі')
    elif user_input == 'green':
        print('рух дозволенно за умовами безпеки')
    else:
        print('невідомий сігнал')

def match_checker(user_input):
    match user_input:
        case 'red':
            print('зупинитися')
        case 'yellow':
            print('очикувати або підготоватися відповідно до навчальної моделі')
        case 'green':
            print('рух дозволенно за умовами безпеки')
        case _:
            print('невідомий сігнал')


user_input = input("-> ")

if_checker(user_input)
print('='*30)
match_checker(user_input)



