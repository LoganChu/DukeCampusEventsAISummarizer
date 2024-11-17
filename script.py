import time
import requests as rq
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


#Getting the URL for page with campus events on a specific date
url = "https://duke.campusgroups.com/events?from_date=17+Nov+2024&to_date=17+Nov+2024"
#response = rq.get(url)

with sync_playwright() as p:
    # Specify the Edge executable path
    #edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    # Launch Edge using the Chromium engine
    browser = p.chromium.launch(channel="msedge", headless=False)  # Set headless=True for background execution
    page = browser.new_page()

    # Navigate to a URL
    page.goto(url)

    time.sleep(5)

    # Get the rendered page content
    html_content = page.content()
    #Parse HTML Content
    soup = BeautifulSoup(html_content, "html.parser")

    with open("page.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    #Section with all separate event pages
    content = soup.find("ul",id="divAllItems",class_="list-group")
   

    events = []
    for event in content.find_all("li", class_="list-group-item"):  
        event_page = event.find("h3",class_="media-heading header-cg--h4").find("a").get('href')
        name = event.find("h3",class_="media-heading header-cg--h4").get_text()
        print(event_page)
        print(name)
 
    # Close the browser
    browser.close()


#Testing to check actual HTML content of page. Some HTML is rendered through Javascript separately.
""" 
with open("page.html", "w", encoding="utf-8") as file:
    file.write(response.text)
"""

#Checking if url opened properly
"""
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the page")
    exit()
"""






"""
    response = rq.get(event_page)
    if response.status_code == 200:
        html_content = response.text
    else:
        print("Failed to retrieve the page")
        exit()
    soup2 = BeautifulSoup(html_content, "html.parser")
    description = soup2.find("div", class_="card-block").get_text()
    events.append({"Event name": name, "Description": description})
"""

 