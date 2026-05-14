print("SUPER SYMULATOR JEDZENIA CEMENTU II TURBO")
print("DEFINITIVE DELUXE DIRECTOR'S CUT REMAKE REMASTERED")
print("GRABARZSOFT© 1993")
print("")
input("WCIŚNIJ START ABY ROZPOCZĄĆ ")
print("")
nazwa = str(input("JAK SIĘ NAZYWA TWOJA POSTAĆ? "))
wiek = int(input("ILE LAT MA TWOJA POSTAĆ? "))
str(input("JAKIEJ PŁCI JEST TWOJA POSTAĆ? "))
poziom_trudnosci = int(input("PODAJ POZIOM TRUDNOŚCI OD 0 do 9: "))
wynik = 0
print("")
if poziom_trudnosci > 7:
    if poziom_trudnosci > 9:
        print(nazwa+", wiek "+str(wiek)+" NATYCHMIAST UMIERA")
        print("ZAKOŃCZENIE 7 z 84")
        wynik += 2
    else:
        print("MUSISZ STWORZYĆ WŁASNY CEMENT")
        print("ZAKOŃCZENIE 5 z 84")
        wynik += 2
elif poziom_trudnosci < 2:
    print("CEMENT JUŻ JEST ZJEDZONY")
    print("ZAKOŃCZENIE 6 z 84")
    wynik += 2
else:
    print(nazwa+", wiek "+str(wiek)+" WIDZI PRZED SOBĄ CEMENT")
    odpowiedz = input("CO ROBISZ? J ABY ZJEŚĆ CEMENT ")
    print("")
    if odpowiedz == "J" or odpowiedz == "j":
        print("JESZ CEMENT")
        print("ZAKOŃCZENIE 1 z 84")
        wynik += 1
    elif odpowiedz == "B" or odpowiedz == "b":
        wynik += 1
        print("ZAMIENIASZ CEMENT W BETON")
        odpowiedz = input("CO ROBISZ? J ABY ZJEŚĆ BETON ")
        print("")
        if odpowiedz == "J" or odpowiedz == "j":
            print("JESZ BETON")
            print("ZAKOŃCZENIE 3 z 84")
            wynik += 1
        elif odpowiedz == "B" or odpowiedz == "b":
            print("PRÓBUJESZ ZAMIENIĆ BETON W BETON I EKSPLODUJESZ")
            print("ZAKOŃCZENIE 4 z 84")
            wynik += 1
        elif odpowiedz == "C" or odpowiedz == "c":
            print("PRÓBUJESZ ZAMIENIĆ BETON W CEMENT I EKSPLODUJESZ")
            print("ZAKOŃCZENIE 10 z 84")
            wynik += 1
        else:
            print("ZOSTAJESZ ZABITY PRZEZ BETON")
            print("ZAKOŃCZENIE 14 z 84")
    elif odpowiedz == "D" or odpowiedz == "d":
        print("PRZECHODZISZ NA DIETĘ")
        print("ZAKOŃCZENIE 8 z 84")
        wynik += 2
    elif odpowiedz == nazwa:
        print("ZJADASZ SAMEGO SIEBIE")
        print("ZAKOŃCZENIE 9 z 84")
        wynik += 4
    elif odpowiedz == "C" or odpowiedz == "c":
        print("PRÓBUJESZ ZAMIENIĆ CEMENT W CEMENT I EKSPLODUJESZ")
        print("ZAKOŃCZENIE 11 z 84")
        wynik += 1
    elif odpowiedz == "W" or odpowiedz == "w":
        print("WCIĄGASZ CEMENT I PRZEDAWKOWUJESZ")
        print("ZAKOŃCZENIE 12 z 84")
        wynik += 2
    elif odpowiedz == "K" or odpowiedz == "k":
        print("Kacper")
        print("ZAKOŃCZENIE 13 z 84")
        wynik += 4
    elif odpowiedz == "N" or odpowiedz == "n":
        print("ROZBIERASZ SIĘ DO NAGA")
        print("ZAKOŃCZENIE 15 z 84")
        wynik += 2
    elif odpowiedz == "S" or odpowiedz == "s":
        print("CENZURA")
        print("ZAKOŃCZENIE 69 z 84")
        wynik += 2
    elif odpowiedz == "1984" or odpowiedz == "84":
        print("CZYTASZ KSIĄŻKĘ JERZEGO ORWELLA POD TYTUŁEM 1984")
        print("ZAKOŃCZENIE 84 z 84")
        wynik += 4
    elif odpowiedz == "Z" or odpowiedz == "z":
        wynik += 2
        print("UDAŁO CI SIĘ UGOTOWAĆ PYSZNĄ ZUPĘ Z CEMENTU")
        odpowiedz = input("CO ROBISZ? J ABY ZJEŚĆ ZUPĘ ")
        print("")
        if odpowiedz == "J" or odpowiedz == "j":
            wynik += 1
            print("JESZ PYSZNĄ ZUPĘ Z CEMENTU")
            print("ZAKOŃCZENIE 16 z 84")
        elif odpowiedz == "B" or odpowiedz == "b":
            wynik += 1
            print("ZAMIENIASZ ZUPĘ Z CEMENTU NA ZUPĘ Z BETONU")
            odpowiedz = input("CO ROBISZ? J ABY ZJEŚĆ ZUPĘ ")
            print("")
            if odpowiedz == "J" or odpowiedz == "j":
                print("JESZ PYSZNĄ ZUPĘ Z BETONU")
                print("ZAKOŃCZENIE 18 z 84")
                wynik += 1
            elif odpowiedz == "B" or odpowiedz == "b":
                print("PRÓBUJESZ ZAMIENIĆ ZUPĘ Z BETONU W BETON I EKSPLODUJESZ")
                print("ZAKOŃCZENIE 21 z 84")
                wynik += 1
            elif odpowiedz == "C" or odpowiedz == "c":
                print("PRÓBUJESZ ZAMIENIĆ ZUPĘ Z BETONU W CEMENT I EKSPLODUJESZ")
                print("ZAKOŃCZENIE 22 z 84")
                wynik += 1
            else:
                print("MARNUJESZ PYSZNĄ ZUPĘ Z BETONU")
                print("ZAKOŃCZENIE 20 z 84")
        elif odpowiedz == "C" or odpowiedz == "c":
            print("PRÓBUJESZ ZAMIENIĆ ZUPĘ Z CEMENTU W CEMENT I EKSPLODUJESZ")
            print("ZAKOŃCZENIE 19 z 84")
            wynik += 1
        else:
            print("MARNUJESZ PYSZNĄ ZUPĘ Z CEMENTU")
            print("ZAKOŃCZENIE 17 z 84")
    elif odpowiedz == "R" or odpowiedz == "r":
        print("IDZIESZ NA RANDKĘ Z CEMENTEM")
        wynik += 2
    else:
        print("NIE UDAŁO CI SIĘ ZJEŚĆ CEMENTU")
        print("ZAKOŃCZENIE 2 z 84")
print("")
print("KONIEC GRY")
print(nazwa+", wiek "+str(wiek)+" WYNIK: "+str(wynik*1000))
