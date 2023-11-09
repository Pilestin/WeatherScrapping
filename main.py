import request
import bs4 

def main():
	url = "https://www.metoffice.gov.uk/weather/world/turkey/"
	html = request.get(url)
	soup = bs4.BeautifulSoup(html, "html.parser")
	
	# print(soup.prettify())


if __name__ == '__main__':
	main()