import random
from prettytable import PrettyTable


class Auto:
    def __init__(self, merkki, nopeus):
        self.merkki = merkki
        self.nopeus = nopeus
        self.matka = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

        # Simuloidaan satunnainen nopeuden muutos
        nopeuden_muutos = random.randint(-20, 20)
        self.nopeus += nopeuden_muutos


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("{:<10} {:<10} {:<10} {:<10}".format("Merkki", "Matka (km)", "Nopeus (km/h)", "Matka/kokonaispituus"))
        for auto in self.autot:
            print("{:<10} {:<10.1f} {:<10.1f} {:<10.1f}%".format(auto.merkki, auto.matka, auto.nopeus,
                                                                 auto.matka / self.pituus * 100))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False


# Pääohjelma
auto1 = Auto("Toyota", 100)
auto2 = Auto("Ford", 120)
auto3 = Auto("Chevrolet", 90)
auto4 = Auto("Volkswagen", 110)
auto5 = Auto("Audi", 130)
auto6 = Auto("Honda", 95)
auto7 = Auto("Nissan", 105)
auto8 = Auto("BMW", 140)
auto9 = Auto("M_Benz", 125)
auto10 = Auto("Mitsubishi", 85)

autot = [auto1, auto2, auto3, auto4, auto5, auto6, auto7, auto8, auto9, auto10]


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
    elif kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()
        print("Kilpailu ohi!")
