import requests
from bs4 import BeautifulSoup as bs

headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
url = "https://www.amazon.com/gp/new-releases/books/10484?ref_=Oct_d_onr_S&pd_rd_w=a5dSS&pf_rd_p=" \
      "a8f3a30d-9e11-4355-859f-4ec616e3a77c&pf_rd_r=AGZ8PFZQPBP0Q9SP4G6A&pd_rd_r=" \
      "4aeac866-f631-4509-96a2-72c6621c090e&pd_rd_wg=mXzu2"
page = requests.get(url, headers=headers)
soup = bs(page.text, 'lxml')
items = soup.findAll("div", class_="a-column a-span12 a-text-center "
                                   "_p13n-zg-list-grid-desktop_style_grid-column__2hIsc")


def print_to_disk(url_):
    base = 'https://amazon.com'
    with open('urls.txt', 'a') as f:
        f.write(base+str(url_)+'\n')


for item in items:
    link = item.find("a", class_='a-link-normal')['href']
    print_to_disk(link)
