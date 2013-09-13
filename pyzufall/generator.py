#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import random
import datetime

from .helfer import lese, e16, e25, e50, e75


r = random.SystemRandom() # Benutze /dev/urandom oder Windows CryptGenRandom für bessere Entropy

# Namen einlesen
vornamen_m = lese('vornamen_m')
vornamen_w = lese('vornamen_w')
nachnamen = lese('nachnamen')

# Objekte einlesen
pflanzen = lese('pflanzen')
baeume = lese('baeume')
tiere = lese('tiere')
gegenstaende = lese('gegenstaende')
koerperteile = lese('koerperteile')
nahrung = lese('nahrung')
geschmack = lese('geschmack')
berufe = lese('berufe')
musik = lese('musikgenre')
stadte = lese('stadt_bundesland')
interessen = lese('interessen.txt')

# Wortarten einlesen

# Verben
nullwertige_verben = lese('nullwertige_verben')
intransitive_verben = lese('intransitive_verben')
intransitive_verben_2 = lese('intransitive_verben_2')
transitive_verben = lese('transitive_verben')
transitive_verben_2 = lese('transitive_verben_2')
ditransitive_verben = lese('ditransitive_verben')

# Adjektive
adjektive = lese('adjektiv')

# Sazteile oder Sätze
ortsangabe = lese('ort')
ns = lese('nebensatz')
sprichwoerter = lese('sprichwoerter')


def geschlecht():
	"""
	Gibt ein zufälliges Geschlecht zurück.

	1 = männlich
	0 = weiblich

	2011 gibt es laut Statistik 51,18% weibliche Personen in Deutschland:
	https://www.destatis.de/DE/ZahlenFakten/GesellschaftStaat/Bevoelkerung/Bevoelkerungsstand/Tabellen/Zensus_Geschlecht_Staatsangehoerigkeit.html
	"""
	if r.randint(0, 100) <= 51:
		return 0
	else:
		return 1


def vorname_m():
	"""
	Gibt einen männlichen Vornamen zurück.
	"""
	return r.choice(vornamen_m)


def vorname_w():
	"""
	Gibt einen weiblichen Vornamen zurück.
	"""
	return r.choice(vornamen_w)


def vorname():
	"""
	Gibt einen zufälligen Vornamen zurück.
	"""
	return r.choice([vorname_m, vorname_w])()


def nachname():
	"""
	Gibt einen Nachnamen zurück.
	"""
	return r.choice(nachnamen)


def verbn():
	"""
	Gibt ein nullwertiges Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(nullwertige_verben)


def verbi():
	"""
	Gibt ein intransitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(intransitive_verben)


def verbi2():
	"""
	Gibt ein intransitives, getrenntes Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(intransitive_verben_2)


def verbt():
	"""
	Gibt ein transitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(transitive_verben)


def verbt2():
	"""
	Gibt ein intransitives, getrenntes Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(transitive_verben_2)


def verbd():
	"""
	Gibt ein ditransitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(ditransitive_verben)


def adjektiv():
	"""
	Gibt ein Adjektiv zurück.
	"""
	return r.choice(adjektive)


def gegenstand():
	"""
	Gibt einen Gegenstand zurück.
	"""
	return r.choice(gegenstaende)


def koerperteil():
	"""
	Gibt ein Körperteil zurück.
	"""
	return r.choice(koerperteile)


def interesse():
	"""
	Gibt ein zufälliges Interesse bzw Hobby zurück.
	"""
	return r.choice(interessen)


def tier():
	"""
	Gibt ein Tier zurück.
	"""
	return r.choice(tiere)


def baum():
	"""
	Gibt einen Baum zurück.
	"""
	return r.choice(baeume)


def pflanze():
	"""
	Gibt eine Pflanze zurück.
	"""
	return r.choice(pflanzen)


