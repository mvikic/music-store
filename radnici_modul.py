import zajednicki
import ucitavanje_korisnika


def ispisi_meni():

    # Funkcija za ispis menija opcija prodavca

    print()
    print("(1) Prikazi sve instrumente na lageru: ")
    print("(2) Pretrazi instrumente: ")
    print("(3) Dodaj novi instrument: ")
    print("(4) Izmijeni postojece instrumente: ")
    print("(5) Logicko brisanje instrumenata: ")
    print("(6) Logicko vracanje instrumenata: ")
    print("(7) Izlaz")
    print()


def logBrisanje_instrumenta(instrumenti):

    # Kao parametar prima listu instrumenata
    # Funkcija sluzi za logicko brisanje nekog instrumenta

    zajednicki.ispisi_tabelu(instrumenti)
    while True:
        postoji = False
        sifra = input("Molimo, unesite sifru instrumenta kog zelite da izbrisete: ")
        if provjera_brisanja(sifra, instrumenti) == "True":
            print("Instrument je vec obrisan!")
            continue
        elif len(sifra.strip()) == 0:
            continue
        for i in instrumenti:
            if i["Sifra"] == sifra:
                postoji = True
                i["Obrisano logicki"] = "True"
        if postoji:
            break
    ucitavanje_korisnika.snimi_instrumente(instrumenti)


def logVracanje_instrumenta(instrumenti):

    # Kao parametar prima listu instrumenata
    # Funkcija sluzi za logicko vracanje nekog instrumenta

    zajednicki.ispisi_tabelu(instrumenti)
    while True:
        postoji = False
        sifra = input("Molimo, unesite sifru instrumenta koji zelite da vratite: ")
        if provjera_brisanja(sifra, instrumenti) == "False":
            print("Instrument je vec aktivan!")
            continue
        elif len(sifra.strip()) == 0:
            continue
        for i in instrumenti:
            if i["Sifra"] == sifra:
                postoji = True
                i["Obrisano logicki"] = "False"
        if postoji:
            break
    ucitavanje_korisnika.snimi_instrumente(instrumenti)


def provjera_brisanja(sifra, instrumenti):

    # Kao parametar prima unetu sifru i listu instrumenata
    # Funkcija sluzi za proveru da li je instrument sa unetom sifrom vec obrisan

    for i in instrumenti:
        if i["Sifra"] == sifra:
            return i["Obrisano logicki"]


def novi_instrument(instrumenti, tipovi_instrumenata):

    # Kao parametar prima listu instrumenata, i listu tipova instrumenata
    # Funkcija sluzi za dodavanje novog instrumenta u sistem

    sifra = ""
    while True:
        sifra = input("Molimo, unesite sifru: ")
        if len(sifra.strip()) == 0:
            print("Sifra ne moze biti prazno polje!")
            continue
        if zajednicki.provjera_sifreInstrumenta(sifra, instrumenti):
            break
        else:
            print("Zao nam je, unijeta sifra vec postoji!")

    naziv = input("Unesite naziv instrumenta: ")
    while len(naziv.strip()) == 0:
        naziv = input("Unesite naziv instrumenta: ")

    proizvodjac = input("Unesite proizvodjaca: ")
    while len(proizvodjac.strip()) == 0:
        print("Pogresan unos probajte ponovo")
        proizvodjac = input("Unesite proizvodjaca: ")

    kolicina = input("Unesite kolicinu: ")
    while pogresan_unosKolicine(kolicina):
        kolicina = input("Unesite kolicinu: ")

    cijena = input("Unesite cenu: ")
    while pogresan_unosCijene(cijena):
        cijena = input("Unesite cenu: ")

    zajednicki.ispisi_tabelu(tipovi_instrumenata)
    tip = ""
    while True:
        postoji = False
        tip = input("Unesite sifru tipa instrumenta: ")
        if len(tip.strip()) == 0:
            continue
        for i in tipovi_instrumenata:
            if i["Sifra"] == tip:
                postoji = True
        if postoji:
            break
    novi_inst = {"Sifra": sifra, "Naziv": naziv, "Proizvodjac": proizvodjac, "Kolicina": int(kolicina), "Cijena": float(cijena),
         "Tip inst.": tip, "Obrisano logicki": "False"}
    instrumenti.append(novi_inst)
    ucitavanje_korisnika.snimi_instrumente(instrumenti)


def pogresan_unosKolicine(kolicina):

    # Kao parametar prima unetu kolicinu
    # Funkcija sluzi za proveru loseg unosa kolicine

    try:
        w = int(kolicina)
        if kolicina.isnumeric() and w > 0:
            return False
    except:
        pass
    print("Molimo, unesite cio broj!(veci od 0)")
    return True


def izmjena_instrumenta(instrumenti):

    # Kao parametar prima listu instrumenata
    # Funkcija sluzi za izmenu instrumenta

    zajednicki.ispisi_tabelu(instrumenti)
    while True:
        postoji = False
        sifra = input("Molimo, unesite sifru instrumenta za izmjenu: ")
        if len(sifra.strip()) == 0:
            continue
        for i in instrumenti:
            if i["Sifra"] == sifra:
                postoji = True
                kolicina = input("Unesite novu kolicinu: ")
                while pogresan_unosKolicine(kolicina):
                    kolicina = input("Unesite novu kolicinu: ")
                i["Kolicina"] = kolicina
        if postoji:
            break
    ucitavanje_korisnika.snimi_instrumente(instrumenti)



def pogresan_unosCijene(cijena):

    # Kao parametar primamo unijetu cijenu kao string
    # Funkcija sluzi za provjeru unosa cijene

    try:
        if float(cijena) > 0:
            return False
    except:
        pass
    print("Molimo, unesite cio broj!(veci od 0)")
    return True



def opcije_radnik(instrumenti, tipovi_instrumenata):

    # Kao parametar prima listu instrumenata i listu tipovaInstrumenata
    # Funkcija sluzi za proveru da li je instrument sa unetom sifrom vec obrisan

    odabrana_opcija = 0
    while odabrana_opcija != "7":
        ispisi_meni()
        odabrana_opcija = input(">>> ")
        if odabrana_opcija == "1":
            zajednicki.prikaz_svihInstrumenata("P", instrumenti, tipovi_instrumenata)
        elif odabrana_opcija == "2":
            zajednicki.pretrazi_sveInstrumente("P", instrumenti, tipovi_instrumenata)
        elif odabrana_opcija == "3":
            novi_instrument(instrumenti, tipovi_instrumenata)
        elif odabrana_opcija == "4":
            izmjena_instrumenta(instrumenti)
        elif odabrana_opcija == "5":
            logBrisanje_instrumenta(instrumenti)
        elif odabrana_opcija == "6":
            logVracanje_instrumenta(instrumenti)
        elif odabrana_opcija == "7":
            break
        else:
            print("Los unos, pokusajte ponovo")
            print()



