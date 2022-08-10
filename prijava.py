import ucitavanje_korisnika
import radnici_modul
import kupci_modul
import menadzer_modul
import zajednicki
import getpass
import time


def prijava():

    # Funkcija za prijavu korisnika

    pokusaji = 0
    korisnici = ucitavanje_korisnika.ucitaj_korisnike()
    instrumenti = ucitavanje_korisnika.ucitaj_muzickeInstrumente()
    tipovi_instrumenata = ucitavanje_korisnika.ucitaj_tipoveInstrumenata()
    racuni = ucitavanje_korisnika.ucitaj_racune()
    while True:
        pogresni_podaci = True
        ime = input("Molimo vas, unesite korisnicko ime: ")
        sifra = getpass.getpass('Molimo vas, unesite sifru: ')
        for i in range(len(korisnici)):

            if korisnici[i]["Korisnicko ime"] == ime and korisnici[i]["Sifra"] == sifra:
                pogresni_podaci = False

                if korisnici[i]["Uloga"] == "radnik":
                    print("Uspjesno ste se prijavili kao korisnik radnik: " + korisnici[i]["Ime"] + " " + korisnici[i][
                        "Prezime"])
                    radnici_modul.opcije_radnik(instrumenti, tipovi_instrumenata)
                    print("Upjesno ste se izlogovali")
                    return
                elif korisnici[i]["Uloga"] == "menadzer":
                    print("Uspjesno ste se prijavili kao korisnik menadzer: " + korisnici[i]["Ime"] + " " + korisnici[i][
                        "Prezime"])
                    menadzer_modul.opcije_menadzer(korisnici, instrumenti, tipovi_instrumenata, racuni)
                    print("Uspjesno ste se izlogovali")
                    return
                elif korisnici[i]["Uloga"] == "kupac":
                    print("Uspjesno ste se prijavili kao korisnik kupac: " + korisnici[i]["Ime"] + " " + korisnici[i][
                        "Prezime"])
                    kupci_modul.opcije_kupac(korisnici[i], instrumenti, tipovi_instrumenata, racuni)
                    print("Upjesno ste se izlogovali")
                    return
        if pogresni_podaci:
            print("Zao nam je, podaci su pogresni. Pokusajte ponovo!")
            pokusaji += 1
            if pokusaji == 3:
                print()
                print("Zao nam je, iskoristili ste maksimalan broj pokusaja za prijavu. ")
                print("Program ce se sada ugasiti!")
                time.sleep(4)
                exit()


def registracija_korisnika(korisnici):

    # Kao parametar primamo listu svih korisnika
    # Funkcija za registrovanje novog kupca

    korisnicko_ime = ""
    while True:
        korisnicko_ime = input("Molimo vas, unesite korisnicko ime: ")
        if len(korisnicko_ime.strip()) == 0:
            print("Zao nam je, korisnicko ime ne moze biti prazno polje!")
            continue
        if zajednicki.provjera_jedinstvenogImena(korisnicko_ime, korisnici):
            break
        else:
            print("Zao nam je, unijeto korisnicko ime vec postoji!")

    sifra = getpass.getpass("Molimo vas, unesite lozinku: ")
    while len(sifra.strip()) == 0:
        sifra = getpass.getpass("Molimo vas, unesite lozinku: ")

    ime = input("Molimo vas, unesite ime: ")
    while len(ime.strip()) == 0:
        print("Zao nam je, unos je pogresan. Pokusajte ponovo!")
        ime = input("Molimo vas, unesite ime: ")

    prezime = input("Molimo vas, unesite prezime: ")
    while len(prezime.strip()) == 0:
        print("Zao nam je, unos je pogresan. Pokusajte ponovo!")
        prezime = input("Molimo vas, unesite prezime: ")

    file = open("korisnici.txt", "a")
    novo = "\n" + korisnicko_ime + "|" + sifra + "|" + ime + "|" + prezime + "|" + "kupac"
    file.write(novo)
    file.close()


def main():

    # Main funkcija pokrece program

    korisnici = ucitavanje_korisnika.ucitaj_korisnike()
    print(" |##########| DOBRODOSLI U PRODAVNICU |##########|")
    print()
    while True:
        print("|1| >> Registracija novog korisnika")
        print("|2| >> Prijava")
        print("|3| >> Izlaz")
        izbor = input(">>> ")
        if izbor == "1":
            registracija_korisnika(korisnici)
        elif izbor == "2":
            prijava()
        elif izbor == "3":
           break
        else:
            print("Zao nam je, unos je pogresan. Pokusajte ponovo.")

    print("Izasli ste iz prodavnice. DOVIDJENJA! :-)")
    time.sleep(4)



main()
