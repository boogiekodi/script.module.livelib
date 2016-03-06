import boogietools as bt
import sys

import xbmcgui

class livelib():
	def __init__(self):
		self.timeout=None

	def scrape(self,scraper,*args,**kwargs):
		try:
			module=__import__("scrapers",fromlist=[scraper])
			scraper_function=getattr(module,scraper)
		except Exception,e:
			type="ERROR: LIVELIB | No scraper for %s"%scraper
			result=e
			return type,result
		try:
			type,result=scraper_function.run(*args,**kwargs)
		except Exception,e:
			type="ERROR: LIVELIB | Scraper \'%s\' can't scrape the service"%scraper
			result=e
			return type,result
		header="*************** LIVELIB %s ARGUMENTS ***************"%type.upper()
		print header
		for k,v in result.iteritems():
			print "%s:%s"%(k,str(v))
		print "*"*len(header)
		return type,result


	def scrape_url(self,scraper,*args,**kwargs):
		type,params=self.scrape(scraper,*args,**kwargs)
		if "ERROR:" in type:
			return type,params
		if type in ["rtmp","rtmpe"]:
			if "tcUrl" in params.keys():
				url = self._escape_rtmp(params["tcUrl"])
				params.pop("tcUrl")
				if not self.timeout is None:
					params["timeout"]=self.timeout
				for k,v in params.iteritems():
					if k=="conn":
						for kc in sorted(v.keys()):
							url+=" conn=%s"%self._escape_rtmp(v[kc])
						continue
					url+=" %s=%s"%(k,self._escape_rtmp(v))
				return type,url
			else:
				return "ERROR: LIVELIB | Can't detect stream type %s"%type,""
		if type in ["m3u","m3u8"]:
			return type,params

	
	def scrape_li(self,scraper,*args,**kwargs):
		type,params=self.scrape(scraper,*args,**kwargs)
		if "ERROR:" in type:
			return type,params
		if type in ["rtmp","rtmpe"]:
			item = xbmcgui.ListItem(path=str(params["tcUrl"]))
			params.pop("tcUrl")
			for k,v in params.iteritems():
				item.setProperty(str(k), str(v))
			return type,item
		else:
			return "ERROR: LIVELIB | Can't convert stream type %s to ListItem"%type,None
	
	def _escape_rtmp(self,s):
		s=str(s)
		escaped=[" ","?","&"]
		for c in escaped:
			if c in s:
				s=s.replace(c,"\\%s"%hex(ord(c))[2:])
		return s