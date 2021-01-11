import bottle

from cela_igra import *



pot_do_views = r"C:\Users\mihar\OneDrive\Namizje\2.letnik\racunalnistvo\projekt\4VVrsto\views"
d = Igra((7, 6), 0, [], [], prosti=[0 for i in range(7)], kam = (0,0))

@bottle.get("/")
def predstavi():
    return bottle.template(pot_do_views + r"\poimenuj")

@bottle.post("/poimenuj/")
def preusmeri():
    a = bottle.request.forms["a"]
    return bottle.template(pot_do_views + r"\preusmeri", ime = a)

@bottle.post("/<ime>/")
def pozdravi(ime):
    return bottle.template(pot_do_views + r"\level", ime = ime)

@bottle.post("/<ime>/<level>/")
def izbira_parametrov(ime, level):
    return bottle.template(pot_do_views + r"\igralec", ime = ime, level = level)

@bottle.post("/<ime>/<level>/<igralec>/")
def prva_poteza(ime, level, igralec):
    """e = Igra((7, 6), 0, [], [], prosti=[0 for i in range(7)], kam = (0,0))
    d = e"""
    d.poteza = 0
    d.rdeci = []
    d.rumeni = []
    d.prosti = [0 for i in range(7)]


    if igralec == "2":
        if level == "zelo lahko":
            n = (robot1(d))
        elif level == "lahko":
            n = (robot2(d))
        elif level == "srednje":
            n = (robot3(d))
        elif level == "težje":
            n = (robot4(d))
        else:
            n = (robot5(d))
        d.dodaj(n)
    rd = (d.rdeci)
    ru = (d.rumeni)
    op = (d.kam_lahko())

    z = []
    for i in range(d.velikost[1] - 1, -1, -1):
        b = "|"
        for j in range(d.velikost[0]):
            if (j, i) in d.rdeci:
                b = b +"_O_|"
            elif (j, i) in d.rumeni:
                b = b + "_#_|"
            else:
                b = b + "___|"
        z.append(b)

        
    return bottle.template(pot_do_views + r"\poteza", ime = ime, level = level, igralec = igralec, tabela = tuple(z), opcije = tuple(op))

@bottle.post("/<ime>/<level>/<igralec>/<opcija>/")
def naslednje_poteze(ime, level, igralec, opcija):
    d.dodaj(int(opcija))

    rd = (d.rdeci)
    ru = (d.rumeni)
    op = (d.kam_lahko())

    z = []
    for i in range(d.velikost[1] - 1, -1, -1):
        b = "|"
        for j in range(d.velikost[0]):
            if (j, i) in d.rdeci:
                b = b +"_O_|"
            elif (j, i) in d.rumeni:
                b = b + "_#_|"
            else:
                b = b + "___|"
        z.append(b)
    tabela = tuple(z)

    if d.zmaga(): #igralec je zmagal
        return bottle.template(pot_do_views + r"\zmaga", ime = ime, tabela = tabela)

    if d.prosti == [d.velikost[1] for i in range(d.velikost[0])]:
        #vse polno-> izenačenje
        return bottle.template(pot_do_views + r"\polno", ime = ime, level = level, igralec = igralec, tabela = tuple(z))

    else:
        if level == "zelo lahko":
            n = (robot1(d))
        elif level == "lahko":
            n = (robot2(d))
        elif level == "srednje":
            n = (robot3(d))
        elif level == "težje":
            n = (robot4(d))
        else:
            n = (robot5(d))
        d.dodaj(n)

    rd = (d.rdeci)
    ru = (d.rumeni)

    z = []
    for i in range(d.velikost[1] - 1, -1, -1):
        b = "|"
        for j in range(d.velikost[0]):
            if (j, i) in d.rdeci:
                b = b +"_O_|"
            elif (j, i) in d.rumeni:
                b = b + "_#_|"
            else:
                b = b + "___|"
        z.append(b)

    if d.zmaga(): #igralec je zmagal
        return bottle.template(pot_do_views + r"\poraz", ime = ime, tabela = tuple(z))

    if d.prosti == [d.velikost[1] for i in range(d.velikost[0])]:
        #vse polno-> izenačenje
        return bottle.template(pot_do_views + r"\polno", ime = ime, level = level, igralec = igralec, tabela = tuple(z))

    
    else:
        op = (d.kam_lahko())
        return bottle.template(pot_do_views + r"\poteza", ime = ime, level = level, igralec = igralec, tabela = tuple(z), opcije = tuple(op))


bottle.run(debug = True, reloader = True)