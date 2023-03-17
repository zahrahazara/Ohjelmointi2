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



# Luo yksi auto ja kiihdytä sen nopeutta
auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
print("Auton nopeus:", auto.nopeus)

# Kiihdytä autoa lisää ja tee hätäjarrutus
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)
print("Auton nopeus hätäjarrutuksen jälkeen:", auto.nopeus)
