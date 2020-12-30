import random

class Igra:
    def __init__(self, velikost=(7, 6), poteza=0, rdeci=[], rumeni=[], prosti=[0 for i in range(7)], kam=(0,0)):
        self.poteza = poteza
        self.rdeci = rdeci
        self.rumeni = rumeni
        self.velikost = velikost
        self.prosti = prosti
        self.kam = kam

    def __repr__(self, znak1="O", znak2="#"): #kako bo izgledala tabela
        a = "" 
        for i in range(self.velikost[1] - 1, -1, -1):
            a = a + "|"
            for j in range(self.velikost[0]):
                if (j, i) in self.rdeci:
                    a = a + znak1 + "|"
                elif (j, i) in self.rumeni:
                    a = a + znak2 + "|"
                else:
                    a = a + " |"
            a = a + "\n"
        
        return a
    
    def kam_lahko(self): #za robota da ve iz kje izbirati
        a = self.prosti
        b = self.velikost[1]
        c = []
        for i in range(len(a)):
            if a[i] < b:
                c.append(i)
        return c
        

    def kdo_na_potezi(self): #kaksne barve je naslednji žeton
        if self.poteza % 2 == 0:
            return "rdeci"
        else:
            return "rumeni"

    def preveri_ce_lahko(self, n): #damo lahko nekam naslednji zeton?
        if n < 0 or n > self.velikost[0] - 1:
            return False
        elif self.prosti[n] >= self.velikost[1]:
            return False
        else:
            return True

        
    def dodaj(self, n): #že prej preverjeno da to lahko stori in s tem dodamo
        a = self.prosti[n]
        Kam = (n, a)
        if self.kdo_na_potezi() == "rdeci":
            self.rdeci = self.rdeci + [Kam]
        else:
            self.rumeni = self.rumeni + [Kam]
        self.prosti[n] = a + 1
        self.poteza = self.poteza + 1
        self.kam = Kam
        return self



    def zmaga(self): #je dodajanje zadnjega žetona v kam povzročilo zmago?
        if self.kam in self.rdeci:
            vsi = self.rdeci
        else:
            vsi = self.rumeni
        (x, y) = self.kam

        a = b = c = d = [True] 
        for i in range(1, 4):
            a = a + [(x, y - i) in vsi] #dol
            b = [(x - i, y) in vsi] + b + [(x + i, y) in vsi] #desno in levo
            c = [(x - i, y - i) in vsi] + c + [(x + i, y + i) in vsi] #jugozahod-severovzhod
            d = [(x - i, y + i) in vsi] + d + [(x + i, y - i) in vsi] #severozahod-jugovzhod
            
        stirivvrsto = [True, True, True, True]
        if a == stirivvrsto:
            return True
        for i in range(4):
            if b[i : i + 4] == stirivvrsto or c[i : i + 4] == stirivvrsto or d[i : i + 4] == stirivvrsto:
                return True
        return False

#pet robotov različnih jakosti, od 3 naprej dejansko pazi na 4 v vrsto :)
def robot1(igra):
    a = igra.kam_lahko()
    b = random.randint(0, len(a) - 1)
    return a[b]

def robot2(igra):
    a = igra.kam[0]
    b = igra.kam_lahko()
    if a in b:
        c = b.index(a)
        if c == 0 or c == len(b) - 1:
            return robot1(igra)
        else:
            d = b[c - 1: c + 2]
            e = random.randint(0, 2)
            return d[e]
    else:
        return robot1(igra)

def robot3(igra):
    return robot_s_parametri(igra, 1, 0, 3)

def robot4(igra):
    return robot_s_parametri(igra, 1, 3, 3)

def robot5(igra):
    return robot_s_parametri(igra, 3, 3, 3.1)

