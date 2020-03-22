import random

lists = ["kamień", "papier", "nożyce"]


def choice():
    choice = input("Wybierasz ")
    return choice


def game_pvp():
    print("1 - Gra PvP")
    gamer_1 = input("Pierwszy graczu jak masz na imię? ").capitalize()
    gamer_2 = input("Drugi graczu jak masz na imię? ").capitalize()
    pkt_1 = 0
    pkt_2 = 0
    while True:
        choose_1 = input(" %s, Co wybierasz? Kamień, papier czy nożyce? " % gamer_1).lower()
        choose_2 = input(" %s, Co wybierasz? Kamień, papier czy nożyce? " % gamer_2).lower()

        if choose_1 in lists and choose_2 in lists:
            if choose_1 == choose_2:
                print("Remis!")
            elif choose_1 == "papier":
                if choose_2 == "kamień":
                    print("Papier wygrywa")
                    pkt_1 += 1
                elif choose_2 == "nożyce":
                    print("Nożyce wygrywają")
                    pkt_2 += 1
            elif choose_1 == "kamień":
                if choose_2 == "nożyce":
                    print("Kamień wygrywa")
                    pkt_1 += 1
                elif choose_2 == "papier":
                    print("Papier wygrywa")
                    pkt_2 += 1
            elif choose_1 == "nożyce":
                if choose_2 == "papier":
                    print("Nożyce wygrywają")
                    pkt_1 += 1
                elif choose_2 == "kamień":
                    print("Kamień wygrywa")
                    pkt_2 += 1

        if choose_1 not in lists or choose_2 not in lists:
            print("Błędny wybór spróbuj jeszcze raz")

        ask = input("Grasz dalej? T czy N? ").lower()
        if ask == "n":
            print(" Gracz %s" % gamer_1, pkt_1, "punkty/ów \n Gracz %s" % gamer_2, pkt_2, "punkty/ów")
            break
        elif ask == "t":
            continue
        else:
            print("Błędny wybór")


def game_pvp_rm():
    print("2 - Gra PVP Random Mode Nowość!!!")
    gamer_1 = input("Pierwszy graczu jak masz na imię? ").capitalize()
    gamer_2 = input("Drugi graczu jak masz na imię? ").capitalize()
    pkt_1 = 0
    pkt_2 = 0
    while True:
        choose_1 = input(" %s, Co wybierasz? Kamień, papier czy nożyce? " % gamer_1).lower()
        choose_r1 = random.choice(lists)
        choose_2 = input(" %s, Co wybierasz? Kamień, papier czy nożyce? " % gamer_2).lower()
        choose_r2 = random.choice(lists)
        x = None
        y = None

        if choose_1 in lists and choose_2 in lists:
            if choose_1 == choose_r1:
                x = choose_1
            elif choose_1 == "papier":
                if choose_r1 == "kamień":
                    x = choose_1
                elif choose_r1 == "nożyce":
                    x = choose_r1
            elif choose_1 == "kamień":
                if choose_r1 == "nożyce":
                    x = choose_1
                elif choose_r1 == "papier":
                    x = choose_r1
            elif choose_1 == "nożyce":
                if choose_r1 == "papier":
                    x = choose_1
                elif choose_r1 == "kamień":
                    x = choose_r1
            if choose_2 == choose_r2:
                y = choose_2
            elif choose_2 == "papier":
                if choose_r2 == "kamień":
                    y = choose_2
                elif choose_r2 == "nożyce":
                    y = choose_r2
            elif choose_2 == "kamień":
                if choose_r2 == "nożyce":
                    y = choose_2
                elif choose_r2 == "papier":
                    y = choose_r2
            elif choose_2 == "nożyce":
                if choose_r2 == "papier":
                    y = choose_2
                elif choose_r2 == "kamień":
                    y = choose_r2
            if x == y:
                print("Remis!")
            elif x == "papier":
                if y == "kamień":
                    print("Papier wygrywa")
                    pkt_1 += 1
                elif y == "nożyce":
                    print("Nożyce wygrywają")
                    pkt_2 += 1
            elif x == "kamień":
                if y == "nożyce":
                    print("Kamień wygrywa")
                    pkt_1 += 1
                elif y == "papier":
                    print("Papier wygrywa")
                    pkt_2 += 1
            elif x == "nożyce":
                if y == "papier":
                    print("Nożyce wygrywają")
                    pkt_1 += 1
                elif y == "kamień":
                    print("Kamień wygrywa")
                    pkt_2 += 1

        if choose_1 not in lists or choose_2 not in lists:
            print("Błędny wybór spróbuj jeszcze raz")

        ask = input("Grasz dalej? T czy N? ").lower()
        if ask == "n":
            print(" Gracz %s" % gamer_1, pkt_1, "punkty/ów \n Gracz %s" % gamer_2, pkt_2, "punkty/ów")
            break
        elif ask == "t":
            continue
        else:
            print("Błędny wybór")


