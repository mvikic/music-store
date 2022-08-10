import zajednicki
import ucitavanje_korisnika
import datetime
from collections import Counter

def ispis_menija():

    # Funkcija za ispis funkcionalnosti kupca

    print()
    print("(1) Prikazi sve instrumente na lageru: ")
    print("(2) Pretrazi instrumente: ")
    print("(3) Kupi instrument/e: ")
    print("(4) Prikazi prethodne kupovine: ")
    print("(5) Izlaz")
    print()


def opcije_kupac(kupac, instrumenti, tipovi_instrumenata, racuni):

    # Kao parametar prima trenutnog kupca,listu korisnika, instrumenata, tipova i racuna
    # Funkcija prikazuje osnovni meni prodavca i njegove funkcionalnosti

    odabrana_opcija = 0
    while odabrana_opcija != "6":
        ispis_menija()
        odabrana_opcija = input(">>> ")
        if odabrana_opcija == "1":
            zajednicki.prikaz_svihInstrumenata("K", instrumenti, tipovi_instrumenata)
        elif odabrana_opcija == "2":
            zajednicki.pretrazi_sveInstrumente("K", instrumenti, tipovi_instrumenata)
        elif odabrana_opcija == "3":
            kupovina_instrumenta(kupac, instrumenti, racuni)
        elif odabrana_opcija == "4":
            prethodno_kupljeno(kupac, instrumenti, tipovi_instrumenata, racuni)
        elif odabrana_opcija == "5":
            break
        else:
            print("Pogresan unos! Molimo da pokusate ponovo!")
            print()


def pogresan_unosKolicine(kolicina, koliko_ima):

    # Kao parametar prima kolicinu i trenutnu dostupnost odabranog instrumenta u sistemu
    # Funkcija sluzi za provjeru ispravnosti unosta za odredjeni instrument

    try:
        b = int(kolicina)
        if koliko_ima < b:
            print("Trazena kolicina instrumenata nije dostupna!")
            return True
        if kolicina.isnumeric() and b > 0:
            return False
    except:
        pass
    print("Molimo, unesite cio broj!(veci od 0)")
    return True


def kupovina_instrumenta(kupac, instrumenti, racuni):

    # Kao parametar prima trenutnog kupca, listu instrumenata i racuna
    # Funkcija sluzi za obradu kupovine trenutnog kupca
    ########
    nova_sifra = nova_sifraRacuna(racuni)
    datum_vrijeme = datetime.datetime.today().strftime("%d.%m.%Y. %H:%M")
    korisnicko_ime = kupac["Korisnicko ime"]
    kupljeni_instrumenti = {}  # sifre instrumenata
    uplaceno = 0
    ukupna_cijena = 0

    while True:
        zajednicki.ispisi_tabelu(zajednicki.ukloni_obrisane(instrumenti))
        sifra = input("Unesite sifru instrumenta za kupovinu (hvala za izlaz): ")
        if sifra == "hvala":
            break
        if len(sifra.strip()) == 0:
            continue
        for i in instrumenti:
            if i["Sifra"] == sifra and i["Obrisano logicki"] == "False" and i["Kolicina"] > 0:
                kolicina = input("Unesite kolicinu koju zelite da kupite: ")
                while pogresan_unosKolicine(kolicina, i["Kolicina"]):
                    kolicina = input("Unesite kolicinu koju zelite da kupite: ")
                i["Kolicina"] -= int(kolicina)
                if i["Naziv"] in kupljeni_instrumenti:
                    kupljeni_instrumenti[i["Naziv"]] += int(kolicina)
                else:
                    kupljeni_instrumenti[i["Naziv"]] = int(kolicina)
                ukupna_cijena += i["Cijena"] * int(kolicina)
                ucitavanje_korisnika.snimi_instrumente(instrumenti)
    if ukupna_cijena == 0:
        return
    print("Kupovina uspjesna! Kupili ste: ")
    for i in kupljeni_instrumenti:
        print("Instrument: " + i + " x " + str(kupljeni_instrumenti[i]) + " = " +
              ukupan_trosak(i,kupljeni_instrumenti[i], instrumenti))


    print("Ukupno za uplatu: " + str(ukupna_cijena))
    print()

    while True:
        uplaceno = input("Unesite iznos sume koju uplacujete: ")
        try:
            if float(uplaceno) < ukupna_cijena:
                print("Nedovoljan iznos uplacene sume!")
                continue
        except:
            print("Molimo vas da unesete cjelobrojni iznos")
            continue
        break
    uplaceno = float(uplaceno)
    instrmnt = ""
    for i in kupljeni_instrumenti:
        instrmnt += (i + ",") * kupljeni_instrumenti[i]
    instrmnt = instrmnt[:len(instrmnt) - 1]
    m = {"Sifra": nova_sifra, "Kupljeni instrumenti": instrmnt, "Korisnicko ime kupca": korisnicko_ime,
         "Uplata": uplaceno, "Ukupna cijena": ukupna_cijena, "Kusur": uplaceno - ukupna_cijena,
         "Datum i vrijeme kupovine": datum_vrijeme}
    racuni.append(m)
    ucitavanje_korisnika.snimi_racune(racuni)


def ukupan_trosak(instrument, kolicina, instrumenti):

    #Kao parametar prima naziv instrumenta, kupljenu kolicinu, listu instrumenata
    #Funkcija sluzi za racunanje ukupne cene kostanja zadatog instrumenta

    for i in instrumenti:
        if i["Naziv"] == instrument:
            kol = kolicina * i["Cijena"]
            return str(kol)


def nova_sifraRacuna(racuni):

    # Kao parametar prima listu racuna
    # Funkcija sluzi za generisanje naredne sifre racuna

    naredni = max([int(x["Sifra"][1:]) for x in racuni])
    return "R" + str(naredni + 1)


def vrati_zaNaziv(naziv, instrumenti, tipovi_instrumenata):

    # Kao parametar prima naziv instrumenta, listu instrumenata, i tipove instrumenata
    # Funkcija za zadato ime, vraca sifru proizvodjaca cenu i tip instrumenta

    vraca = []
    for i in instrumenti:
        if naziv == i["Naziv"]:
            vraca.append(i["Sifra"])
            vraca.append(i["Proizvodjac"])
            vraca.append(i["Cijena"])
            for j in tipovi_instrumenata:
                if i["Tip inst."] == j["Sifra"]:
                    vraca.append(j["Naziv"])
                    return vraca


def prethodno_kupljeno(kupac, instrumenti, tipovi_instrumenata, racuni):

    # Kao parametar prima trenutnog kupca, listu instrumenata, tipove,racune
    # Funkcija prikazuje sve kupovine trenutnog ulogovanog kupca

    kupio = []
    for i in racuni:
        if i["Korisnicko ime kupca"] == kupac["Korisnicko ime"]:
            brojac = dict(Counter(i["Kupljeni instrumenti"].split(",")))
            for j in brojac:
                q = vrati_zaNaziv(j, instrumenti, tipovi_instrumenata)
                kupio.append(
                    {"Sifra inst.": q[0], "Naziv inst.": j, "Proizvodjac": q[1], "Tip inst.": q[3],
                     "Cijena": str(brojac[j] * q[2]) + "(" + str(brojac[j]) + " x " + str(q[2]) + ")",
                     "Datum i vrijeme kupovine": i["Datum i vrijeme kupovine"]})
    zajednicki.ispisi_tabelu(kupio)