def robot_s_parametri(igra, s1, s2, s3): #za vsako potezo ovrednoti koliko je dobra glede na različne parametre
    a = igra.prosti
    b = [i for i in a]
    d = Igra(igra.velikost, igra.poteza, igra.rdeci, igra.rumeni, b, igra.kam)
    f = d.kam_lahko() #opcije
    g = [] #sestevanje točk za opcije
    for i in range(len(f)):
        a1 = d.prosti
        b1 = [i for i in a1]
        e = Igra(d.velikost, d.poteza, d.rdeci, d.rumeni, b1, d.kam)
        e.dodaj(f[i])
        #preveri če lahko zmagaš
        if e.zmaga():
            return f[i]
        else:
            tocke = 0
            h = e.kam_lahko() # opcije nasprotnika

            #minus točke za robno
            #minus točke za eno od roba
            if e.kam[0] == 0 or e.kam[0] == e.velikost[0] - 1:
                tocke = tocke - s1
            if e.kam[0] == 1 or e.kam[0] == e.velikost[0] - 2:
                tocke = tocke - (s1 - 1)
            if e.kam[1] == e.velikost[1] - 2: #bolje deluje če mu ne omejimo spodnje vrstice (e.kam[1] == 0)
                tocke = tocke - (s1 - 1)
            if e.kam[1] == e.velikost[1] - 1:
                tocke = tocke - (s1 + 1)

            #točke za tri v vrsto
            tocke = tocke + st_novih_trojk(e) * s2 #popravek parametra

            for j in range(len(h)):
                a2 = e.prosti
                b2 = [i for i in a2]
                k = Igra(e.velikost, e.poteza, e.rdeci, e.rumeni, b2, e.kam)
                k.dodaj(h[j])
                if k.zmaga(): #minus če nasprotnik potem lahko zmaga
                    tocke = tocke - 1000
                tocke = tocke - s3 * st_novih_trojk(k) #minus točke za koliko tri v vrsto lahko naredi nasprotnik z naslednjo potezo

        g.append(tocke)
    #iz seznama tock izberemo najboljsega    
    najvecji = g[0]
    vsinajvecji = [] #če vec z enako zbranimi tockami
    for i in range(len(f)):
        if g[i] == najvecji:
            vsinajvecji.append(i)
        elif g[i] > najvecji:
            vsinajvecji = [i]
            najvecji = g[i]
    
    #če izenačeno random od ostalih
    return f[vsinajvecji[random.randint(0, len(vsinajvecji) - 1)]]

def st_novih_trojk(igra):
    n = 0
    if igra.kam in igra.rdeci:
            vsi = igra.rdeci
    else:
        vsi = igra.rumeni
    (x, y) = igra.kam

    a = b = c = d = [True] 
    for i in range(1, 3):
        a = a + [(x, y - i) in vsi] #dol
        b = [(x - i, y) in vsi] + b + [(x + i, y) in vsi] #desno in levo
        c = [(x - i, y - i) in vsi] + c + [(x + i, y + i) in vsi] #jugozahod-severovzhod
        d = [(x - i, y + i) in vsi] + d + [(x + i, y - i) in vsi] #severozahod-jugovzhod
            
    trivvrsto = [True, True, True]
    if a == trivvrsto:
        n = n + 1
    for i in range(3):
        if b[i : i + 3] == trivvrsto:
            n = n + 1.5
            #popravek parametra za boljšo igro

        if c[i : i + 3] == trivvrsto:
            n = n + 1.3
        if d[i : i + 3] == trivvrsto:
            n = n + 1.3
    return n

def igraj(igra, robot=robot5, igralec=1):
    d = igra
    
    if igra.prosti == [d.velikost[1] for i in range(d.velikost[0])]:
        #vse polno
        return polno(igra)

    if (d.poteza + igralec - 1) % 2 == 0:
        n = inputi(d)
    else:
        n = robot(d)

    d = d.dodaj(n)

    if d.zmaga():
        #nekdo je zmagal
        return konec(d)
    igraj(d)

def konec(igra):
    d = igra
    print(d)
    a = "rdeci"
    if d.kdo_na_potezi() == "rdeci":
        a = "rumeni"
    print("Zmagovalec je {0}!".format(a))
    
    if input("Želite poizkusiti ponovno? (da/ne) ") == "da":
        e = Igra()
        e.prosti = [0 for i in range(e.velikost[0])]
        igraj(e)
    else:
        print("Nasvidenje")  

def inputi(igra):
    d = igra
    print(d)
    n = int(input("V kateri stolpec? ")) - 1
    while not igra.preveri_ce_lahko(n):
        print("Sem nemorete dati žetona, poizkusite ponovno")
        n = int(input("V kateri stolpec torej? ")) - 1
    return n    

def polno(igra):
    d = igra
    print(d)
    print("Izenačenje!")
    if input("Želite poizkusiti ponovno? (da/ne) ") == "da":
        e = Igra()
        e.prosti = [0 for i in range(e.velikost[0])]
        igraj(e)
    else:
        print("Nasvidenje")
        

d = Igra()
igraj(d)
