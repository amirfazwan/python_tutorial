#/usr/bin/python


import urllib2
from  bs4 import BeautifulSoup

data = [ ]
url = "http://www.met.gov.my/index.php?option=com_content&task=view&id=3358&Itemid=1930"
string = []

def make_request(url):

	response = urllib2.urlopen(url);

	if response.getcode() == 200:
		content = response.read()

		parser = BeautifulSoup(content)
		get_table = parser.find_all("td")
		
		for i in get_table:
			data.append(i.get_text())	

make_request(url);

array_position = 0

if len(data) > 0:
	for i in data:
		array_position += 1
		string.append({array_position : i})



print string









