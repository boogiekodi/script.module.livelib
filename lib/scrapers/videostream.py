import boogietools as bt
import random

encoding="utf-8"

def run(id):
	type="rtmpe"
	values={}
	r_servers=["93.189.58.42","185.28.190.158","178.175.132.210","178.17.168.90","185.56.137.178","94.242.254.72"]
	values["tcUrl"]="rtmpe://%s/xlive"%random.choice(r_servers)
	values["playpath"]="raw:sl1_%s"%str(id)
	values["pageUrl"]="http://videostream.dn.ua/videopage/videoPage.php"
	values["swfUrl"]="http://videostream.dn.ua/videopage/images/VideoPlayer.swf"
	values["flashver"]="WIN 19,0,0,185"
	values["conn"]={0:"S:client",1:"S:3.1.0.9",2:"S:en"}
	values["live"]="true"
	return type,values