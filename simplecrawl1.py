from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPProxyAuth
class Crawl:
	
	def __init__(self):
		self.domain=['http://www.iiita.ac.in',]
		self.url='http://www.iiita.ac.in'
	
	def connect(self):
		self.req=requests.get('http://www.iiita.ac.in')
		if self.req.status_code != 200:
			print 'Error Check Internet Connection'
			sys.exit()
	
	def  websiteok(self,url):
		r = requests.head(url)
		return r.status_code == 200

	def crawl(self):
		count = 0
		li=[self.req]
		link_file = open('links.txt','w+')
		link_file2 = open('links.txt','r+')
		link_file.write(str(self.url)+'\n')
		for line in link_file2:
			try:
				#print urls[count]
				#link_file.write(urls[count-1]+'\n')
				req=requests.get(str(line))
				print req.status_code
				r = requests.head(urls[count])
				print r.status_code
				if req.status_code == 200 and r.status_code == 200: 
					page = li[count].text
					link_file2.write(str(line)+'\n')
					count = count+1;
					print 'hello'
					if(count == 50):
						sys.exit()
					soup = BeautifulSoup(page,'lxml')
					for a in soup.find_all(href=True):
						urls.append(str(self.domain[0])+str(a['href']))
						link_file2.write(str(self.domain[0])+str(a['href'])+'\n')
						
					del li[count-1]
			except requests.exceptions.ConnectionError as e:
				count=count +1 	

x=Crawl()
x.connect()
x.crawl()	
		
