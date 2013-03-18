#!/usr/bin/env python
import urllib,urllib2,cookielib,httplib,os,sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
class http:

	def __init__(self):
		self.rhost = ''
		self.postData = {}
		self.header = {'User-Agent':
						'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		self.cookieFile = '/tmp/cookie.dat'
		self.cookie = cookielib.LWPCookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
		urllib2.install_opener(opener)
	def post(self,postData = None):
		self.postData = urllib.urlencode(postData)
		q = self.query()
		result = q.read()
		self.cookie.save(self.cookieFile)
		return result

	def get(self):
		self.postData = urllib.urlencode({})
		q = self.query()
		print q.getcode()
		exit();
		self.cookie.save(self.cookieFile)
		print str(q.read())
	def post_status(self):
		pass
	def get_status(self,file = None):
		conn = httplib.HTTPConnection(self.rhost)
		conn.request(method='POST',url='/%s'%file)
		rs = conn.getresponse()
		print rs.status

	def http_dowload(self,url = None):
		if len(url) > 0:
			rs = urllib.urlopen(url).read()
		else:
			rs = None
		return rs
	def set_postData(self,data = None):
		passls
	def query(self):
		req = urllib2.Request(
                              url = self.rhost,
                              data = self.postData,
                              headers = self.header
                              )
		return urllib2.urlopen(req)


# def main():
# 	hp = http()
# 	hp.rhost = 'sb.f4ck.net'
# 	hp.get_status('thread-6042-1-1.html')

# if __name__ == '__main__':
# 	main()
		