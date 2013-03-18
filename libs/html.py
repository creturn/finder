#!/usr/bin/env python
#coding: utf-8
#autor: return blog: www.creturn.com
import os,sys
from HTMLParser import HTMLParser
import urllib
import urlparse
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
# parser the html 
class html(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.getTag = ''
		self.links = []
		self.tmp = False
		self.getContent = ''
	def handle_starttag(self,tag,attrs):
		if self.getTag == 'url':
			self.filter_tag(tag,attrs,'a','href')
		elif self.getTag == 'img':
			self.filter_tag(tag,attrs,'img','src')
		elif self.getTag == 'content':
			self.parser_content(tag,attrs)
		else:
			print 'No Tag Select!'
	def handle_data(self, data):
		if self.tmp:
			self.getContent = data
			self.tmp = False
	def getUrl(self,html):
		self.getTag = 'url'
		self.feed(html)
		self.close()
	def getImage(self,html):
		self.getTag = 'img'
		self.feed(html)
		self.close()

	def getTagContent(self,html,tag,arrt,arrtValue):
		self.getTag = 'content'
		self.getContentTag = tag
		self.getContentArrt = arrt
		self.getContentArrtValue = arrtValue
		self.feed(html)
		self.close()
	def parser_content(self,tag,attrs):
		if tag == self.getContentTag:
 				for (variable, value) in attrs:
					if variable == self.getContentArrt and value == self.getContentArrtValue:
 						self.tmp = True
 						print self.get_starttag_text()
		
 	def filter_tag(self,tag,attrs,get_tag,get_attr):
 		if tag == get_tag:
 			if len(attrs):
 				for (variable, value) in attrs:
 					if variable == get_attr:
 						self.links.append(value)
 		self.links = list(set(self.links))


# def main():
# 	url = 'http://cn.bing.com/search?q=ip:61.129.57.32'
# 	strs= urllib.urlopen(url).read()
# 	# print urlparse.urlparse(url)
# 	hp = html()
	 

# 	# hp.getUrl(strs)
# 	# for url in hp.links:
# 	# 	rs = urlparse.urlparse(url)
# 	# 	if len(rs.netloc):
# 	# 		print rs.netloc
# 	# hp.getTagContent(strs,'div','id','results')
#  # 	print hp.getContent
# if __name__ == '__main__':
# 	main()
		
		