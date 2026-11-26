from decimal import Decimal

def composition_of_amount(input_amount: str):
    amount = input_amount.replace(',', '.')
    amount = Decimal(amount)
    composition = {
        'banknotes': {
            '500': None,
            '200': None,
            '100': None,
            '50': None,
            '20': None,
            '10': None,
            '5': None
        },
        'coins': {
            '2': None,
            '1': None,
            '0.5': None,
            '0.2': None,
            '0.1': None,
            '0.05': None,
            '0.02': None,
            '0.01': None
        }
    }

    min_banknote = int(min(composition['banknotes'].keys(), key= lambda x: int(x)))

    if amount >= min_banknote:
        banknotes = composition['banknotes']
        for nominal in banknotes.keys():
            while amount >= int(nominal): 
                amount -= int(nominal)
                banknotes[nominal] = increase_nominal_counter(banknotes[nominal])

            if int(nominal) < min_banknote:
                break
            

    if amount > 0:
        coins = composition['coins']
        for nominal in coins.keys():
            nominal = Decimal(nominal)
            while amount >= nominal: 
                amount -= nominal
                coins[str(nominal)] = increase_nominal_counter(coins[str(nominal)])

            if nominal == 0:
                break

    composition["banknotes"] = dict(filter(lambda item: item[1] is not None, composition['banknotes'].items()))
    composition['coins'] = dict(filter(lambda item: item[1] is not None, composition['coins'].items()))

    return composition
            
                
def increase_nominal_counter(count):
    if count is None:
        return 1
    else:
       count += 1  
       return count        


def print_composition(composition):
    if composition["banknotes"]:
        for key, value in composition["banknotes"].items():
            print(f"{value} X {key}")

    if composition["coins"]:
        for key, value in composition["coins"].items():
            print(f"{value} X {key}")       


def start_program():
    user_amount = input('Введіть суму: ')
    composition = composition_of_amount(user_amount)

    if composition['banknotes']:
        print(f"Кількість банкнот: {sum(composition['banknotes'].values())}")

    if composition['coins']:
        print(f"Кількість монет: {sum(composition['coins'].values())}")

    print('-'*30)
    print("Склад суми:")    
    print_composition(composition)


start_program()
