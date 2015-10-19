import boogietools as bt
import re
import urlparse
import urllib

encoding="utf-8"

def run(channel,e,script,referer,width="480",height="270"):
	# provides janjua.tv, p3gtv and friends
	type="rtmp"
	page=bt.get_page(script,encoding)
	vidserver=re.findall("src=(.*?)/'\+embedded",page)[0]
	r_pageurl="%s/embedplayer/%s/%s/%s/%s"%(vidserver,channel,e,width,height)
	page=bt.get_page(r_pageurl,encoding,referer=referer)
	flashvars=re.findall("'FlashVars', '(.*?)'",page)
	flashvars=urlparse.parse_qs(flashvars[0])
	vidid=flashvars["id"][0]
	s=flashvars["s"][0]
	pk=flashvars["pk"][0]
	r_flashver="WIN 19,0,0,232"
	r_swfurl="%s%s"%(vidserver,re.findall('SWFObject\("(.*?)"',page)[0])
	r_server='%s:1935/loadbalancer?%s'%(vidserver,vidid)
	r_server=bt.get_page(r_server,encoding).split("=")[1]
	r_tcurl="rtmp://%s/live"%r_server
	r_playpath="%s?id=%s&pk=%s"%(s,vidid,pk)
	values={}
	values["tcUrl"]=r_tcurl
	values["playpath"]=r_playpath
	values["pageUrl"]=r_pageurl
	values["swfUrl"]=r_swfurl
	values["live"]="true"
	values["flashver"]=r_flashver
	values["live"]="true"
	values["conn"]={0:"S:OK"}
	return type,values

#RTMP Proxy Server v2.4 GIT-2015-01-15 (Compiled by KSV)
#(c) 2010 Andrej Stepanchuk, Howard Chu; license: GPL

#Streaming on rtmp://0.0.0.0:1935
#WARNING: Trying different position for client digest!
#Processing connect
#       app : live
#  flashVer : WIN 19,0,0,185
#    swfUrl : http://www.janjuaplayer.com/resources/scripts/eplayer.swf
#     tcUrl : rtmp://80.82.65.164/live
#   pageUrl : http://www.janjuaplayer.com/embedplayer/xxwebsporxx/1/700/480
#      live : yes
#  Playpath : xxwebsporxx?id=47863&pk=3cabac77723cbd6b4fb101871b5fb0202a57b726d6623162114bc27cf541ac62