beziehung_m = ['Vater', 'Bruder', 'Mann', 'Sohn', 'Onkel', 'Opa', 'Cousin', 'Enkel', 'Chef', 'Freund', 'Partner', 'Kollege', 'Mitarbeiter', 'Mitbewohner', 'Vermieter', 'Lehrer']
beziehung_w = ['Mutter', 'Schwester', 'Frau', 'Tochter', 'Tante', 'Oma', 'Cousine', 'Enkelin', 'Cheffin', 'Freundin', 'Partnerin', 'Kollegin', 'Mitarbeiterin', 'Mitbewohnerin', 'Vermieterin', 'Lehrerin']
possessivpronomen_m = ['mein', 'dein', 'sein', 'ihr']
personen = ['er', 'sie', 'es', 'jemand', 'niemand']
spezial_m = ['ein Held', 'ein Penner', 'ein Verkäufer', 'ein Zuhälter', 'ein Lehrer', 'ein Polizist', 'ein Beamter', 'ein Arzt', 'Hitler', 'ein Bernd', 'ein Schwuler', 'ein Behinderter', 'der Affenmensch', 'der Satanist', 'der Alkoholiker', 'ein normaler Mensch', 'ein Pirat', 'ein Hartz-IV-Empfänger', 'ein Müllmann']
spezial_w = ['eine Heldin', 'eine Pennerin', 'eine Verkäuferin', 'eine Zuhälterin', 'eine Prostituierte', 'eine Nutte', 'eine Hure', 'eine Schlampe', 'eine Lehrerin', 'eine Polizistin', 'eine Beamtin', 'eine Ärztin', 'eine Behinderte', 'eine Sekretärin', 'die Transe', 'das Mannsweib', 'das Penismädchen', 'die Lesbe', 'die Kampflesbe', 'die Satanistin', 'die Alkoholikerin', 'die Piratin', 'die Hartz-IV-Empfängerin']
def person_m():
	"""
	Gibt eine männliche Person zurück.
	"""
	z = r.randint(1,10)
	if z == 1:
		s = e25(adjektiv() + 'er ')
		s = re.sub('eer $', 'er ', s) # feigeer
		s = r.choice([vorname_m(), vorname_w()]) + 's ' + s + r.choice(beziehung_m)
	elif z == 2:
		s = e25(adjektiv() + 'er ')
		s = re.sub('eer $', 'er ', s) # feigeer
		s = r.choice(possessivpronomen_m) + ' ' + s + r.choice(beziehung_m)
	elif z == 3:
		s =  e50(adjektiv() + 'e ')
		s = re.sub('ee $', 'e ', s) # der feigee
		s = 'der ' + s + r.choice(beziehung_m)
	elif z == 4:
		s = adjektiv() + 'e '
		s = re.sub('ee $', 'e ', s) # der feigee
		s = 'der ' + s + r.choice(vornamen_m)
	elif z == 5:
		s = adjektiv() + 'e'
		s = re.sub('ee$', 'e', s) # der feigee
		s = 'der ' + s.capitalize()
	elif z == 6:
		s = r.choice(['der ', 'ein ']) + beruf_m()
	elif z == 7:
		s = r.choice(spezial_m)
	elif z == 8:
		s = 'er'
	else:
		s = vorname_m()
	return s


def person_w():
	"""
	Gibt eine weibliche Person zurück.
	"""
	z = r.randint(1,10)
	if z == 1:
		s = e25(adjektiv() + 'e ')
		s = re.sub('ee $', 'e ', s) # feigee
		s = r.choice([vorname_m(), vorname_w()]) + 's ' + s + r.choice(beziehung_w)
	elif z == 2:
		s = e25(adjektiv() + 'e ')
		s = re.sub('ee $', 'e ', s) # die feigee
		s = r.choice(possessivpronomen_m) + 'e ' + s + r.choice(beziehung_w)
	elif z == 3:
		s =  e50(adjektiv() + 'e ')
		s = re.sub('ee $', 'e ', s) # die feigee
		s = 'die ' + s + r.choice(beziehung_w)
	elif z == 4:
		s = adjektiv() + 'e '
		s = re.sub('ee $', 'e ', s) # die feigee
		s = 'die ' + s + vorname_w()
	elif z == 5:
		s = adjektiv() + 'e'
		s = re.sub('ee$', 'e', s) # die feigee
		s = 'die ' + s.capitalize()
	elif z == 6:
		s = r.choice(['die ', 'eine ']) + beruf_w()
	elif z == 7:
		s = r.choice(spezial_w)
	elif z == 8:
		s = 'sie'
	else:
		s = vorname_w()
	return s


