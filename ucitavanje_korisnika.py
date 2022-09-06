import time


def ucitaj_korisnike():
    """Funkcija za ucitavanje svih korisnika u sistemu"""

    try:
        lista_korisnika = []
        file = open("korisnici.txt", "r")
        for i in file.readlines():
            m = i.split("|")
            podaci = {"Korisnicko ime": m[0].strip(), "Sifra": m[1].strip(), "Ime": m[2].strip(),
                      "Prezime": m[3].strip(), "Uloga": m[4].strip()}
            lista_korisnika.append(podaci)
        return lista_korisnika
    except Exception:
        print("ULAZNI PODACI NISU PRONADJENI!")
        time.sleep(2)
        exit()


def ucitaj_racune():
    """Funkcija za ucitavanje svih racuna u sistemu"""

    try:
        lista_racuna = []
        file = open("racuni.txt", "r")
        for i in file.readlines():
            m = i.split("|")
            podaci = {"Sifra": m[0].strip(), "Kupljeni instrumenti": m[1].strip(), "Korisnicko ime kupca": m[2].strip(),
                      "Uplata": float(m[3].strip()), "Ukupna cijena": float(m[4].strip()), "Kusur": float(m[5].strip()),
                      "Datum i vrijeme kupovine": m[6].strip()}
            lista_racuna.append(podaci)
        return lista_racuna
    except Exception:
        print("ULAZNI PODACI NISU PRONADJENI!")
        time.sleep(2)
        exit()


def ucitaj_muzickeInstrumente():
    """Funkcija za ucitavanje svih instrumenata u sistemu"""

    try:
        lista_instrumenata = []
        file = open("instrumenti.txt", "r")
        for i in file.readlines():
            m = i.split("|")
            podaci = {"Sifra": m[0].strip(), "Naziv": m[1].strip(), "Proizvodjac": m[2].strip(),
                      "Kolicina": int(m[3].strip()), "Cijena": float(m[4].strip()), "Tip inst.": m[5].strip(),
                      "Obrisano logicki": m[6].strip()}
            lista_instrumenata.append(podaci)
        return lista_instrumenata
    except Exception:
        print("ULAZNI PODACI NISU PRONADJENI!")
        time.sleep(2)
        exit()


def ucitaj_tipoveInstrumenata():
    """Funkcija za ucitavanje svih tipova instrumenata u sistemu"""

    try:
        lista_tipova = []
        file = open("tipovi_instrumenata.txt", "r")
        for i in file.readlines():
            m = i.split("|")
            podaci = {"Sifra": m[0].strip(), "Naziv": m[1].strip()}
            lista_tipova.append(podaci)
        return lista_tipova
    except Exception:
        print("ULAZNI PODACI NISU PRONADJENI!")
        time.sleep(2)
        exit()


def snimi_instrumente(instrumenti):
    """Funkcija za snimanje svih instrumenata u sistemu"""

    file = open("instrumenti.txt", "w")
    br = 0
    for i in instrumenti:
        if br == 0:
            file.write(i["Sifra"] + "|" + i["Naziv"] + "|" + i["Proizvodjac"] + "|" + str(i["Kolicina"]) + "|" + str(
                       i["Cijena"]) + "|" + i["Tip inst."] + "|" + i["Obrisano logicki"])

            br += 1
        else:
            file.write("\n" + i["Sifra"] + "|" + i["Naziv"] + "|" + i["Proizvodjac"] + "|" + str(i["Kolicina"]) + "|" +
                       str(i["Cijena"]) + "|" + i["Tip inst."] + "|" + i["Obrisano logicki"])


def snimi_racune(racuni):
    """Funkcija za ucitavanje svih racuna u sistemu"""

    file = open("racuni.txt", "w")
    br = 0
    for i in racuni:
        if br == 0:
            file.write(i["Sifra"] + "|" + i["Kupljeni instrumenti"] + "|" + i["Korisnicko ime kupca"] + "|" + str(
                       i["Uplata"]) + "|" + str(i["Ukupna cijena"]) + "|" + str(
                       i["Kusur"]) + "|" + i["Datum i vrijeme kupovine"])
            br += 1
        else:
            file.write("\n" + i["Sifra"] + "|" + i["Kupljeni instrumenti"] + "|" + i["Korisnicko ime kupca"] + "|" +
                       str(i["Uplata"]) + "|" + str(i["Ukupna cijena"]) + "|" + str(
                       i["Kusur"]) + "|" + i["Datum i vrijeme kupovine"])