import urlparse
import urllib2
import os
import sys

try:
	from bs4 import BeautifulSoup
except ImportError:
	print "[*] Please download and install Beautiful Soup first!"
	sys.exit(0)

url = raw_input("[+] Enter the url: ")
folderName = raw_input("[+] Enter name for folder: ")
extension = raw_input("[+] Enter the extension you want, with period before it: ")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
i = 0
request = urllib2.Request(url, None, headers)
html = urllib2.urlopen(request)
soup = BeautifulSoup(html.read())
os.mkdir(folderName)
 # find <a> tags with href in it
for tag in soup.findAll('a', href=True):
	tag['href'] = urlparse.urljoin(url, tag['href'])
	if os.path.splitext(os.path.basename(tag['href']))[1] == extension:
		current = urllib2.urlopen(tag['href'])
		print "[*] Downloading: %s" %(os.path.basename(tag['href']))

		f = open(folderName + "/" + os.path.basename(tag['href']), "wb")
		f.write(current.read())
		f.close()
		i += 1
print "Downloaded %d files" % (i)
raw_input("[+] Press any key to exit...")




