#!/usr/bin/python -u

print "Content-type: text/html"
print
import cgi,cgitb
import time
cgitb.enable()
import subprocess
from extractkeywords import Crawl
from databaseconnect import Database
db=Database('LoginSession','crawler')
db.connect()
form=cgi.FieldStorage()
site=form.getvalue('site')
domain=form.getvalue('domain')
username=form.getvalue('uname')
db.insert1([str(username),str(site)])
link_id=db.view([str(username),str(site)])
#print link_id
x=Crawl(domain,site)
print "<html>"
print "<head>"
print "<title>your query list</title>"
print "</head>"
print '<body>'
x.connect();
x.crawl(link_id);
time.sleep(20)
print "</body>"
print "</html>"

