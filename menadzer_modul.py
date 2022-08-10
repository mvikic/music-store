import datetime
import zajednicki
import getpass
from collections import Counter


def ispisi_meniMenadzer():

    # Funkcija za ispis funkcionalnosti dostupnih menadzeru

    print()
    print("(1) Prikazi sve instrumente na lageru: ")
    print("(2) Pretrazi instrumente: ")
    print("(3) Dodaj novog radnika: ")
    print("(4) Ispisi izvjestaj: ")
    print("(5) Izlaz: ")
    print()

def dodaj_novogRadnika(korisnici):

    # Kao parametar funkcija prima listu korisnika
    # Sluzi za dodavanje novog prodavca

    korisnicko_ime = ""
    while True:
        korisnicko_ime = input("Molimo vas, unesite korisnicko ime radnika: ")
        if len(korisnicko_ime.strip()) == 0:
            print("Zao nam je, korisnicko ime radnika ne moze biti prazno polje!")
            continue
        if zajednicki.provjera_jedinstvenogImena(korisnicko_ime, korisnici):
            break
        else:
            print("Zao nam je, unijeto korisnicko ime vec postoji!")

    sifra = getpass.getpass("Molimo vas, unesite lozinku radnika: ")
    while len(sifra.strip()) == 0:
        sifra = getpass.getpass("Molimo vas, unesite lozinku radnika: ")

    Ime = input("Molimo vas, unesite ime radnika: ")
    while len(Ime.strip()) == 0:
        print("Zao nam je, unos je neispravan. Probajte ponovo!")
        Ime = input("Molimo vas, unesite ime radnika: ")

    Prezime = input("Molimo vas, unesite prezime radnika: ")
    while len(Prezime.strip()) == 0:
        print("Zao nam je, unos je pogresan. Pokusajte ponovo!")
        Prezime = input("Molimo vas, unesite prezime radnika: ")

    file = open("korisnici.txt", "a")
    novo = "\n" + korisnicko_ime + "|" + sifra + "|" + Ime + "|" + Prezime + "|" + "radnik"
    file.write(novo)
    file.close()


def novi_datum(unesiDatum):

    # Kao parametar prima poruku za unos datuma
    # Funkcija sluzi za proveru formata datuma i vremena

    dan = 0
    mje = 0
    god = 0
    while True:
        datum = input(unesiDatum)
        try:
            datetime.datetime.strptime(datum, "%d.%m.%Y.")
            q = datum.split(".")
            dan = q[0]
            mje = q[1]
            god = q[2]
            break
        except:
            print("Unijeli ste neispravan datum!")
    sat = 0
    min = 0
    while True:
        vrijeme = input("Molimo vas, unesite sate i minute! (sati:minuti)")
        try:
            datetime.datetime.strptime(vrijeme, "%H:%M")
            m = vrijeme.split(":")
            sat = m[0]
            min = m[1]
            break
        except:
            print("Los unos vremena !")

    return datetime.datetime(int(god), int(mje), int(dan), int(sat), int(min))          # 24.12.2017. 14:22



def uredi_datum(tumda):

    # Kao parametar prima datum u stringu
    # Funkcija sluzi za konverziju iz stringa u datetime objekat

    pr = tumda.split(" ")
    datum = pr[0].split(".")
    vrijeme = pr[1].split(":")
    dan = datum[0]
    mje = datum[1]
    god = datum[2]
    sat = vrijeme[0]
    min = vrijeme[1]
    return datetime.datetime(int(god), int(mje), int(dan), int(sat), int(min))


