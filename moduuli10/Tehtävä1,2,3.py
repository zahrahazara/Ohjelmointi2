class Hissi:
    def __init__(self, alin_kerros, ylimmän_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimmän_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print("Hissi on kerroksessa", self.kerros)

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros < kohde_kerros:
            self.kerros_ylös()
        while self.kerros > kohde_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylimmän_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            hissi = Hissi(alin_kerros, ylimmän_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_nro, kohde_kerros):
        hissi = self.hissit[hissin_nro - 1]
        hissi.siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)

# Esimerkkikäyttö
talo = Talo(1, 10, 2) # Talossa on 2 hissiä, jotka liikkuvat kerroksilla 1-10
talo.aja_hissiä(1, 5) # Ajetaan hissiä 1 kerrokseen 5
talo.aja_hissiä(2, 8) # Ajetaan hissiä 2 kerrokseen 8
talo.palohälytys() # Kaikki hissit 1 kerrokseen