def person():
	"""
	Gibt eine zufällige Person zurück.
	"""
	return r.choice([person_m, person_w])()


vokal = ['a', 'e', 'i', 'o', 'u', 'ei', 'au']
konsonant = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'sch']
konsonant2 = ['h', 'k', 'l', 'm', 'n', 's', 't']
def wort():
	"""
	Gibt ein Fantasiewort zurück.
	"""
	laenge = r.randint(3,12)
	anfaengt = r.randint(1,3)
	s = ""
	
	if anfaengt == 2: # Anfang wird ein Vokal
		s = r.choice(vokal)
		while len(s) < laenge:
			s += r.choice(konsonant)
			if len(s) < laenge and r.randint(0,1):
				s += r.choice(konsonant2)
			if len(s) >= laenge:
				break
			s += r.choice(vokal)

	else: # Anfang wird ein Konsonant
		s = r.choice(konsonant)
		while len(s) < laenge:
			s += r.choice(vokal)
			if len(s) >= laenge:
				break
			s += r.choice(konsonant)
			if len(s) < laenge and r.randint(0,1):
				s += r.choice(konsonant2)
	s = s.capitalize()
	return s


def zahl():
	"""
	Gibt eine Zahl zwischen 0 und 100 zurück.
	"""
	s = r.randint(0,100)
	return str(s)


farben = ['Rot', 'Gelb', 'Blau', 'Violett', 'Türkis', 'Orange', 'Grün', 'Magenta', 'Braun', 'Grau', 'Weiß', 'Schwarz']
def farbe():
	"""
	Gibt eine Farbe zurück.
	"""
	return r.choice(farben)


colors = ['red', 'yellow', 'blue', 'violet', 'orange', 'green', 'magenta', 'brown', 'gray', 'white', 'black']
def color():
	"""
	Gibt eine Farbe auf englisch zurück.
	"""
	return r.choice(colors)


def geburtsdatum():
	"""
	Gibt ein gültiges Datum zwischen dem 01.01.1910 und 31.12.2012 zurück.
	"""
	while(True):
		try:
			_s = str(r.randint(1,31)).zfill(2) + '.' + str(r.randint(1,12)).zfill(2) + '.' + str(r.randint(1910,2012))
			_dateobj = datetime.datetime.strptime(_s, "%d.%m.%Y").date() # kann der String in ein gültiges Datum umgewandelt werden?
			return _s
		except:
			print(_s + " ist kein gültiges Datum!")


def datum():
	"""
	Gibt ein gültiges Datum zwischen dem 01.01.1950 und 31.12.2012 zurück.
	"""
	while(True):
		try:
			_s = str(r.randint(1,31)).zfill(2) + '.' + str(r.randint(1,12)).zfill(2) + '.' + str(r.randint(1950,2012))
			_dateobj = datetime.datetime.strptime(_s, "%d.%m.%Y").date() # kann der String in ein gültiges Datum umgewandelt werden?
			return _s
		except:
			print(_s + " ist kein gültiges Datum!")


def sprichwort():
	"""
	Gibt ein Sprichwort zurück.
	"""
	return r.choice(sprichwoerter)


def beruf_m():
	"""
	Gibt eine männliche Berufsbezeichnung zurück.
	"""
	return r.choice(berufe)


def beruf_w():
	"""
	Gibt eine weibliche Berufsbezeichnung zurück.
	"""
	s = beruf_m() + 'in'
	s = re.sub('mannin$', 'frau', s) # Restaurantfachmannin => Restaurantfachfrau
	s = re.sub('kraftin$', 'kraft', s) # Edv-Fachkraftin => Edv-Fachkraft
	s = re.sub('angestellterin$', 'angestellte', s)
	s = re.sub('Fotomodellin$', 'Fotomodell', s)
	s = re.sub('Technischer Zeichnerin$', 'Technische Zeichnerin', s)
	s = re.sub('Arztin$', 'Ärztin', s)
	s = re.sub('arztin$', 'ärztin', s)
	s = re.sub('beamterin$', 'beamtin', s) # Polizeibeamterin => Polizeibeamte
	s = re.sub('ein$', 'in', s) # Mikrobiologein => Mikrobiologin
	return s


