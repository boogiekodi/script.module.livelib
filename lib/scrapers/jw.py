import boogietools as bt
import re
import urllib
import urlparse

encoding="utf-8"

def run(id,ref):
	type="rtmp"
	#provides: http://www.hdmyt.info, http://www.playerhd(n).pw
	r_pageurl="http://content.jwplatform.com/players/%s.html"%id
	jsurl="http://content.jwplatform.com/players/%s.js"%id
	#loop through endless domains and player/channel pages until you find embed code
	page=bt.get_page(r_pageurl,encoding,referer=ref)
	r_playpath=re.findall('<h1 id="title">(.*?)</h1>',page)[0]
	js=bt.get_page(jsurl,encoding,referer=ref)
	r_swfurl=re.findall('flashplayer\: "(.*?)"',js)[0]
	if r_swfurl.startswith("//"):
		r_swfurl="http:"+r_swfurl
	values={}
	values["app"]="ARYNEWS//"
	values["tcUrl"]="rtmp://5.254.116.206/ARYNEWS//"
	values["playpath"]=r_playpath
	values["pageUrl"]=r_pageurl
	values["swfUrl"]=r_swfurl
	values["flashver"]="WIN 19,0,0,185"
	values["live"]="true"
	return type,values