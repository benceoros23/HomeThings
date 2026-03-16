from keres import *
class Hanoi(Feladat): # öröklődés
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c

    def célteszt(self, a):  # a=(a1,a2,..., an)
        return a == self.cél

    def rákövetkező(self, a):
        gyerekek = []
        n = len(a)  # korongok száma
        for melyiket in range(0, n):
            for hova in ['P', 'Q', 'R']:  # átrak melyiket hova
                tmp = True
            if a[melyiket] != hova:
                for i in range(0, melyiket):
                    if a[i] != a[melyiket] and a[i] != hova:
                        tmp = True
                else:
                    tmp = False
                    break
            else:
                tmp = False

            if tmp == True:
                uj_allapot = list(a)
                uj_allapot[melyiket] = hova
                gyerekek.append(("operator",tuple(uj_allapot)))

        return gyerekek


if __name__ == '__main__':
    feladat = Hanoi(('P', 'P', 'P', 'P', 'P'), ('R', 'R', 'R', 'R', 'R'))
    print("mélységi kereső")
    result1 = melysegi_fakereso(feladat)
    print(result1.megoldás())
    utam = result1.út()
    utam.reverse()
    print(utam)