def objekt():
	"""
	Gibt ein Objekt zurück.
	"""
	return r.choice([gegenstand(), tier(), pflanze(), baum()])


def objekt_m(s):
	"""
	Bringt ein Objekt in Berzug zu einer männlichen Person.

	Beispiel:
	'der Bär' wird zu 'den Bären' oder 'seinen Bären'
	"""
	if 'der ' in s:
		s = re.sub('e$', 'en', s) # Löwen
	s = re.sub('Bär$', 'Bären', s)
	s = re.sub('der ', 'den ', s)
	
	if r.randint(0,2):
		s = re.sub('den ', r.choice(['einen ', 'seinen ', 'deinen ']), s)
		s = re.sub('die ', r.choice(['eine ', 'seine ', 'deine ']), s)
		s = re.sub('das ', r.choice(['ein ', 'sein ', 'dein ']), s)
	
	return s


def objekt_w(s):
	"""
	Bringt ein Objekt in Berzug zu einer weiblichen Person.

	Beispiel:
	'der Bär' wird zu 'den Bären' oder 'ihren Bären'
	"""
	if 'der ' in s:
		s = re.sub('e$', 'en', s) # Löwen
	s = re.sub('Bär$', 'Bären', s)
	s = re.sub('der ', 'den ', s)
	
	if r.randint(0,2):
		s = re.sub('den ', r.choice(['einen ', 'ihren ', 'deinen ']), s)
		s = re.sub('die ', r.choice(['eine ', 'ihre ', 'deine ']), s)
		s = re.sub('das ', r.choice(['ein ', 'ihr ', 'dein ']), s)
	
	return s


def person_objekt_m():
	"""
	Gibt eine Person als Objekt in Bezug auf eine männliche Person zurück.

	Beispiel: seine Mitarbeiterin
	"""
	y = r.randint(1,4)
	if y == 1:
		s = vorname_m()
	if y == 2:
		s = vorname_w()
	if y == 3:
		s =  e25(adjektiv() + 'en ')
		s = re.sub('een ', 'en ', s) # feigeen
		s = r.choice(['seinen ', 'deinen ']) + s + r.choice(beziehung_m)
		s = re.sub('Kollege', 'Kollegen', s)
	if y == 4:
		s =  e25(adjektiv() + 'e ')
		s = re.sub('ee ', 'e ', s) # feigee
		s = r.choice(['seine ', 'deine ']) + s + r.choice(beziehung_w)
		
	return s


def person_objekt_w():
	"""
	Gibt eine Person als Objekt in Bezug auf eine weibliche Person zurück.

	Beispiel: ihre Mutter
	"""
	y = r.randint(1,4)
	if y == 1:
		s = vorname_m()
	if y == 2:
		s = vorname_w()
	if y == 3:
		s =  e25(adjektiv() + 'en ')
		s = re.sub('een ', 'en ', s) # feigeen
		s = r.choice(['ihren ', 'deinen ']) + s + r.choice(beziehung_m)
		s = re.sub('Kollege', 'Kollegen', s)
	if y == 4:
		s =  e25(adjektiv() + 'e ')
		s = re.sub('ee ', 'e ', s) # feigee
		s = r.choice(['ihre ', 'deine ']) + s + r.choice(beziehung_w)

	return s


def ort():
	"""
	Gibt eine Ortsangabe zurück.

	Beispiel: 'im Flur'
	"""
	tausende = ['500', '1000', '2000', '5000', '10000', '100000']
	if r.randint(0,3):
		zuschauer = r.choice(tausende)
	else:
		zuschauer = str(r.randint(1,10000))

	s = r.choice(ortsangabe)
	s = re.sub('auf Gleis XX$', 'auf Gleis ' + str(r.randint(1,14)), s)
	s = re.sub('XXZusch', zuschauer, s)
	s = re.sub('XXName', r.choice([vorname_m(), vorname_w()]) + 's', s)
	return s


