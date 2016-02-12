import boogietools as bt
import re
encoding="utf-8"

def run(ch,referer):
	# provides janjua.tv, p3gtv and friends
	type="rtmp"
	r_pageurl="http://www.cast4u.tv/embed.php?live=%s"%ch
	page=bt.get_page(r_pageurl,encoding,referer=referer)
	r_flashver="WIN 19,0,0,232"
	r_swfurl="http://cast4u.tv/jwplayer/jwplayer.flash.swf"
	r_tcurl=re.findall('file1 = "(.*?)"',page)[0]
	r_playpath=ch
	values={}
	values["tcUrl"]=r_tcurl
	values["playpath"]=r_playpath
	values["pageUrl"]=r_pageurl
	values["swfUrl"]=r_swfurl
	values["live"]="true"
	values["flashver"]=r_flashver
	values["live"]="true"
	return type,values