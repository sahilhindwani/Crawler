from databaseconnect import Database
from bs4 import BeautifulSoup
import requests
import rake
import sys
from requests.auth import HTTPProxyAuth


class Crawl:
	
	def __init__(self,domain,url):
		self.domain=[domain,]
		self.url=url
	
	def connect(self):
		try:
			http_proxy  = "http://172.31.1.4:8080"
			https_proxy = "http://172.31.1.4:8080"
			ftp_proxy   = "ftp://172.31.1.4:8080"
			proxyDict = { "http"  : http_proxy,"https" : https_proxy,"ftp"   : ftp_proxy}
			self.req=requests.get(self.url);
#			print self.req.status_code
			if self.req.status_code != 200:
				print 'Error Check Internet Connection'
				sys.exit()
		except requests.exceptions.ConnectionError as e:
			print e	
				

	def get_links(self,url):
		links=set()
		try:
			http_proxy  = "http://172.31.1.4:8080/"
			https_proxy = "https://172.31.1.4:8080/"
			ftp_proxy   = "ftp://172.31.1.4:8080/"
			proxyDict={"http"  : http_proxy,"https" : https_proxy,"ftp"   : ftp_proxy}
			req=requests.get(url);
			page=req.text
			soup=BeautifulSoup(page,'lxml')
			for a in soup.find_all(href=True):
				newurl=a['href']
				if newurl.startswith('//'):
					link='https:'+newurl
					if self.domain[0] in link:
						links.add(link)
				if a['href'].startswith('/'):
					links.add(url+a['href'])
				elif newurl.startswith('http'):
					link=a['href']
					if self.domain[0] in link:
			     	  		links.add(a['href'])

		except requests.exceptions.ConnectionError as e:
				print "none";
		return links
	def  websiteok(self,url):
		r = requests.head(url)
		return r.status_code == 200

	def crawl(self,link_id):
		urls=set()
		x=Database('Result','crawler')
		x.connect()
		visited=set()
#print self.url
		urls.add(self.url)
		count = 0
		#xy=str()+'.txt'
		#dp=open(xy,'w+')
		while count <= 1000:
				if len(urls) == 0:
					break;
				url = urls.pop()
#				print url
				if url in visited:
					continue
				print "<p><a href="+url+">"+url+"</a></p>"
#sys.stdout.flush()
				try:
					ur=unicode(url,'utf-8',errors='ignore')
				except TypeError:
					continue			
				rake_object = rake.Rake("SmartStoplist.txt", 3, 1, 1)
				try:
					http_proxy  = "http://172.31.1.4:8080/"
					https_proxy = "https://172.31.1.4:8080/"
					ftp_proxy   = "ftp://172.31.1.4:8080"
					proxyDict={"http"  : http_proxy,"https" : https_proxy,"ftp"   : ftp_proxy}
					req=requests.get(url);
					if req.status_code == 200:
						page=req.text
						u=""
						xy=page.title+'.html'
						dp=open(xy,'w+')
						dp.write(str(page));
						soup=BeautifulSoup(page,'lxml')
						for p in soup.find_all('p'):
							s=''.join(p.find_all(text=True))
							keyword=rake_object.run(s)
							c = 0
							for s in keyword:
								c=c +1
#								print s
								if c > 10:
									break
								u=u+str(s)+','
						for p in soup.find_all('li'):
							s=''.join(p.find_all(text=True))
							keyword=rake_object.run(s)
							c = 0	
							for s in keyword:
								c=c +1
								if c > 2:
									break
								u=u+str(s)+','
						u=u.replace("'",'"')
						dp.write(str(u));
						x.insert([str(count),str(ur),u])
				except requests.exceptions.ConnectionError as e:
					continue
				count = count +1
				if url not in visited:
					links = self.get_links(url)
#					print links
					for l in links:
						urls.add(l)
					visited.add(url)
#dp.write(str(urls))
	def query(self,url):
		x=Database('ukey','crawler')
		x.connect()
		x.view(url)


if __name__ == "__main__":
	x=Crawl(sys.argv[1],sys.argv[2]);
	x.connect()
	x.crawl()
