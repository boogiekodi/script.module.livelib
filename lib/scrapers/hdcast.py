import boogietools as bt
import re
encoding="utf-8"

def run(ch,referer):
	# provides janjua.tv, p3gtv and friends
	type="rtmpe"
	r_pageurl="http://www.hdcast.info/embed.php?live=%s"%ch
	page=bt.get_page(r_pageurl,encoding,referer=referer)
	funcs=re.findall(" return\((.*?)\)\;",page)
	ops=funcs[0].split(" + ")
	r_tcurl="".join(eval(ops[0].split(".join")[0]))
	r_tcurl=r_tcurl+"".join(eval(re.findall(ops[1].split(".join")[0]+" \= (\[.*?\])",page)[0]))
	r_tcurl=r_tcurl+re.findall(re.findall("getElementById\(\"(.*?)\"\)",ops[2])[0]+"\>(.*?)<",page)[0]
	r_app=r_tcurl.split("/")[-1]+"/"
	r_tcurl=r_tcurl.replace("\\","")+"/"
	r_flashver="WIN 20,0,0,267"
	r_swfurl="http://www.hdcast.info/myplayer/jwplayer.flash.swf"
	r_playpath=ch
	r_token=re.findall("securetoken: (.*?)\n",page)[0]
	values={}
	values["app"]=r_app
	values["tcUrl"]=r_tcurl
	values["playpath"]="".join(eval(funcs[1].split(".join")[0]))
	values["pageUrl"]=r_pageurl
	values["swfUrl"]=r_swfurl
	values["live"]="false"
	values["flashver"]=r_flashver
	#values["token"]=r_token
	return type,values