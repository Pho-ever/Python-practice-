import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.nytimes.com/')
soup = BeautifulSoup(page.text,'html.parser')

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace('\n','').strip())
    else:
        print(story_heading.content[0].strip())
