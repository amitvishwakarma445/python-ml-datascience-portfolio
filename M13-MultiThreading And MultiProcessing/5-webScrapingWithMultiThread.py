### Scenario : web scraping
'''
* Web scaping often involve making numerous network requests to fetch web pages.
* These task are I?O bound becoz they spent a lot of time waiting for responce from servers.
* mutli Threading can significantly improve the performance
of allowing multiple web pages to be fatched concurrently.

'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/docs/concepts/',
    'https://python.langchain.com/docs/tutorials/',
    'https://python.langchain.com/docs/how_to/pydantic_compatibility/'

]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetch {len(soup.text)} characters form {url}')

threads =  []

for url in urls:
    thread = threading.Thread(target=fetch_content, args = (url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("all web pagesfatched")