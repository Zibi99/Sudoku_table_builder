import random


def wylosuj_1_liczbe(lista_do_losowania, lista_wykluczonych):
    lista_wykluczonych = sorted(lista_wykluczonych)
    lista_do_losowania = sorted(lista_do_losowania)

    # czyszczę duplikaty w liście wykluczonych
    [lista_wykluczonych.remove(x) for x in lista_wykluczonych.copy() if lista_wykluczonych.copy().count(x) > 1]

    # usuwam wykluczone - muszę dać, ze to kopia, bo inaczej od razu zmienia samą listę
    [lista_do_losowania.remove(x) for x in lista_do_losowania.copy() if x in lista_wykluczonych]

    try:
        return random.choice(lista_do_losowania)
    except:
        return "0"

print(wylosuj_1_liczbe([1,2,4,5,3],[2,1,1]))