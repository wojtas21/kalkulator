print("========== Co chcesz dzisiaj zrobic? ==========")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")

print ("==========")

wybor = int(input("Wybierz opcje wpisujac numer: "))

if wybor == 1:
    print("Wybrales dodawanie")
elif wybor == 2:
    print("Wybrales Odejmowanie")
elif wybor == 3:
    print("Wybrales Mnozenie")
elif wybor == 4:
    print("Wybrales Dzielenie")
print ("=============================================")

liczba1 = float(input("Podaj pierwsza liczbe: "))
liczba2 = float(input("Podaj druga liczbe: "))

print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

if wybor == 1:
    w1 = liczba1+liczba2
    print(("Wynik:"), w1)
elif wybor == 2:
    w2=liczba1-liczba2
    print(("Wynik:"), w2)
elif wybor == 3:
    w3=liczba1*liczba2
    print(("Wynik:"), w3)
elif wybor == 4:
    w4=liczba1/liczba2
    print(("Wynik:"), w4)
print ("=============================================")
