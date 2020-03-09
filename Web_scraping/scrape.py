import requests
from bs4 import BeautifulSoup
import pprint
from urllib.parse import urljoin


def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
	hn = []
	for index, item in enumerate(links):
		title = links[index].getText()
		href = links[index].get('href', None)
		vote = subtext[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99 :
				hn.append({'title': title, 'link': href, 'votes': points})

	return sort_stories_by_votes(hn)

url = 'https://news.ycombinator.com/news'
links = []
subtext = []

while(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	
	links += soup.select('.storylink')
	subtext += soup.select('.subtext')
	morelink = soup.select('.morelink')

	if (len(morelink) != 0):
		nextpage = morelink[0].get('href')
		url = urljoin('https://news.ycombinator.com/', nextpage)
	else:
		pprint.pprint(create_custom_hn(links, subtext))
		break




