person=int(input("Hány főre készül az étel?: "))

omlett={"tojás":2,"zsiradék(evőkanál)":1}
bundaskenyer={"tojás":3,"bögre tej":1,"bögre barna cukor":1,"vanília aroma (ek)":1,	"fahéj (tk)":1,"szerecsendió(tk)":1,"szelet kenyér":4,"vaj(dkg)":5,	"bögre barna cukor":1,"bögre tejszín":1}
palacsinta={"liszt(g)":250, "porcukor(ek)":1, "tojás(db)":2, "csipet só":1, "sütőpor(mk)":1, "szódavíz(ml)":250, "tej(ml)":300}
csilisbab={"darált sertéshús(g)":500,"olívaolaj(ek)":2,"nagy db vöröshagyma":1,"gerezd fokhagyma":2,"paradicsomlé(ml)":500,"csemegekukorica(g)":300,"vörösbab(g)":500,"csipet só":1,"teáskanál majoranna":1,"teáskanál oregánó":1,"teáskanál petrezselyem":1,"teáskanál fűszerpaprika":1,"csipet fahéj":1,"teáskanál csípős paprikakrém":1,"worcestershire-szósz(ek)":1}
madartej={"tojásfehérje(db)":4,"csipet só":1,"porcukor(ek)":2,"ml tej":800,"vanília(db)":1,"tojássárgája(db)":4,"cukor(g)":70,"csipet só":1}
paradicsomleves={"paradicsomlé(dl)":7,"finomliszt(ek)":3,"napraforgó olaj(ek)":3,"kis fej vöröshagyma":1,"cukor(ek)":3,"tészta(dkg)":20}
gozolttojas={"tojás(db)":2,"vaj(tk)":2,"rozskenyér(szelet)":2,"csiper só":2}
corndog={"kukoricaliszt(dkg)":7,"búzaliszt(dkg)":6,"sütőpor(csomag)":1,"cukor(dkg)":2,"só(tk)":1,"őrölt bors(tk)":1,"tojás":1,"tej(dl)":1}

Rdesszert={"omlett":omlett, "bundaskenyer":bundaskenyer, "palacsinta":palacsinta}
Rfoetel={"omlett":omlett, "bundaskenyer":bundaskenyer,"madartej":madartej}
Reloetel={"omlett":omlett, "bundaskenyer":bundaskenyer,"madartej":madartej}

Edesszert={"palacsinta":palacsinta,"madartej":madartej}
Efoetel={"csilisbab":csilisbab,"paradicsomleves":paradicsomleves}
Eeloetel={"omlett":omlett,"corndog":corndog}

Vdesszert={"omlett":omlett, "palacsinta":palacsinta}
Vfoetel={"omlett":omlett,"gozolttojas":gozolttojas}
Veloetel={"omlett":omlett,}

reggeli={"eloetel":Reloetel,"foetel":Rfoetel,"desszert":Rdesszert}
ebed={"eloetel":Eeloetel,"foetel":Efoetel, "desszert":Edesszert}
vacsora={"eloetel":Veloetel,"foetel":Vfoetel, "desszert":Vdesszert}

napszak={"reggeli":reggeli,"ebed":ebed,"vacsora":vacsora}

print("Reggelit vagy Vacsorát vagy Ebédet szeretnél? ")


for key, value in napszak.items():
    print(key)
melyikStr=input("Válasz: ")
print(" ")
melyik=0

for key, value in napszak.items():
    if(key==melyikStr):
        melyik=value

for key, value in melyik.items():
    print(key)
melyikStr=input("Válasz: ")
print(" ")
for key, value in melyik.items():
    if(key==melyikStr):
        melyik=value
        break

for key, value in melyik.items():
    print(key)
melyikStr=input("Válasz: ")
print(" ")
for key, value in melyik.items():
    if(key==melyikStr):
        melyik=value
        break

for key,value in melyik.items():
    print(key,":", person*value)