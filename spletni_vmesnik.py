import bottle
import model

@bottle.get("/vsota")
def pridobi_matrike():
    return bottle.template('vsota.tpl')

@bottle.post("/vsota")
def sestej():
    matrika1 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika1'))
    matrika2 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika2'))
    rezultat = matrika1 + matrika2
    return bottle.template('izpis_vsote.tpl', matrika1 = matrika1, matrika2 = matrika2, rezultat = rezultat)

@bottle.get("/razlika")
def pridobi_matrike():
    return bottle.template('razlika.tpl')

@bottle.post("/razlika")
def odstej():
    matrika1 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika1'))
    matrika2 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika2'))
    rezultat = matrika1 - matrika2
    return bottle.template('izpis_razlike.tpl', matrika1 = matrika1, matrika2 = matrika2, rezultat = rezultat)


bottle.run(reloader=True)

