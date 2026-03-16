
from keres import *
class Királynő(Feladat):
    def __init__(self,ke,c):
        self.kezdő=ke;
        self.cél=c;
        self.N=len(ke)-1
    def célteszt(self,a): #a = (a1,a2,...,an,s)
        return a[self.N] == self.cél

    def rákövetkező(self,a):
        gyerekek=[]
        s=a[self.N] # ebbe a sorba probálok rakni

        for i in range(1,self.N+1):
            elofeltetel=True # lerak (s, i) alkalmazható?
            for m in range(1,s): #bármely m<s esetén
                if a[m-1]!=i and abs(m-s) != abs (a[m-1]-i):
                    #elofeltetel=True
                    pass
                else:
                    elofeltetel=False
                    break

            if elofeltetel:
                uj_allapot=list(a)
                uj_allapot[s-1]=i
                uj_allapot[self.N]=s+1
                gyerekek.append(("operátor",tuple(uj_allapot)))

        return gyerekek





if __name__ == '__main__':
   feladat= Királynő((0,0,0,0,0,0,0,0,1),9)
   print("szélességi kereső")
   result1 = szelessegi_grafkereso(feladat)
   print(result1.megoldás())
   utam = result1.út()
   utam.reverse()
   print(utam)