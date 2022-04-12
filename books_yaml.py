from selectorlib import Extractor
import requests
import json
from time import sleep


# Create an extractor by reading the YAML file
e = Extractor.from_yaml_file('selectors.yml')


def scrape(url_):
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0)'
                      'AppleWebKit/537.46 (KHTML, like Gecko) Chrome?51.0.2704.64 Safari/537.36',
        'accept': 'teext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,'
                  '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=9.0,en;q=0.8'}
    print(f'Downloading {url_}')
    r = requests.get(url_, headers=headers)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page {url_} was blocked by Amazon. Please try using better proxies\n")
        else:
            print(f"Page {url_} must have been blocked by Amazon as the status code was {r.status_code}")
        return None
    # Pass the HTML of the page and create
    return e.extract(r.text)


with open("urls.txt", "r") as urllist, open('output.jsonl', 'w') as outfile:
    for url in urllist.readlines():
        data = scrape(url)
        if data:
            json.dump(data, outfile)
            outfile.write('\n')
            sleep(4)