import random
from prettytable import PrettyTable

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        matka = self.nopeus * tuntimaara
        self.kuljettu_matka += matka

    def __str__(self):
        return f"Auto {self.rekisteritunnus}: nopeus {self.nopeus} km/h, kuljettu matka {self.kuljettu_matka} km"

# Luo lista kymmenestä autosta
autot = []
for i in range(10):
    rekisteritunnus = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

# Kilpailu
while True:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            break
    else:
        continue
    break

# Tulosta tulokset
print("Kilpailun tulokset:")
print("====================")
table = PrettyTable()
table.field_names = ["Rekisteritunnus", "Huippunopeus", "Nopeus", "Matka"]

# Lisää autojen tiedot taulukkoon
for auto in autot:
    table.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka])

print(table)