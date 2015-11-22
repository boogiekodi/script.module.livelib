import boogietools as bt
import re
import urlparse
import urllib

encoding="utf-8"

def run(id,referer,width="480",height="270"):
	wurl="http://weplayer.pw/stream.php?id=%s"%id
	page=bt.get_page(wurl,encoding,referer=referer)
	id=re.findall("<script type='text/javascript'>id='(.*?)'.*?src='http://deltatv.pw/player.js'",page)
	import deltatv
	return deltatv.run(id[0],wurl)