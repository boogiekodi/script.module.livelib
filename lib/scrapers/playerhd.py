import boogietools as bt
import re
import urllib
import urlparse

encoding="utf-8"

def run(domain,id,ref,width="700",height="480"):
	type="rtmp"
	#provides: http://www.hdmyt.info, http://www.playerhd(n).pw
	r_pageurl="http://%s/channel.php?file=%s&width=%s&height=%s&autostart=true"%(domain,id,width,height)
	#loop through endless domains and player/channel pages until you find embed code
	while True:
		page=bt.get_page(r_pageurl,encoding,referer=ref)
		pageurl=re.findall('iframe src="(.*?)"',page)
		if len(pageurl)>0:
			r_pageurl=pageurl[0]
		else:
			r_pageurl=re.findall('<script type="text/javascript" src="(.*?channel\.php.*?)"',page)[0]
		if "embed.php?" in r_pageurl:
			break
	page=bt.get_page(r_pageurl,encoding,referer=ref)
	#script=urllib.unquote(re.findall("unescape\('(.*?)'\)",page)[0])
	sx1=re.findall('id="ssx1" value="(.*?)"',page)[0].decode("base64")
	sx4=re.findall('id="ssx4" value="(.*?)"',page)[0].decode("base64")
	r_swfurl="http://www.businessapp1.pw/jwplayer5/addplayer/jwplayer.flash.swf"
	r_tcurl=sx4
	r_playpath=sx1
	up=urlparse.urlparse(r_tcurl)
	values={}
	values["app"]=up.path[1:]+"?"+up.query
	values["tcUrl"]=r_tcurl
	values["playpath"]=r_playpath
	values["pageUrl"]=r_pageurl
	values["swfUrl"]=r_swfurl
	values["flashver"]="WIN 19,0,0,185"
	values["live"]="true"
	return type,values