def game_pvc():
    print("3 - Gra PvC")
    pkt_p = 0
    pkt_c = 0
    while True:
        choose = input("Co wybierasz? Kamień, papier czy nożyce? ").lower()
        comp_choice = random.choice(lists)
        if choose in lists:
            if choose == comp_choice:
                print("Remis")
            elif choose == "kamień":
                if comp_choice == "nożyce":
                    print("Kamień wygrywa")
                    pkt_p += 1
                elif comp_choice == "papier":
                    print("Papier wygrywa")
                    pkt_c += 1
            elif choose == "papier":
                if comp_choice == "kamień":
                    print("Papier wygrywa")
                    pkt_p += 1
                elif comp_choice == "nożyce":
                    print("Nożyce wygrywają")
                    pkt_c += 1
            elif choose == "nożyce":
                if comp_choice == "papier":
                    print("Nożyce wygrywają")
                    pkt_p += 1
                elif comp_choice == "kamień":
                    print("Kamień wygrywa")
                    pkt_c += 1

        print(" Zdobyłeś/aś", pkt_p, "punkt/ów \n Komputer zdobył", pkt_c, "punkt/ów")
        ask = input("Grasz dalej? T czy N? ").lower()
        if ask == "n":
            if pkt_p == pkt_c:
                print("Remis")
            elif pkt_p > pkt_c:
                print("Gratuluje - Wygrałeś!")
            else:
                print("Przykro mi - Przegrałeś!")
            break
        elif ask == "t":
            continue
        else:
            print("Błędny wybór")


def game_pvc_10():
    print("""4 - Gra PvC "10 szans""")
    name = input("Jak masz na imię? ").capitalize()
    chance = 10
    pkt_p = 0
    pkt_c = 0
    while chance != 0:
        choose = input("Co wybierasz kamień, papier czy nożyce? ").lower()
        comp_choice = random.choice(lists)
        if choose in lists:
            if choose == comp_choice:
                print("Remis")
                chance -= 1
            elif choose == "kamień":
                if comp_choice == "nożyce":
                    print("Kamień wygrywa")
                    pkt_p += 1
                    chance -= 1
                elif comp_choice == "papier":
                    print("Papier wygrywa")
                    pkt_c += 1
                    chance -= 1
            elif choose == "papier":
                if comp_choice == "kamień":
                    print("Papier wygrywa")
                    pkt_p += 1
                    chance -= 1
                elif comp_choice == "nożyce":
                    print("Nożyce wygrywają")
                    pkt_c += 1
                    chance -= 1
            elif choose == "nożyce":
                if comp_choice == "papier":
                    print("Nożyce wygrywają")
                    pkt_p += 1
                    chance -= 1
                elif comp_choice == "kamień":
                    print("Kamień wygrywa")
                    pkt_c += 1
                    chance -= 1
    score = name + " " + str(pkt_p) + "\n"
    print(score)
    text_file = open("wyniki", "a+")
    text_file.write(score)
    text_file.close()


def board():
    print(" 5 - Tablica wyników")
    try:
        text_file = open("wyniki", "r")
        print(text_file.read())
        text_file.close()
    except FileNotFoundError:
        print('Nie ma jeszcze wyników. Musisz najpierw zagrać w tryb Gra PvC "10 szans"')


def instruction():
    print("6 - Instrukcja")
    try:
        plik = open("instruction.txt", "r")
        print(plik.read())
        plik.close()
    except FileNotFoundError:
        print("Nie znaleziono pliku z instrukcją.")


def qui_t():
    print("Do zobaczenia")


def outro():
    print("Gra została stworzona przez MB - ProGramPI")


def menu():
    choice = None
    while choice != "7":
        print("""
                  GRA
        KAMIEŃ - PAPIER - NOŻYCE
        ________________________
        1 - Gra PvP
        2 - Gra PvP RM !!!
        3 - Gra PvC
        4 - Gra PvC "10 Szans"
        5 - Tablica wyników
        6 - Instrukcja
        7 - Wyjście""")

        choice = input("Wybierasz? ")

        if choice == "1":
            game_pvp()
        elif choice == "2":
            game_pvp_rm()
        elif choice == "3":
            game_pvc()
        elif choice == "4":
            game_pvc_10()
        elif choice == "5":
            board()
        elif choice == "6":
            instruction()
        elif choice == "7":
            qui_t()
        else:
            print("Błędny wybór")


def main():
    menu()
    quit()
    outro()


main()
