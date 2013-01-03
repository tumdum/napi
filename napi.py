#!/usr/bin/python
# reversed napi 0.16.3.1
#
# by gim,krzynio,dosiu,hash 2oo8.
#
#
#
# last modified: 6-I-2oo8
#
# 4pc0h f0rc3
#
# do dzialania potrzebny jest p7zip-full (tak sie nazywa paczka w debianie)
#
# POZDRAWIAMY NASZYCH FANOW!

import md5, sys, urllib, os

import urllib
import urllib2

import xml.etree.ElementTree as ET

import base64

def f(z):
	idx = [ 0xe, 0x3,  0x6, 0x8, 0x2 ]
	mul = [   2,   2,    5,   4,   3 ]
	add = [   0, 0xd, 0x10, 0xb, 0x5 ]

	b = []
	for i in xrange(len(idx)):
		a = add[i]
		m = mul[i]
		i = idx[i]

		t = a + int(z[i], 16)
		v = int(z[t:t+2], 16)
		b.append( ("%x" % (v*m))[-1] )

	return ''.join(b)


if(len(sys.argv)==1):
	print "wy*dalaj na stadion po film"
	sys.exit(2)

d = md5.new()
d.update(open(sys.argv[1]).read(10485760))

def download_subtitles(digest):
	request_data = { 
		"downloaded_subtitles_id" : digest, 
		"mode" : "31", 
		"client" : "NapiProjekt", 
		"downloaded_subtitles_lang" : "PL"
	}
	try:
		request_stream = urllib.urlencode(request_data)
		request = urllib2.Request("http://napiprojekt.pl/api/api-napiprojekt3.php", request_stream)
		response = urllib2.urlopen(request)
		xml = ET.XML(response.read())
		content = xml.find("subtitles").find("content").text
	except:
		print "nie ma napisa do filmu"
		return
	
	open("napisy.7z","w").write(base64.b64decode(content))
	nazwa=sys.argv[1][:-3]+'txt'

	if (os.system("7z x -y -so -piBlm8NTigvru0Jr0 napisy.7z 2>/dev/null >\""+nazwa+"\"")):
		print "nie ma napisa do filmu"
		os.remove(nazwa)        
	else:
		print "napisy pobrano, milordzie!"

	os.remove("napisy.7z")

download_subtitles(d.hexdigest())