def izvjestaj_maker(instrumenti, tipovi_instrumenata, racuni):

    # Kao parametar prima listu instumenata, tipova, i racuna
    # Funkcija pravi izvjestaj menadzera

    while True:
        Izvjestaj = []
        print("(1) Prikazi ukupnu prodaju instrumenata u zadatom vremenskom periodu:")
        print("(2) Prikazi ukupnu prodaju odredjenog instrumenta u zadatom vremenskom periodu:")
        print("(3) Prikazi ukupnu prodaju odredjenog tipa instrumenta u zadatom vremenskom periodu")
        print("(4) Izlaz")
        odabrana_opcija = input(">>> ")
        if odabrana_opcija == "4":
            break
        datum_pocetak = novi_datum("Molimo vas, unesite pocetni datum (dan.mjesec.godina.)")
        datum_kraj = novi_datum("Molimo vas, unesite krajnji datum (dan.mjesec.godina.)")
        while datum_pocetak > datum_kraj:
            print("Greska! Krajnji datum ne moze biti prije pocetnog datuma!")
            datum_kraj = novi_datum("Molimo vas, unesite krajnji datum (dan.mjesec.godina.)")
        zarada = 0
        if odabrana_opcija == "1":
            for i in racuni:
                trenutni = uredi_datum(i["Datum i vrijeme kupovine"])
                if datum_pocetak <= trenutni <= datum_kraj:
                    zarada += i["Ukupna cijena"]
                    Izvjestaj.append(i)
        elif odabrana_opcija == "2":
            naziv_instr = input("Molimo vas, unesite naziv instrumenta: ")
            while len(naziv_instr.strip()) == 0:
                naziv_instr = input("Molimo vas, unesite naziv instrumenta: ")
            for i in racuni:
                trenutni = uredi_datum(i["Datum i vrijeme kupovine"])
                if datum_pocetak <= trenutni <= datum_kraj:
                    brojac = dict(Counter(i["Kupljeni instrumenti"].split(",")))
                    for j in brojac:
                        if j == naziv_instr:
                            m = vrati_infoInstrumenta(j, instrumenti, tipovi_instrumenata)
                            zarada += brojac[j] * m[2]
                            Izvjestaj.append({"Sifra inst.": m[0], "Naziv inst.": j, "Proizvodjac": m[1],
                                             "Tip inst.": m[3],
                                             "Cijena": str(brojac[j] * m[2]) + "(" + str(brojac[j]) + " x " + str(m[2]) + ")",
                                             "Datum i vrijeme kupovine": i["Datum i vrijeme kupovine"]})

        elif odabrana_opcija == "3":
            tip_instr = input("Molimo vas, unesite tip instrumenta: ")
            while len(tip_instr.strip()) == 0:
                tip_instr = input("Molimo vas, unesite tip instrumenta: ")
            for i in racuni:
                trenutni = uredi_datum(i["Datum i vreme kupovine"])
                if datum_pocetak <= trenutni <= datum_kraj:
                    brojac = dict(Counter(i["Kupljeni instrumenti"].split(",")))
                    for j in brojac:
                        m = vrati_infoInstrumenta(j, instrumenti, tipovi_instrumenata)
                        if m[3] == tip_instr:
                            zarada += brojac[j] * m[2]
                            Izvjestaj.append({"Sifra inst.": m[0], "Naziv inst.": j, "Proizvodjac": m[1],
                                             "Tip inst.": m[3],
                                             "Cijena": str(brojac[j] * m[2]) + "(" + str(m[j]) + " x " + str(m[2]) + ")",
                                             "Datum i vrijeme kupovine": i["Datum i vrijeme kupovine"]})
        else:
            print("Zao nam je, unos je pogresan. Pokusajte ponovo!")
            print()
        zajednicki.ispisi_tabelu(Izvjestaj)
        print()
        print("Ukupna zarada: " + str(zarada))
        print()


def vrati_infoInstrumenta(naziv_instr, instrumenti, tipovi_instrumenata):

    # Kao parametar prima naziv instrumenta, listu instrumenata, i tipove instrumenata
    # Funkcija za zadato ime, vraca sifru proizvodjaca cenu i tip instrumenta

    vraca = []
    for i in instrumenti:
        if naziv_instr == i["Naziv"]:
            vraca.append(i["Sifra"])
            vraca.append(i["Proizvodjac"])
            vraca.append(i["Cijena"])
            for j in tipovi_instrumenata:
                if i["Tip inst."] == j["Sifra"]:
                    vraca.append(j["Naziv"])
                    return vraca


def opcije_menadzer(korisnici, instrumenti, tipovi_instrumenata, racuni):

    # Kao parametar prima listu korisnika, instrumenata, tipova i racuna
    # Funkcija prikazuje osnovni meni prodavca i njegove funkcionalnosti

    odabrana_opcija = 0
    while odabrana_opcija != "5":
        ispisi_meniMenadzer()
        odabrana_opcija = input(">>> ")
        if odabrana_opcija == "1":
            zajednicki.prikaz_svihInstrumenata("M", instrumenti, tipovi_instrumenata)
        elif odabrana_opcija == "2":
            zajednicki.pretrazi_sveInstrumente("M", instrumenti, tipovi_instrumenata)
        elif odabrana_opcija == "3":
            dodaj_novogRadnika(korisnici)
        elif odabrana_opcija == "4":
            izvjestaj_maker(instrumenti, tipovi_instrumenata, racuni)
        elif odabrana_opcija == "5":
            break
        else:
            print("Zao nam je, unos je pogresan. Pokusajte ponovo!")
            print()