voressen = ['Brat', 'Rühr', 'Reibe', 'Brech', 'Back', 'Ofen', 'Hack', 'Mager', 'Frisch', 'Bio', 'Gammel', 'Soja', 'Tofu', 'Milch']
def essen():
	"""
	Gibt ein Gericht zurück.
	"""
	if r.randint(0,2): # zusammengesetzt aus zwei Wörtern
		if r.randint(0,2):
			s = r.choice(geschmack) + r.choice(nahrung).lower()
		else:
			s = r.choice(voressen) + r.choice(nahrung).lower()
	else: # aus einem Wort bestehend
		if r.randint(0,2):
			s = r.choice(geschmack)
		else:
			s = r.choice(nahrung)
	return s


beilag = ['Soße', 'Sauce', 'Brühe', 'Brei', 'Püree', 'Kartoffeln', 'Salat', 'Marmelade']
beilag2 = ['Kroketten', 'Pommes', 'Rösti', 'Röstzwiebeln', 'Mayo', 'Mayonnaise', 'Ketchup', 'Bratkartoffeln', 'Zwiebelringen', 'Kartoffelpuffer', 'Soße', 'Nudeln', 'Gemüse', 'Knödeln', 'Salat', 'Marmelade']
def beilage():
	"""
	Gibt eine Beilage zum Essen zurück.
	"""
	if r.randint(0,2):
		s = r.choice(beilag2)
	else:
		s = r.choice(geschmack) + r.choice(beilag).lower()
	return s


getraenk = ['Wasser', 'Saft', 'Tee', 'Kaffee', 'Eistee', 'Milch', 'Punsch', 'Bowle', 'Bier', 'Likör',  'Wein', 'Rum', 'Sekt', 'Schnaps', 'Cocktail']
def trinken():
	"""
	Gibt ein Getränk zurück.
	"""
	if r.randint(0,2):
		s = r.choice(geschmack) + r.choice(getraenk).lower()
	else:
		s = r.choice(getraenk)
	return s


def stadt():
	"""
	Gibt eine Stadt zurück.
	"""
	s = r.choice(stadte).split(' (', 1) # Stadt und Bundesland trennen
	s = s[0] # Nur Stadt, nicht Bundesland
	return s


def stadt_bl():
	"""
	Gibt eine Stadt mit Bundesland zurück.
	"""
	return r.choice(stadte)


gruppe = ['Menschen', 'Personen', 'Kinder', 'Tiere', 'Gedärme', 'Kadaver', 'Nudeln', 'Unterhosen', 'Würstchen', 'Bäume', 'Stühle', 'Schweine', 'Neger', 'Alkoholiker', 'Leichen']
def band():
	"""
	Gibt einen fiktiven Bandnamen zurück.
	"""
	z = r.randint(0,5)
	if z == 0:
		s = 'Die ' + adjektiv().capitalize() + 'en ' + r.choice(gruppe)
	if z == 1:
		s = r.choice(geschmack) + ' ' + ort()
	if z == 2:
		s = adjektiv().capitalize() + ' ' + ort()
	if z == 3:
		s = adjektiv().capitalize() + 'e ' + essen()
	if z == 4:
		s = adjektiv().capitalize()
	if z == 5:
		s = wort()
	return s


def bandart():
	"""
	Gibt eine Bandart zurück.

	Beispiel: 'Gothic Metal Band'
	"""
	if r.randint(0,2):
		m = r.choice(musik)
		if ' ' in m:
			s = m + ' Band'
		elif '-' in m:
			s = m + '-Band'
		else:
			s = m + 'band'
	else:
		s = r.choice(['Band', 'Musikergruppe'])
	return s


def firma():
	"""
	Gibt einen fiktiven Firmenname zurück.

	.. todo::

		Funktion programmieren
	"""
	pass