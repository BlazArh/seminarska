from re import template
import bottle
import model

@bottle.get('/')
def index():
    return bottle.template('uvodna_stran.tpl')

@bottle.get("/vsota")
def pridobi_matrike1():
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

@bottle.get("/produkt")
def pridobi_matrike():
    return bottle.template('produkt.tpl')

@bottle.post("/produkt")
def zmnozi():
    matrika1 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika1'))
    matrika2 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika2'))
    rezultat = matrika1 * matrika2
    return bottle.template('izpis_produkta.tpl', matrika1 = matrika1, matrika2 = matrika2, rezultat = rezultat)

@bottle.get("/sled")
def pridobi_matrike():
    return bottle.template('sled.tpl')

@bottle.post("/sled")
def sledi():
    matrika1 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika1'))
    rezultat = model.sled_matrike(matrika1)
    return bottle.template('izpis_sled.tpl', matrika1 = matrika1, rezultat = rezultat)


bottle.run(reloader=True)

