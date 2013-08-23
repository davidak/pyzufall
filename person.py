#!/usr/bin/env python
# -*- coding: utf8 -*-

# https://www.destatis.de/DE/Startseite.html
# http://de.statista.com/
# https://www.zensus2011.de/DE/Home/home_node.html
# http://www.statistik2013.de/de/

# Geschlechterverteilung:
# https://www.destatis.de/DE/ZahlenFakten/GesellschaftStaat/Bevoelkerung/Bevoelkerungsstand/Tabellen/Zensus_Geschlecht_Staatsangehoerigkeit.html


import random as r
import datetime
import pyzufall as z

class Person(object):
	"""
	Generiert Daten einer zufälligen, fiktiven, aber plausiblen Person.
	"""
	anzahl = 0

	def __init__(self):
		self.geschlecht = z.geschlecht()
		if self.geschlecht:
			self.vorname = z.vorname_m()
		else:
			self.vorname = z.vorname_w()

		self.nachname = z.nachname()
		self.name = self.vorname + " " + self.nachname
		self.geburtsdatum = z.geburtsdatum()
		self.geburtsort = z.stadt()
		self.alter = Person.alter(self)
		self.wohnort = z.stadt()
		self.beruf = Person._gen_beruf(self)
		self.interessen = Person._gen_interessen()
		self.lieblingsfarbe = z.farbe()
		self.lieblingsessen = z.essen() + z.e50(" mit " + z.beilage())
		self.motto = z.sprichwort()

		Person.anzahl += 1
		print("Neue Person generiert: " + self.name)
	def __del__(self):
		Person.anzahl -= 1
		print("Person '" + self.name + "' wurde gelöscht.")

	def __str__(self):
		s = "*" * 80 + "\n"
		s += "Name: " + self.name + "\n"
		s += "Geschlecht: "
		if self.geschlecht:
			s += "männlich"
		else:
			s += "weiblich"
		s += "\nGeburtsdatum: " + self.geburtsdatum + " (" + str(self.alter) + ")\n"
		s += "Geburtsort: " + self.geburtsort + "\n"
		s += "Wohnort: " + self.wohnort + "\n"
		s += "Beruf: " + self.beruf + "\n"
		s += "Interessen: " + self.interessen + "\n"
		s += "Lieblingsfarbe: " + self.lieblingsfarbe + "\n"
		s += "Lieblingsessen: " + self.lieblingsessen + "\n"
		s += "Motto: " + self.motto + "\n"
		s += "*" * 80 + "\n"
		return s

	def alter(self):
		_heute = datetime.date.today()
		_geburtstag = datetime.datetime.strptime(self.geburtsdatum, "%d.%m.%Y").date()
		_alter = int((_heute - _geburtstag).days / 365.2425)
		return _alter

	def _gen_beruf(self):
		"""
		Generiert den Beruf einer Person anhand des Alters und Statistiken.

		Es wird von 10% Arbeitslosigkeit ausgegangen, die ofizielle Statistik ist allerdings 7,10% im Jahr 2013.
		Quelle: http://de.statista.com/statistik/daten/studie/1224/umfrage/arbeitslosenquote-in-deutschland-seit-1995/

		Es wird angenommen, dass 30% der zwischen 19 und 29 jährigen studieren:
		Studienanfänger 43,3%
		Studienabsolventen: 26,2%
		Quelle: http://de.wikipedia.org/wiki/Abiturientenquote_und_Studienanf%C3%A4ngerquote
		"""
		if self.geschlecht: # männlich
			if self.alter < 6:
				return "kein"
			elif self.alter <= 18:
				return "Schüler"
			elif self.alter > 18 and self.alter < 30 and r.randint(0,100) <= 30: # 30% studieren
				return "Student"
			elif self.alter > 68:
				return "Rentner"
			elif r.randint(0,9): # 1 von 10 arbeitslos
				return z.beruf_m()
			else:
				return "arbeitslos"
		else: # weiblich
			if self.alter < 6:
				return "kein"
			elif self.alter <= 18:
				return "Schülerin"
			elif self.alter > 18 and self.alter < 30 and r.randint(0,100) <= 30: # 30% studieren
				return "Studentin"
			elif self.alter > 68:
				return "Rentnerin"
			elif r.randint(0,9): # 1 von 10 arbeitslos
				return z.beruf_w()
			else:
				return "arbeitslos"

	def _gen_interessen():
		_anzahl = r.randint(1,3)
		if r.randint(0,1): # 50% haben mehr als 3 Interessen, maximal 8
			_anzahl + r.randint(1, 5)
		s = z.interesse()

		return s

print("Anzahl: " + str(Person.anzahl))
p1 = Person()
print(p1)
print("Anzahl: " + str(Person.anzahl))
p2 = Person()
print(p2)
print("Anzahl: " + str(Person.anzahl))

print(p1.vorname + " und " + p2.vorname + " sitzen auf einer Bank im Park.\n")

del p1
print("Anzahl: " + str(Person.anzahl))
del p2
print("Anzahl: " + str(Person.anzahl))

# Bugs
# Etagenaufsichtin

# Funktion um Liste mit ungleichen Teilen zu erzeugen?