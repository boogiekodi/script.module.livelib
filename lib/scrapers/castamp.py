import boogietools as bt
import re

encoding="utf-8"

def run(id,referer):
	type="rtmp"
	r_pageurl="http://www.castamp.com/embed.php?c=%s"%id
	page=bt.get_page(r_pageurl,encoding,referer=referer)
	r_flashver="WIN 20,0,0,306"
	r_swfurl="http://p.castamp.com/cplayer.swf"
	r_tcurl=re.findall("'streamer': '(.*?)'",page)[1]
	r_playpath=re.findall("'file': '(.*?)'",page)[1]
	values={}
	values["live"]="true"
	values["tcUrl"]=r_tcurl
	values["playpath"]=r_playpath
	values["pageUrl"]=r_pageurl
	values["swfUrl"]=r_swfurl
	values["flashver"]=r_flashver
	return type,values
