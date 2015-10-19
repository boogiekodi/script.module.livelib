import boogietools as bt
import re
import urlparse
import urllib

encoding="utf-8"

def run(id,referer):
	token=bt.deobfus(u'\u0114\u018f\xe1\u015f\u018c\xd2\u01a7\xff\u0141\xcc\u0198\u0105\xe4\u0186\xdb\xc9\xe7\xd2\u01a7\xde\xe7\u016b\u017a')
	purl="http://deltatv.pw/stream.php?id=%s"%id
	page=bt.get_page(purl,encoding,referer=referer)
	streamer=re.findall("streamer=(.*?)\&",page)
	splayer=re.findall('src="(.*?\.swf)"',page)
	values={}
	values["tcUrl"]=streamer[0]
	values["playpath"]=id
	values["pageUrl"]=purl
	values["swfUrl"]=splayer[0]
	values["flashver"]="WIN 19,0,0,185"
	values["live"]="true"
	values["token"]=token
	return "rtmp",values