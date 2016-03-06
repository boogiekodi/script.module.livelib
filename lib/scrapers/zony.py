import boogietools as bt
import re
import urlparse

encoding="utf-8"

def run(id,referer):
	type="rtmp"
	r_pageurl="http://www.zony.tv/embedplayer/%s/1/680/470"%id
	page=bt.get_page(r_pageurl,encoding,referer=referer)
	r_flashver="WIN 20,0,0,306"
	flashvars=re.findall("'FlashVars', '(.*?)'",page)
	flashvars=urlparse.parse_qs(flashvars[0])
	vidid=flashvars["id"][0]
	s=flashvars["s"][0]
	pk=flashvars["pk"][0]
	r_swfurl="http://www.zony.tv%s"%re.findall('SWFObject\("(.*?)"',page)[0]
	values={}
	values["live"]="true"
	r_server='http://cdn.pubzony.com:1935/loadbalancer?%s'%vidid
	r_server=bt.get_page(r_server,encoding).split("=")[1]
	r_tcurl="rtmp://%s/stream"%r_server
	r_playpath="%s?id=%s&pk=%s"%(s,vidid,pk)
	values["tcUrl"]=r_tcurl
	values["playpath"]=r_playpath
	values["pageUrl"]=r_pageurl
	values["swfUrl"]=r_swfurl
	values["flashver"]=r_flashver
	values["conn"]={0:"S:OK"}
	return type,values