import boogietools as bt
import re
import urlparse
import urllib

encoding="utf-8"
def dec(st):
	newstr=""
	for s in st:
		newstr=newstr+unichr(ord(s)^123)
	return newstr

def run(url,ref):
	page=bt.get_page(url,encoding,referer=ref)
	type="rtmp"
	r_tcurl=re.findall("('rtmp://.*?');",page)
	r_tcurl=eval(r_tcurl[0])
	r_playpath=r_tcurl.split("/")[-1]
	r_app=r_tcurl.split("/")[-2]+"/"
	r_tcurl="/".join(r_tcurl.split("/")[:-1])+"/"
	values={}
	values["app"]=r_app
	values["tcUrl"]=r_tcurl
	values["playpath"]=r_playpath
	values["pageUrl"]=url
	values["swfUrl"]="http://www.micast.tv/jwplayer/jwplayer.flash.swf"
	values["flashver"]="WIN 19,0,0,185"
	values["live"]="true"
	return type,values