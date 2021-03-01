# 4 v vrsto

__Igrica štiri v vrsto proti računalniku__

Projekt pri računalništvu, 2. letnik fizike, FMF UL.

__Potrebne knjižnice__

Za zagon lokalnega serverja je potrebna knjižnica

    bottle.py

in pa

    python3

__Delovanje__

Na (lokalni) spletni strani igralec najprej vpiše svoje ime, nato izbere težavnost nasprotnika (5 težavnosti) in barvo žetonov, ter nato igra igro štiri v vrsto proti računalniku. Za vsa sporočila igralcu, je igralec nazvan po imenu.
Koda, ki robotom narekuje kateri stolpec izberejo, je v

    cela_igra

Najlažji robot izbira stolpce naključno, naslednji izbira naključno med stolpci v katerega smo mi odvrgli zadnji žeton ter levim in desnim stolpcem. Najtežji trije leveli upoštevajo tudi preprečevanje naših "štiric" in iščejo svoje. Če "štiric" ni, predzadnja težavnost upošteva preprečevanje "trojic" nasprotnika in iskanje svojih, zadnja težavnost pa dodatno upošteva še, da so robni žetoni manj vredni (v manj strani lahko zmagamo) in se jim zato izogiba.

__Zagon__

Za zagon poženete

    4_v_vrsto_streznik

ki vam izpiše lokalni spletni naslov. Na tem naslovu nato lahko igrate igrico.

__Viri__

Za pisanje projekta sem uporabljal dokumentacijo za bottle.py in predavanja doc. dr. Matije Pretnarja pri predmetu uvod v programiranje.
