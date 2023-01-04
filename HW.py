import bs4 as bs4
import requests
from constants import HEADERS

KEYWORDS = {'дизайн', 'фото', 'web', 'Python', 'python'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    previews = [x.span.text for x in article.find_all('span', class_="tm-article-snippet__hubs-item")]
    date = article.time.text
    title = article.find('a', class_='tm-article-snippet__title-link')
    href = title['href']
    span_title = title.text
    # print(span_title)
    # print(date)
    # print(previews)

    for x in previews:
        if x in KEYWORDS:
            result = f'Дата: {date} - Заголовок: {span_title} - Ссылка: {base_url + href}'
            print(result)
            break