import requests
import bs4
import sys

#root_url = 'http://www.54new.com/'
#index_url = root_url + 'seed-89422.html'
def get_web_data():
	if len(sys.argv)<2:
		return None
	else:
		index_url = sys.argv[1]
		#index_url = root_url + sys.argv[1]
	print index_url
	response = requests.get(index_url);
	soup = bs4.BeautifulSoup(response.text)
	#return [a.attrs.get('href') for a in soup.select('div.siteop')]
	#return [a.get('href') for a in soup.find(id = 'down_link')]
	#return soup.select('a[href="http://www.54new.com/"]')
	return soup.find(id='down_link').get('href')

print get_web_data();