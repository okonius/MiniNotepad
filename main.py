# Definiowanie funkcji

# 1. Dodawanie notatki
def dodaj_notatke(sciezka="dane.txt"):
    notatka = input("\nPodaj treść notatki:\n")
    with open(sciezka, "a", encoding="utf-8") as plik:
        plik.write(f"{notatka}\n")

# 2. Wyświetlanie notatek
def wyswietl_notatki(sciezka="dane.txt"):
    try:
        with open(sciezka, "r", encoding="utf-8") as plik:
            notatki = plik.read().splitlines()
            if not notatki:
                print("Plik jest pusty! Dodaj wpis!")
            else:
                print("\n--- Twoje notatki ---\n")
                for nr, linia in enumerate(notatki, start=1):
                    print(f"{nr}. {linia}")
                print("\n---")

    except FileNotFoundError:
        print("Plik nie istnieje! Najpierw dodaj notatkę!")

# 3. Edycja notatki
def edytuj_notatke(sciezka="dane.txt"):
    try:
        with open(sciezka, "r", encoding="utf-8") as plik:
            notatki = plik.read().splitlines()
            if not notatki:
                print("Plik jest pusty! Dodaj wpis!")

        wyswietl_notatki(sciezka)
        wybor = int(input("\nPodaj numer notatki do edycji: "))

        if wybor <= 0:
            raise IndexError

        nowa_tresc = input("\nPodaj nową treść: ")
        notatki[wybor - 1] = nowa_tresc

        with open(sciezka, "w", encoding="utf-8") as plik:
            for linia in notatki:
                plik.write(f"{linia}\n")

    except FileNotFoundError:
        print("Plik nie istnieje! Najpierw dodaj notatki!")
        return

    except IndexError:
        print("Brak notatki o takim numerze!")

    except ValueError:
        print("Podaj poprawną liczbę!")

# 4. Usuwanie notatki
def usun_notatke(sciezka="dane.txt"):
    try:
        with open(sciezka, "r", encoding="utf-8") as plik:
            notatki = plik.read().splitlines()

        if not notatki:
            print("Plik jest pusty! Nie ma czego usuwać.")
            return

        wyswietl_notatki(sciezka)
        wybor = int(input("\nPodaj numer notatki do usunięcia: "))
        if wybor <= 0:
            raise IndexError

        usunieta = notatki.pop(wybor - 1)

        with open(sciezka, "w", encoding="utf-8") as plik:
            for linia in notatki:
                plik.write(f"{linia}\n")

        print(f"Pomyślnie usunięto: '{usunieta}'")
    except FileNotFoundError:
        print("Plik nie istnieje! Najpierw dodaj notatki!")
    except IndexError:
        print("Brak notatki o takim numerze!")
    except ValueError:
        print("Podaj poprawną liczbę")

# 5. Czyszczenie wszystkich notatek
def wyczysc_notatki(sciezka="dane.txt"):
    with open(sciezka, "w", encoding="utf-8") as plik:
        pass
    print("Notes wyczyszczony!")


# Główny program

print("================")
print(" MINI NOTES 4.1 ")
print("================\n")

while True:
    print("\n--- Menu opcji ---"
        "\n1. Dodaj nowy wpis\n"
        "2. Wyświetl wpisy\n"
        "3. Edytuj notatkę\n"
        "4. Usuń notatkę\n"
        "5. Czyszczenie wszytkich notatek\n"
        "0. Wyjdź\n"
    )

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        dodaj_notatke()
    elif wybor == "2":
        wyswietl_notatki()
    elif wybor == "3":
        edytuj_notatke()
    elif wybor == "4":
        usun_notatke()
    elif wybor == "5":
        wyczysc_notatki()
    elif wybor == "0":
        print("\nDo widzenia!")
        break
    else:
        print("\nBłędny wybór!")