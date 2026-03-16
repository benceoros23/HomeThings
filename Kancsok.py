from keres import *
class Kancsok:
    def __init__(self, ke, c):
        self.kezdő=ke
        self.cél=c
        self.Max1 =3
        self.Max2 = 5
        self.Max3 = 8
    def célteszt(self,a): #a=(a1,a2,a3) állapot
        return a[0]==self.cél or a[1]==self.cél or a[2]==self.cél

    def rákövetkező(self,a): #a=(a1,a2,a3) állapot
        gyerekek=[]
        a1,a2,a3=a

        #tolt1,2 operátor alkalmazasi elofeltetel
        if a1!=0 and a2!=self.Max2:
            T=min(a1,self.Max2-a2)
            gyerekek.append(("tölt 1-ből 2-be",(a1-T,a2+T,a3)))

        # tolt1,3 operátor alkalmazasi elofeltetel
        if a1 != 0 and a3 != self.Max3:
            T = min(a1, self.Max3 - a3)
            gyerekek.append(("tölt 1-ből 3-ba", (a1 - T, a2, a3+5)))

        return gyerekek

if __name__ == '__main__':
   feladat= Kancsok((0,0,8),4)
   print("szélességi kereső")
   result1=szelessegi_fakereso(feladat)
   print(result1.megoldás())
   utam=result1.út()
   utam.reverse()
   print(utam)
