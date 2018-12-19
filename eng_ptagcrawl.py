import bs4
from urllib.request import urlopen as uReq
from urllib.request import Request
from urllib.parse import quote
from bs4 import BeautifulSoup as soup
import re
import time
import io

def get_time():
	return time.asctime(time.localtime(time.time()))

def crawl(href,count):
	print(get_time() + ", Parsing Link: " + href)
	

	req = Request(href, headers={'User-Agent': 'Mozilla/5.0'})

	uClient = uReq(req)
	page_html = uClient.read()
	uClient.close()
	
	page_soup = soup(page_html, "html.parser")
	heading = page_soup.find('center')
	content_container = page_soup.find('table', attrs={'style' : "background:transparent; text-align:justify;"}).prettify()
	
	table = soup(content_container,"html.parser")	
	
	para = table.find_all('p')
	
	#name = str(count)+".html"
	with io.open("para_en.html", "a", encoding="utf-8") as fout:
		#fout.write("\n\n" + heading.text + "\n\n")
		#	for i in para:
	 	#print(para[i])
		fout.write(str(para))
		

	link = page_soup.find('img', attrs={'alt' : 'Next.png'})
	next_link = link.findPrevious('a')['href']
	complete_link = "http://en.krishnakosh.org" + quote(next_link, safe='%,/')

	return complete_link


base = "http://en.krishnakosh.org/krishna/Narayaneeyam"

my_url = "http://en.krishnakosh.org/krishna/Narayaneeyam_1"

counter=1

while(my_url != base):
	my_url = crawl(my_url,counter)
	counter=counter+1
			
print(get_time() + ": First page match found, exiting...")
print(get_time() + ": Parsing Complete")
