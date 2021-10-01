from re import template
import bottle
import model
from bottle import debug

debug(True)

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
    try:
        rezultat = matrika1 + matrika2
        return bottle.template('izpis_vsote.tpl', matrika1 = matrika1, matrika2 = matrika2, rezultat = rezultat)
    except:
        return bottle.template("izpis_napake.tpl")

@bottle.get("/razlika")
def pridobi_matrike2():
    return bottle.template('razlika.tpl')

@bottle.post("/razlika")
def odstej():
    matrika1 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika1'))
    matrika2 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika2'))
    try:
        rezultat = matrika1 - matrika2
        return bottle.template('izpis_razlike.tpl', matrika1 = matrika1, matrika2 = matrika2, rezultat = rezultat)
    except:
        return bottle.template("izpis_napake.tpl")

@bottle.get("/produkt")
def pridobi_matrike3():
    return bottle.template('produkt.tpl')

@bottle.post("/produkt")
def zmnozi():
    matrika1 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika1'))
    matrika2 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika2'))
    try:
        rezultat = matrika1 * matrika2
        return bottle.template('izpis_produkta.tpl', matrika1 = matrika1, matrika2 = matrika2, rezultat = rezultat)
    except:
        return bottle.template("izpis_napake.tpl")

@bottle.get("/sled")
def pridobi_matrike4():
    return bottle.template('sled.tpl')

@bottle.post("/sled")
def sledi():
    matrika1 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika1'))
    try:
        rezultat = matrika1.sled_matrike()
        return bottle.template('izpis_sled.tpl', matrika1 = matrika1, rezultat = rezultat)
    except:
        return bottle.template("izpis_napake.tpl")

@bottle.get("/transponiranje")
def pridobi_matrike5():
    return bottle.template('transponiranje.tpl')

@bottle.post("/transponiranje")
def trans():
    matrika1 = model.preberi_matriko_iz_niza(bottle.request.forms.getunicode('matrika1'))
    rezultat = matrika1.transponiraj()
    return bottle.template('izpis_trans.tpl', matrika1 = matrika1, rezultat = rezultat)

@bottle.get("/navodila")
def nav():
    return bottle.template('navodila.tpl')



bottle.run(reloader=True)

