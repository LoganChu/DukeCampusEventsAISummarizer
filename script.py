import requests as rq
from bs4 import BeautifulSoup
import csv

#Getting the URL for page with campus events on a specific date
url = "https://duke.campusgroups.com/events?from_date=17+Nov+2024&to_date=17+Nov+2024"
response = rq.get(url)

#Checking if url opened properly
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the page")
    exit()


soup = BeautifulSoup(html_content, "html.parser")

#Section with all separate event pages
content = soup.find("ul",id="divAllItems",class_="list-group")

events = []
for event in content.find_all("li", class_="list-group-item"):  
    event_page = event.find("h3",class_="media-heading header-cg--h4").find("a").get('href')
    name = event.find("h3",class_="media-heading header-cg--h4").get_text()
    print(event_page)
    print(name)
 