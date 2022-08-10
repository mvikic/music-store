import operator
import copy


def provjera_jedinstvenogImena(korisnicko_ime, korisnici):

    # Funkcija kao parametre prima unijeto korisnicko ime, i listu korisnika
    # Provjeravamo da li se unijeto korisnicko ime vec nalazi u sistemu


    for i in korisnici:
        if korisnicko_ime == i["Korisnicko ime"]:
            return False
    return True


def ukloni_obrisane(svi):

    # Funkcija kao parametar prima listu rijecnika instrumenata,
    # i izbacuje sve koji su obrisani i cija je kolicina na lageru 0

    odg = []
    privr = copy.deepcopy(svi)
    for i in privr:
        if i["Obrisano logicki"] == "False":
            del i["Obrisano logicki"]
            if i["Kolicina"] > 0:
                odg.append(i)
    return odg


def uzimanje_duzineZaglavlja(entiteti):

    # Funkcija za zadatu listu rjecnika, odredjuje maksimalnu duzinu
    # svake kolone, kako bi ispis u tabeli bio formatiran

    if len(entiteti) == 0:
        return "Nema pronadjenih rezultata"
    A = []
    for i in range(len(entiteti[0])):
        A.append([])
    j = 0
    for i in (entiteti[0]):
        A[j].append(len(i))
        j += 1
    for i in range(len(entiteti)):
        br = 0
        for j in entiteti[i]:
            A[br].append(len(str(entiteti[i][j])))
            br += 1
    B = []
    for i in A:
        B.append(max(i))
    return B


def ispisi_tabelu(lista_entiteta):

    # Funkcija prima listu rijecnika, i ispisuje ih u tabelarnom prikazu

    proba = lista_entiteta

    lista = uzimanje_duzineZaglavlja(proba)
    if type(lista) == str:
        print(lista)
        return
    zaglavlje = list(proba[0].keys())
    duzina_crtica = (sum(lista) + len(zaglavlje) + 1)

    q = "|"
    print("-" * duzina_crtica)
    for i in range(len(zaglavlje)):
        q += "{zaglavlje[" + str(i) + "]:^{lista[" + str(i) + "]}}|"
    print(q.format(zaglavlje=zaglavlje, lista=lista))
    for i in range(len(proba)):
        print("-" * duzina_crtica)
        q = "|"
        for j in range(len(zaglavlje)):
            q += "{AD[" + str(j) + "]:^{lista[" + str(j) + "]}}|"
        print(q.format(lista=lista, AD=list(proba[i].values())))
    print("-" * duzina_crtica)

def zamijeni_TipoveZaNaziv(kopija, tipovi):

    # Funkcija prima listu instrumenata i listu tipova instrumenata
    # i svaka sifra tipa instrumenta u listi instrumenata se zamjenjuje sa nazivom tipa insturmenta

     for i in kopija:
        for j in tipovi:
            if j["Sifra"] == i["Tip inst."]:
                i["Tip inst."] = j["Naziv"]


def prikaz_svihInstrumenata(uloga, instrumenti, tipovi):

    # Funkcija prima ulogu kao karakter, listu instrumenata i listu tipova instrumenata
    # i prikazuje sve instrumente u sistemu sortirane po odredjenom kriterijumu

    kopija = copy.deepcopy(instrumenti)
    if uloga == "K":
        kopija = ukloni_obrisane(kopija)

    print("(1) Sortiraj po sifri")
    print("(2) Sortiraj po nazivu")
    print("(3) Sortiraj po proizvodjacu")
    print("(4) Sortiraj po tipu instrumenta")
    odabrana_opcija = input(">>> ")
    if odabrana_opcija == "1":
        kopija.sort(key=operator.itemgetter("Sifra"))
    elif odabrana_opcija == "2":
        kopija.sort(key=operator.itemgetter("Naziv"))
    elif odabrana_opcija == "3":
        kopija.sort(key=operator.itemgetter("Proizvodjac"))
    elif odabrana_opcija == "4":
        zamijeni_TipoveZaNaziv(kopija, tipovi)
        kopija.sort(key=operator.itemgetter("Tip inst."))

    ispisi_tabelu(kopija)


def pretrazi(krit_pretrage, parametar, lista):

    #Funkcija prima rijec koja se pretrazuje, kljuc u kojem pretrazujemo, i lista instrumenata


    pretraga = []
    for i in lista:
        if krit_pretrage.lower() in i[parametar].lower():
            pretraga.append(i)
    return pretraga


def pretrazi_sveInstrumente(uloga, instrumenti, tipovi):

    # Funkcija prima ulogu osobe, listu instrumenata, listu tipova
    # zaduzena je za pretragu instrumenata po odredjenom kriterijumu

    kopija = copy.deepcopy(instrumenti)
    if uloga == "K":
        kopija = ukloni_obrisane(kopija)

    print("(1) Pretrazi po sifri")
    print("(2) Pretrazi po nazivu")
    print("(3) Pretrazi po proizvodjacu")
    print("(4) Pretrazi po tipu instrumenta")
    odabrana_opcija = input(">>> ")
    krit_pretrage = input("Unesite rijec za pretragu: ")
    while len(krit_pretrage.strip()) == 0:
        print("Pogresan unos! Probajte ponovo.")
        krit_pretrage = input("Unesite rijec za pretragu: ")
    if odabrana_opcija == "1":
        kopija = pretrazi(krit_pretrage, "Sifra", kopija)
    elif odabrana_opcija == "2":
        kopija = pretrazi(krit_pretrage, "Naziv", kopija)
    elif odabrana_opcija == "3":
        kopija = pretrazi(krit_pretrage, "Proizvodjac", kopija)
    elif odabrana_opcija == "4":
        zamijeni_TipoveZaNaziv(kopija, tipovi)
        kopija = pretrazi(krit_pretrage, "Tip inst.", kopija)

    ispisi_tabelu(kopija)


def provjera_sifreInstrumenta(sifra, instrumenti):

    # Funkcija prima unijetu sifru i listu instrumenata
    # provjerava da li je unijeta sifra jedinstvena

    for i in instrumenti:
        if i["Sifra"] == sifra:
            return False
    return True

