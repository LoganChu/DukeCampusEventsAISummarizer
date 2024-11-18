import time
import requests as rq
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from datetime import datetime

now = datetime.now()

current_day = now.day
current_month = now.strftime("%b")
current_year = now.year

#Getting the URL for page with campus events on a specific date
url = f"https://duke.campusgroups.com/events?from_date={current_day}+{current_month}+{current_year}&to_date={current_day}+{current_month}+{current_year}"
#response = rq.get(url)
with open("data.txt", "w", encoding="utf-8") as file:
    with sync_playwright() as p:
        # Specify the Edge executable path
        #edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

        # Launch Edge using the Chromium engine
        browser = p.chromium.launch(channel="msedge", headless=False)  # Set headless=True for background execution
        page = browser.new_page()

        # Navigate to a URL
        page.goto(url)
        time.sleep(3)

        # Get the rendered page content
        html_content = page.content()
        #Parse HTML Content
        soup = BeautifulSoup(html_content, "html.parser")

        #Section with all separate event pages
        content = soup.find("ul",id="divAllItems",class_="list-group")
        
        index = 0
        events = []
        for event in content.find_all("li", class_="list-group-item"):  
            if(index==0):
                index+=1
                continue
            event_page = event.find("h3",class_="media-heading header-cg--h4").find("a").get('href')
            name = event.find("h3",class_="media-heading header-cg--h4").get_text()
            file.write(name + "\n")
            page.goto("https://duke.campusgroups.com"+event_page)
            contents = page.content()
            soup = BeautifulSoup(contents, "html.parser")
            description = " ".join((soup.find("div",id="event_details").find("div",class_="card-block").get_text()).split())
            file.write(description + "\n")
            time.sleep(3)
            index+=1

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

 