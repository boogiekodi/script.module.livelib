import boogietools as bt
import re

encoding="utf-8"

def run(purl,referer):
	type="rtmp"
	r_pageurl=purl
	page=bt.get_page(r_pageurl,encoding,referer=referer)
	r_flashver="WIN 18,0,0,232"
	values={}
	values["live"]="true"
	try:
		r_swfurl=re.findall("swf      : '(.*?)'",page)[0]
		r_tcurl=re.findall("streamer : '(.*?)'",page)[0]
		r_playpath=re.findall("video    : '(.*?)'",page)[0]
		values["tcUrl"]=r_tcurl
		values["playpath"]=r_playpath
		values["pageUrl"]=r_pageurl
		values["swfUrl"]=r_swfurl
		values["flashver"]=r_flashver
	except IndexError:
		import urllib
		r_swfurl=re.findall('embedSWF\("(.*?)",',page)[0]
		farg=urllib.unquote(re.findall('"file":[\s]*?"(.*?)"',page)[0])
		farg=farg.split("/live/")
		values["tcUrl"]=farg[0]+"/live"
		values["playpath"]=farg[1]
		values["pageUrl"]=r_pageurl
		values["flashver"]=r_flashver
	return type,values