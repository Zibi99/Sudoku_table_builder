import random
import time


def sprawdz_sume_w_linii(sprawdzana_lista):
    suma = 0
    for val in sprawdzana_lista:
        suma +=int(val)
    return "OK" if suma == 45 else "BŁĄD"

def sprawdz_powtorke(sprawdzana_lista):
    for x in sprawdzana_lista:
        if sprawdzana_lista.count(x) > 1:
            return "-"
        else:
            return "1"



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

def linia_pionowa(lista_list, nr_kolumny, dodaj_ostatnia=True):
    zwrotka = []
    for x in range(len(lista_list)):
            zwrotka.append(lista_list[x][nr_kolumny])
    if dodaj_ostatnia:
        return zwrotka[-1]
    else:
        return zwrotka




#
# piony = []


#
# JAK DOSTAJĘ BŁĄD Z wylosuj_1_liczbe(), TO LOSUJĘ CAŁĄ LINIĘ JESZCZE RAZ, AŻ NIE BĘDZIE BŁĘDU!
#


zakres_niezmienny = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
piony = []
tablica_sudoku = []
zakres = zakres_niezmienny.copy()

# # # pierwsza linia - losowa
# random.shuffle(zakres)
# tablica_sudoku.append(zakres)
#
# # pierwsze indeksy dla pionów
# for x in range(9):
#     piony.append(linia_pionowa(tablica_sudoku,x, dodaj_ostatnia=False))

# def zbuduj_linie(nr_linii, in_st, in_end):
#
#     while True:
#         trojkaNr_1 = []
#         for x in range(3):
#             trojkaNr_1.append(wylosuj_1_liczbe(zakres_niezmienny.copy(),
#                                                trojkaNr_1 + piony[0][in_st:in_end] + piony[1][in_st:in_end] + piony[2][in_st:in_end])[0])
#
#         trojkaNr_2 = []
#
#         for x in range(3):
#             trojkaNr_2.append(wylosuj_1_liczbe(zakres_niezmienny.copy(),  trojkaNr_1+ trojkaNr_2 + piony[3][in_st:in_end] + piony[4][in_st:in_end]+ piony[5][in_st:in_end])[0])
#
#         trojkaNr_3 = []
#
#         for x in range(3):
#             trojkaNr_3.append(wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1+ trojkaNr_2+ trojkaNr_3 + piony[6][in_st:in_end] + piony[7][in_st:in_end]+ piony[8][in_st:in_end])[0])
#
#         tablica_sudoku.append(trojkaNr_1 + trojkaNr_2 + trojkaNr_3)
#
#         # jak nie błąd to linia jest ok,
#         if sprawdz_sume_w_linii(tablica_sudoku[nr_linii]) != "BŁĄD":
#             # aktualizuję piony
#             for x in range(9):
#                 piony[x].append(linia_pionowa(tablica_sudoku, x, dodaj_ostatnia=True))
#
#             break
#         # jak błąd to usuwamy dodaną linię
#         else:
#             tablica_sudoku.pop()
#
# for x in range(1,3):
#     zbuduj_linie(x,0,3)
#
# # BUDOWA 4 linii - TUTAJ NIE MUSZE SPRAWDZAĆ W KWADRACIE 3X3 I JEST OK
# while True:
#
#     trojkaNr_1 = []
#     for x in range(9):
#         trojkaNr_1.append(wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + piony[x])[0])
#
#     tablica_sudoku.append(trojkaNr_1)
#
#     # jak nie błąd to linia jest ok,
#     if sprawdz_sume_w_linii(tablica_sudoku[3]) != "BŁĄD":
#         # aktualizuję piony
#         for x in range(9):
#             piony[x].append(linia_pionowa(tablica_sudoku, x, dodaj_ostatnia=True))
#
#         break
#     # jak błąd to usuwamy dodaną linię
#     else:
#         tablica_sudoku.pop()

# BUDOWA LINII 5 - TUTAJ MUSZĘ WRÓCIĆ PONOWNIE DO SPRAWDZANIA W KWADRACIE 3X3
# TO JEST ZROBIONE ALE BARDZO NA PIECHOTĘ - NIE WIEM JAK ZROBIĆ DO TEGO PĘTLĘ
def zbuduj_linie_dalsza(nr_linii, ind):
    while True:
        if nr_linii ==0:
            # # pierwsza linia - losowa
            random.shuffle(zakres)
            tablica_sudoku.append(zakres)
            # print(tablica_sudoku)
            for y in range(9):
                piony.append(linia_pionowa(tablica_sudoku, y, dodaj_ostatnia=False))
            break
        else:
            trojkaNr_1 = []

            trojkaNr_1.append(
                wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + piony[0][0:] + piony[1][ind:] + piony[2][ind:])[0])

            trojkaNr_1.append(
                wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + piony[0][ind:] + piony[1][0:] + piony[2][ind:])[0])

            trojkaNr_1.append(
                wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + piony[0][ind:] + piony[1][ind:] + piony[2][0:])[0])

            trojkaNr_2 = []

            trojkaNr_2.append(wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + trojkaNr_2 + piony[3][0:] + piony[4][ind:] + piony[5][ind:])[0])
            trojkaNr_2.append(wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + trojkaNr_2 + piony[3][ind:] + piony[4][0:] + piony[5][ind:])[0])
            trojkaNr_2.append(wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + trojkaNr_2 + piony[3][ind:] + piony[4][ind:] + piony[5][0:])[0])

            trojkaNr_3 = []

            trojkaNr_3.append(wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + trojkaNr_2 + trojkaNr_3 + piony[6][0:] + piony[7][ind:] + piony[8][ind:])[0])
            trojkaNr_3.append(wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + trojkaNr_2 + trojkaNr_3 + piony[6][ind:] + piony[7][0:] + piony[8][ind:])[0])
            trojkaNr_3.append(wylosuj_1_liczbe(zakres_niezmienny.copy(), trojkaNr_1 + trojkaNr_2 + trojkaNr_3 + piony[6][ind:] + piony[7][ind:] + piony[8][0:])[0])

            tablica_sudoku.append(trojkaNr_1 + trojkaNr_2 + trojkaNr_3 )

        #
        # # jak nie błąd to linia jest ok,
        if sprawdz_sume_w_linii(tablica_sudoku[nr_linii]) != "BŁĄD" and nr_linii !=0:
            # aktualizuję piony

            for x in range(9):
                piony[x].append(linia_pionowa(tablica_sudoku, x, dodaj_ostatnia=True))

            break
        # jak błąd to usuwamy dodaną linię
        else:
            tablica_sudoku.pop()

for x in range(9):
    if x <3:
        zbuduj_linie_dalsza(nr_linii=x, ind=0)
    elif x >= 3 and x <6:
        zbuduj_linie_dalsza(nr_linii=x, ind=3)
    else:
        zbuduj_linie_dalsza(nr_linii=x, ind=6)

# WYDRUK KOŃCOWY

for x in range(len(tablica_sudoku)):
    print(tablica_sudoku[x], sprawdz_sume_w_linii(tablica_sudoku[x]))
print([sprawdz_powtorke(x) for x in piony])




