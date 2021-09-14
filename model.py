import random


class Matrika:

    def __init__(self, polja=None):
        if polja is None:
            self.polja = []
        else:
            self.polja = polja[:]

    def __str__(self):
        lepsa_matrika = ""
        for vrstica in self.polja:
            lepsa_matrika += ' '.join([str(x) for x in vrstica]) + "\n"
        return lepsa_matrika

    def __repr__(self):
        izpis = f'Matrika({str(self.polja)})'
        return izpis

    def identiteta(self, n):
        """
        Metoda, ki ti vrne kvadratno matriko, velikosti n, ki je sestavljena s samih ničel, le po diagonali ima enice.
        """
        mat = [[0 for i in range(n)] for j in range(n)]   # izpeljani seznami
        for i in range(n):
            mat[i][i] = 1
        self.polja = mat
        return None

    def transponiraj(self):
        """
        Metoda, ki matriki priredi novo matriko, pri kateri so vrstice iz prve matrike postavljene v stolpce.
        """
        m = len(self.polja)
        n = len(self.polja[0])         # stolpci
        transponiranka = []
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append(self.polja[j][i])
            transponiranka.append(vrstica)
        return Matrika(transponiranka)

    def _enaka_velikost(self, other):
        """
        Metoda, ki preveri, ali sta dani matriki enakih dimenzij.
        """
        polja1 = self.polja
        polja2 = other.polja
        return len(polja1) == len(polja2) and len(polja1[0]) == len(polja2[0])

    def _preverba_kvadratnosti(self):
        if len(self.polja) != len(self.polja[0]):
            raise Exception("Prišlo je do napake! Matrika ni kvadratna.")

    def __add__(self, other):
        """
        Metoda, ki sešteje dani matriki.

        Pazi, da sta matriki enakih dimenzij!
        """
        m = len(self.polja)
        n = len(self.polja[0])
        vsota = []
        if self._enaka_velikost(other):
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self.polja[i][j] + other.polja[i][j])
                vsota.append(vrstica)
            return Matrika(vsota)
        else:
            raise Exception('Matriki nista ustreznih velikosti, da bi se izvedla ta operacija.')

    def __sub__(self, other):
        """
        Metoda, ki odšteje dani matriki.
        
        Pazi, da sta matriki enakih dimenzij!
        """
        m = len(self.polja)
        n = len(self.polja[0])
        razlika = []
        if self._enaka_velikost(other):
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self.polja[i][j] - other.polja[i][j])
                razlika.append(vrstica)
            return Matrika(razlika)
        else:
            raise Exception('Matriki nista ustreznih velikosti, da bi se izvedla ta operacija.')

    def __mul__(self, other):
        """
        Metoda, ki zmnoži dani matriki.

        Pazi, da je število vrstic prve matrike enako številu stolpcev druge matrike.
        """
        matrika = []
        if len(self.polja[0]) == len(other.polja):            # pogoj
            for i in range(len(self.polja)):
                vrstica = []
                for j in range(len(other.polja)):
                    vsota = 0
                    for k in range(len(self.polja[i])):
                        vsota += self.polja[i][k] * other.polja[k][j]
                    vrstica.append(vsota)
                matrika.append(vrstica)
            return Matrika(matrika)
        else:
            return print('Matriki nista ustreznih velikosti, da bi se izvedla ta operacija.')

    def nicelna_matrika(self, n):
        """
        Metoda, ki vrne kvadratno matriko, velikosti n, sestavljeno iz samih ničel
        """
        mat = [[0 for i in range(n)] for j in range(n)]
        self.polja = mat
        return None

    def sled_matrike(self):
        """
        Metoda, ki sešteje diagonalne elemente v matriki.

        Pazi, da je matrika kvadratna!
        """
        self._preverba_kvadratnosti()
        sled = 0
        for i in range(len(self.polja)):
            sled += self.polja[i][i]
        return Matrika(sled)

    @staticmethod
    def poljubna_matrika(st_vrstic, st_stolpcev):
        """
        Metoda, ki ti vrne matriko, ki ima za elemente naključna števila med 0 in 999.
        """
        matrika = []
        for i in range(st_vrstic):
            vrstica = []
            for j in range(st_stolpcev):
                vrstica.append(random.randint(0, 999))
            matrika.append(vrstica)
        return matrika


def preberi_matriko_iz_niza(niz):
    vrstice = niz.strip().split('\n')
    mat = []
    for vrstica in vrstice:
        elementi_vrstice = vrstica.split(' ')
        elementi_vrstice = [int(element) for element in elementi_vrstice]
        mat.append(elementi_vrstice)
    return Matrika(mat)

##########################################


# matr1 = Matrika()
matr1 = [[1, 4, 6], [7, 8, 3], [0, 0, 9]]

m3 = Matrika()
m3.nicelna_matrika(8)
# sled_matrike

# m1 = Matrika()
# a = m1.identiteta(3)
# m2 = Matrika()
# m2.identiteta(3)


# matr2 = [[9, 2, 6], [7, 0, 1], [8, 3, 9]]
# matr3 = [[1,6], [7,6]]
