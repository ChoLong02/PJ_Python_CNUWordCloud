#############################################################
## [Developer] → cholong02                                 ##
## [DATE] → 2020-07-24                                     ##
#############################################################
## [Description] → 전남대학교 포털에서 2020년 뉴스 수집      ##
#############################################################

from bs4 import BeautifulSoup
import requests
import os

page = 1              # 뉴스 리스트 Page
count = 0             # 뉴스 건수
flag = 0
total_doc = ''

url = 'http://cnutoday.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=146&page={}&'.format(page)
doc = requests.get(url)
if doc.status_code != 200:
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒ [Message] → Not Found Page:/')
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
else:
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒ [Message] → Start Crawling:)')
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')

while True:
    url = 'http://cnutoday.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=146&page={}&'.format(page)
    doc = requests.get(url)

    soup = BeautifulSoup(doc.text, 'html.parser')
    news_list = soup.select('div.mainnews_text')

    if flag == 1:
        break

    for news in news_list:
        date = news.select('span.write_date')[0].text[:7].replace('-', '')

        # 2020년도 기사만 수집
        if int(date) <= 201912:
            flag = 1
            break

        count += 1
        title_src = news.select('a')[0]['onclick']
        href = url + title_src[title_src.find('\'')+1:title_src.rfind('\'')]

        doc = requests.get(href)

        bs4 = BeautifulSoup(doc.text, 'html.parser')
        title = bs4.select('div.article_view > h1')[0].text.strip()
        content_list = bs4.select('div.article_view > p')

        contents = ''
        for i, p in enumerate(content_list):
            if p == '':
                continue
            contents += p.get_text().strip()

        print('[DATE] →', date)
        print('[TITLE] →', title)
        print('[CONTENTS] →', contents)

        total_doc += title + ' ' + contents
        # total_doc += title
    page += 1


print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
print('▒▒ 전남대학교 포털에서 뉴스 {}건 수집되었습니다.'.format(count))
print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')


# 파일로 저장
if os.path.isfile('../files/total_contents.txt'):
    with open('../files/total_contents.txt', 'a', encoding='UTF8') as f:
        f.write(' ' + total_doc)
else:
    with open('../files/total_contents.txt', 'w', encoding='UTF8') as f:
        f.write(total_doc)
f.close()