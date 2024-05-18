from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalt_datumok = []

    def foglalas(self, datum):
        self.foglalt_datumok.append(datum)
        print(f"{self.szobaszam} szoba foglalva {datum} dátumra.")

    def lemondas(self, datum):
        if datum in self.foglalt_datumok:
            self.foglalt_datumok.remove(datum)
            print(f"{self.szobaszam} szoba foglalása törölve {datum} dátumról.")
        else:
            print(f"Nincs foglalás ezen a dátumon a(z) {self.szobaszam} szobára.")

    def ellenorzes(self, datum):
        return datum not in self.foglalt_datumok

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = {}

    def szoba_hozzaadasa(self, szobaszam, ar):
        self.szobak[szobaszam] = Szoba(szobaszam, ar)

    def foglalas(self, szobaszam, datum):
        if szobaszam in self.szobak:
            szoba = self.szobak[szobaszam]
            if szoba.ellenorzes(datum):
                szoba.foglalas(datum)
            else:
                print("Ez a szoba már foglalt ekkorra.")
        else:
            print("Nincs ilyen szoba a szállodában.")

    def lemondas(self, szobaszam, datum):
        if szobaszam in self.szobak:
            self.szobak[szobaszam].lemondas(datum)
        else:
            print("Nincs ilyen szoba a szállodában.")

    def foglalasok_listazasa(self):
        print("Foglalt szobák:")
        for szobaszam, szoba in self.szobak.items():
            if szoba.foglalt_datumok:
                print(f"{szobaszam}: {', '.join(map(str, szoba.foglalt_datumok))}")
            else:
                print(f"{szobaszam}: Nincs foglalás.")

def main():
    szalloda = Szalloda("Példa Szálloda")
    szalloda.szoba_hozzaadasa("101", 7000)
    szalloda.szoba_hozzaadasa("201", 6500)
    szalloda.szoba_hozzaadasa("202", 8500)

    szalloda.foglalas("101", datetime(2024, 6, 10))
    szalloda.foglalas("201", datetime(2024, 7, 25))
    szalloda.foglalas("201", datetime(2024, 6, 27))
    szalloda.foglalas("202", datetime(2024, 6, 7))
    szalloda.foglalas("202", datetime(2024, 7, 18))

    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Művelet kiválasztása: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalandó szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            szalloda.foglalas(szobaszam, datum)

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondandó foglalás szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            szalloda.lemondas(szobaszam, datum)

        elif valasztas == "3":
            szalloda.foglalasok_listazasa()

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen művelet.")

if __name__ == "__main__":
    main()