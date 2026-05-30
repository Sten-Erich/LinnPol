from random import shuffle

class Kaart:
    mastid = ["ruutu", "risti", "ärtu", "poti"]
    väärtus = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "poiss", "emand","kunn","äss"]
    
    def __init__(self, v, s):
        self.väärt = v
        self.mast = s

    def __lt__(self, suva): #väiksem kui võrdlemine
        if self.väärt < suva.väärt:
            return True
        if self.väärt == suva.väärt:
            if self.mast < suva.mast:
                return True
            else:
                return False
        return False
    
    def __gt__(self, suva): #suurem kui võrdlemine
        if self.väärt > suva.väärt:
            return True
        if self.väärt == suva.väärt:
            if self.mast > suva.mast:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v = self.väärtus[self.väärt] + " " + self.mastid[self.mast]
        return v

class Pakk:
    def __init__(self):
        self.kaardid = []
        for i in range(2, 15):
            for j in range(4):
                self.kaardid.append(Kaart(i, j))
        shuffle(self.kaardid)
    
    def rm_kaart(self):
        if len(self.kaardid) == 0:
            return
        return self.kaardid.pop()
    
class Mängija:
    def __init__(self, nimi):
        self.võit = 0
        self.kaart = None
        self.nimi = nimi

class Mäng:
    def __init__(self):
        nimi1 = input("Esimese mängija nimi: ")
        nimi2 = input("Teise mängija nimi: ")
        self.pakk = Pakk()
        self.p1 = Mängija(nimi1)
        self.p2 = Mängija(nimi2)
    def võit(self, võitja):
        w = "{} võitis selle lahingu".format(võitja)
        print(w)
    def tõmbamine(self, p1n, p1c, p2n, p2c):
        d = "{} tõmbas {} ja {} tõmbas {}".format(p1n, p1c, p2n, p2c)
        print(d)
    
    def mängimine(self):
        kaardid = self.pakk.kaardid
        print("Alustame mängimist!")
        while len(kaardid) >= 2:
            m = "Vajuta 'q' et mäng lõpetada. Vajuta muud nuppu, et jätkata: "
            vastus = input(m)
            if vastus == 'q':
                break
            p1c = self.pakk.rm_kaart()
            p2c = self.pakk.rm_kaart()
            p1n = self.p1.nimi
            p2n = self.p2.nimi
            self.tõmbamine(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.võit += 1
                self.võit(self.p1.nimi)
            else:
                self.p2.võit += 1
                self.võit(self.p2.nimi)
        
        võit = self.võitja(self.p1, self.p2)
        print("Mängu lõpp. {} võitis".format(võit))
    
    def võitja(self, p1, p2):
        if self.p1.võit > self.p2.võit:
            return self.p1.nimi
        if self.p1.võit < self.p2.võit:
            return self.p2.nimi
        return "Viik"

mäng = Mäng()
mäng.mängimine()