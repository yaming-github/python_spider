from os import path
import time
import requests
from bs4 import BeautifulSoup

d = path.dirname(__file__)

def get_page(link):
    # TODO "Cookie" : "******"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    r = requests.get(link, headers = headers)
    html = r.content
    html = html.decode('UTF-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_data(arr):
    f = open(path.join(d, 'comment.txt'), 'a')
    for i in range(len(arr)):
        if (i == 0 or arr[i] != arr[i - 1]) and not arr[i].get_text().startswith('引用内容'):
            f.write(arr[i].get_text() + '\n')
    f.close()

if __name__ == '__main__':
    link = 'https://bbs.hupu.com/39652754-'
    for i in range (155):
        curLink = link + str(i + 1) + '.html'
        soup = get_page(curLink)
        arr = soup.find_all('p', class_ = '', string = True)
        if i == 0:
            arr = arr[8:]
        else:
            arr = arr[:-3]
        if len(arr) > 0:
            get_data(arr)
            print('page ' + str(i) + ' finished')
        time.sleep(2)
