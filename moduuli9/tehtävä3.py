import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
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



# Autojen luonti ja alustus
auto_lista = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    auto_lista.append(auto)

# Auton nopeuden muutokset ja kuljetun matkan päivitys
for auto in auto_lista:
    auto.kiihdytä(30)
    auto.kulje(1)
    auto.kiihdytä(70)
    auto.kulje(1)
    auto.kiihdytä(50)
    auto.kulje(1)
    print(f"{auto.rekisteritunnus} nopeus: {auto.nopeus} km/h")