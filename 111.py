import requests

a1 = {}


class Pokemon:
    def __init__(self, name):
        if name in a1:
            print(f'''{name}
abilities: {a1[name]['abilities']}
base_experience: {a1[name]['base_experience']}
forms: {a1[name]['forms']}''')
        else:
            a = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
            if not a:
                print('Нет такого')
            else:
                a1[name] = {'abilities': a.json()['abilities'][0]['ability']['name'],
                            'base_experience': a.json()['base_experience'],
                            'forms': a.json()['forms'][0]['name']}
                print(f'''{name}
abilities: {a1[name]['abilities']}
base_experience: {a1[name]['base_experience']}
forms: {a1[name]['forms']}''')


while True:
    a = input('Введите имя покемона: ')
    Pokemon(a)
