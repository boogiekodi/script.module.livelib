import boogietools as bt
import re
import urlparse
import urllib

encoding="utf-8"

def run(id,referer,width="480",height="270"):
	wurl="http://sostart.org/streamk.php?id=%s"%id
	page=bt.get_page(wurl,encoding,referer=referer)
	r_tcurl=re.findall("file:'(.*?)'",page)[0]
	values={}
	values["app"]="live/"
	values["tcUrl"]=r_tcurl
	values["playpath"]=id
	values["pageUrl"]=wurl
	values["swfUrl"]="http://sostart.org/jw/jwplayer.flash.swf"
	values["flashver"]="WIN 19,0,0,185"
	values["live"]="true"
	return "rtmpe",values