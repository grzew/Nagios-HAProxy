#!/usr/bin/env python

# Grzegorz Wieczorek
#
# Usage: ./check_haproxy.py -u http://your-site.pl

from optparse import OptionParser
import os, sys, urllib2

UNKNOWN = -1
OK = 0
WARNING = 1
CRITICAL = 2

parser = OptionParser()
parser.add_option('-u', '--url', dest='url')

options, args = parser.parse_args()

if not getattr(options, 'url'):
	print 'CRITICAL - %s not specified' % options.url
        #raise SystemExit, CRITICAL
	sys.exit(CRITICAL)

adres = options.url+"/haproxy?stats;csv"

#strona = urllib2.urlopen("http://balancer.diframe.pl/haproxy?stats;csv")
strona = urllib2.urlopen(adres)
log = strona.read()
strona.close()

lista = [[]]
slowo = ""
j = 0

for i in log:
	if i == "\n":
		j += 1
		lista.append([])
	elif i == ",":
		lista[j].append(slowo)
		slowo = ""
	else:
		slowo += i

print "Ilosc polaczen: %s :: Sekstylion: %s %s %s/%s  %s %s %s/%s" % (lista[1][4],lista[6][0],lista[6][17],lista[6][18],lista[6][19],lista[9][0],lista[9][17],lista[9][18],lista[9][19])
suma = 0
if suma < 12:
	sys.exit(OK)
elif suma > 12 and suma < 18:
	sys.exit(WARNING)
else:
	sys.exit(CRITICAL)

