import bottle
import pathlib
import os

from cela_igra import *

pot = os.path.join(pathlib.Path(__file__).parent.absolute(), "views")

d = Igra((7, 6), 0, [], [], prosti=[0 for i in range(7)], kam=(0, 0))


@bottle.get("/")
def predstavi():
    return bottle.template(os.path.join(pot, "poimenuj.tpl"))


@bottle.post("/poimenuj/")
def preusmeri():
    a = bottle.request.forms.a
    return bottle.template(os.path.join(pot, "preusmeri.tpl"), ime=a)


@bottle.post("/<ime>/")
def pozdravi(ime):
    return bottle.template(os.path.join(pot, "level.tpl"), ime=ime)


@bottle.post("/<ime>/<level>/")
def izbira_parametrov(ime, level):
    return bottle.template(os.path.join(pot, "igralec.tpl"),
                           ime=ime, level=level)


@bottle.post("/<ime>/<level>/<igralec>/")
def prva_poteza(ime, level, igralec):
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

    z = []
    for i in range(d.velikost[1] - 1, -1, -1):
        b = "   "
        for j in range(d.velikost[0]):
            if (j, i) in d.rdeci:
                b = b + "&#128308;&#160;&#160;&#160;"
            elif (j, i) in d.rumeni:
                b = b + "&#128309;&#160;&#160;&#160;"
            else:
                b = b + "&#9898;&#160;&#160;&#160;"
        z.append(b)

    return bottle.template(os.path.join(pot, "poteza.tpl"), ime=ime,
                           level=level, igralec=igralec, tabela=tuple(z))


@bottle.post("/<ime>/<level>/<igralec>/<opcija>/")
def naslednje_poteze(ime, level, igralec, opcija):
    if int(opcija) not in d.kam_lahko():
        z = []
        for i in range(d.velikost[1] - 1, -1, -1):
            b = "   "
            for j in range(d.velikost[0]):
                if (j, i) in d.rdeci:
                    b = b + "&#128308;&#160;&#160;&#160;"
                elif (j, i) in d.rumeni:
                    b = b + "&#128309;&#160;&#160;&#160;"
                else:
                    b = b + "&#9898;&#160;&#160;&#160;"
            z.append(b)
        tabela = tuple(z)
        return bottle.template(os.path.join(pot, "poteza.tpl"), ime=ime,
                               level=level, igralec=igralec, tabela=tuple(z))

    else:
        d.dodaj(int(opcija))

    z = []
    for i in range(d.velikost[1] - 1, -1, -1):
        b = "   "
        for j in range(d.velikost[0]):
            if (j, i) in d.rdeci:
                b = b + "&#128308;&#160;&#160;&#160;"
            elif (j, i) in d.rumeni:
                b = b + "&#128309;&#160;&#160;&#160;"
            else:
                b = b + "&#9898;&#160;&#160;&#160;"
        z.append(b)
    tabela = tuple(z)

    if d.zmaga():  # igralec je zmagal
        return bottle.template(os.path.join(pot, "zmaga.tpl"),
                               ime=ime, tabela=tabela)

    if d.prosti == [d.velikost[1] for i in range(d.velikost[0])]:
        # vse polno-> izenačenje
        return bottle.template(os.path.join(pot, "polno.tpl"), ime=ime,
                               level=level, igralec=igralec, tabela=tuple(z))

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

    z = []
    for i in range(d.velikost[1] - 1, -1, -1):
        b = "   "
        for j in range(d.velikost[0]):
            if (j, i) in d.rdeci:
                b = b + "&#128308;&#160;&#160;&#160;"
            elif (j, i) in d.rumeni:
                b = b + "&#128309;&#160;&#160;&#160;"
            else:
                b = b + "&#9898;&#160;&#160;&#160;"
        z.append(b)

    if d.zmaga():  # igralec je zmagal
        return bottle.template(os.path.join(pot, "poraz.tpl"),
                               ime=ime, tabela=tuple(z))

    if d.prosti == [d.velikost[1] for i in range(d.velikost[0])]:
        # vse polno-> izenačenje
        return bottle.template(os.path.join(pot, "polno.tpl"), ime=ime,
                               level=level, igralec=igralec, tabela=tuple(z))

    else:
        return bottle.template(os.path.join(pot, "poteza.tpl"), ime=ime,
                               level=level, igralec=igralec, tabela=tuple(z))


bottle.run(debug=True, reloader=True)