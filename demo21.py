import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.nytimes.com/')
soup = BeautifulSoup(page.text,'html.parser')

web_scrapping = input('Save this file as: \n')
with(web_scrapping,'w') as web:
    
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            web.write(story_heading.a.text.replace('\n','').strip())
        else:
            web.write(story_heading.content[0].strip())
