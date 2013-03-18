#!/usr/bin/env python
#coding: utf-8
import urlparse,os,sys
import socket,urllib
import re
sys.path.append('/home/return/workspace/python/return')
import libs.html

class sites():
	def __init__(self,host,callback):
		self.sitesUrl = []
		self.host = host
		self.hostIp = self.getHostIp(host)
		self.callback = callback
	def getHostIp(self,host=''):
		 
		return socket.gethostbyname(host)
 	# use the bing api
	def getSameIpSites(self,host = ''):
		if len(host):
			host = host
		else:
			host = self.host
		hostIp = self.getHostIp(host)
		findUrl = 'http://cn.bing.com/search?q=ip:%s'%hostIp
		strHtml = urllib.urlopen(findUrl).read()
		patten = re.compile('class="sb_rc_btm">(.*?)条结果')
		match = re.search(patten,strHtml)
		if match and len(match.groups()):
			num = match.groups()
			num = num[0]
			if num.find(','):
				num = num.replace(',','')
			num = int(num)
			self.parse_html(strHtml)
			if num > 11:
				for i in range(num/10):
					page = str((i*10+10))
					findUrl = 'http://cn.bing.com/search?q=ip:%s&first=%s'%(hostIp,page)
					strHtml = urllib.urlopen(findUrl).read()
					self.parse_html(strHtml)
		else:
			self.sitesUrl.append(self.host)
	#other api
	def webApi(self):
		http.rhost = 'http://www.yougetsignal.com/tools/web-sites-on-web-server/php/get-web-sites-on-web-server-json-data.php'
		rs = http.post({'remoteAddress':url})
	def parse_html(self,strHtml):
		sitesTmp = []
		htmlUtil = libs.html.html()
		htmlUtil.getUrl(strHtml)
		for url in htmlUtil.links:
			m = urlparse.urlparse(url)
			if len(m.netloc):
				sitesTmp.append(m.netloc)
		sitesTmp.append(self.host)
		sitesTmp = list(set(sitesTmp))
		for site in sitesTmp:
			if self.getHostIp(site)	== self.hostIp:
				if not self.sitesUrl.count(site):
					self.sitesUrl.append(site)
					self.callback(str(site))


# if __name__ == '__main__':
# 	# st = sites('sb.f4ck.com')
# 	# st.getSameIpSites()
# 	socket = socket.socket(socket.INET,socket,socket.STREAM_TCP)

	 