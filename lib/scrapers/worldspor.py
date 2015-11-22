import boogietools as bt
import re
import urlparse
import urllib

encoding="utf-8"

def run(id,referer,width="480",height="270"):
	wurl="http://worldsport.me/%s"%id
	page=bt.get_page(wurl,encoding,referer=referer)
	soid=re.findall("<script type='text/javascript'>id='(.*?)'.*?http://sostart\.org/playerk\.js",page)
	if len(soid)>0:
		import sostart
		return sostart.run(soid[0],wurl)
	else:
		raise