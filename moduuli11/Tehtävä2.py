class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntimaara):
        self.matkamittari += tuntimaara * self.huippunopeus

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

# Esimerkki käytöstä:
sahkoauto = Sahkoauto('ABC-15', 180, 52.5)
sahkoauto.aja(3)
print(f"Sähköauton matkamittari: {sahkoauto.matkamittari} km")

polttomoottoriauto = Polttomoottoriauto('ACD-123', 165, 32.3)
polttomoottoriauto.aja(3)
print(f"Polttomoottoriauton matkamittari: {polttomoottoriauto.matkamittari} km")

