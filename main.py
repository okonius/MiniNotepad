# Definiowanie funkcji

def dodaj_notatke(sciezka="dane.txt"):
      notatka = input("Podaj treść notatki:\n")
      with open(sciezka,"a", encoding="utf-8") as plik:
            plik.write(f"{notatka}\n")

def wyswietl_notatki(sciezka="dane.txt"):
      try:
          with open(sciezka, "r", encoding="utf-8") as plik:
              tresc = plik.read()
              if not tresc.strip():
                  print("Dziennik jest pusty! Dodaj wpis!")
              else:
                  with open(sciezka, "r", encoding="utf-8") as plik:
                      print(f"--- Twoje notatki ---\n")
                      nr = 1
                      for linia in plik:
                          print(f"{nr}. {linia.strip()}")
                          nr += 1
                      print(f"\n---------")
      except FileNotFoundError:
          print("Plik nie istnieje! Najpierw dodaj notatkę!")


def wyczysc_notatki(sciezka="dane.txt"):
      with open(sciezka, "w", encoding="utf-8") as plik:
            pass
      print("Notes wyczyszczony!")


# Główny programg
print("============")
print(" MINI NOTES ")
print("============\n")

while True:

      print("\n1. Dodaj nowy wpis\n"
            "2. Wyświetl wpisy\n"
            "3. Czyszczenie notatek\n"
            "0. Wyjdź")

      wybor = input("Wybierz opcję: ")

      if wybor == "1":
            dodaj_notatke()
      elif wybor == "2":
            wyswietl_notatki()
      elif wybor == "3":
            wyczysc_notatki()
      elif wybor == "0":
            break
      else:
            print("Błędny wybór!")