#############################################################
## [Developer] → cholong02                                 ##
## [DATE] → 2020-07-24                                     ##
#############################################################
## [Description] →                                         ##
## keyword를 입력하면 한국대학신문에서 뉴스를 검색하고         ##
## 2019년~현재까지 기사만 수집하여 txt파일로 저장한는 프로그램 ##
#############################################################

from bs4 import BeautifulSoup
import requests
import os

keyword = '전남대학교' # 대학뉴스에서 검색할 키워드
page = 1              # 뉴스 리스트 Page
count = 0             # 뉴스 건수
flag = 0
total_doc = ''

url = 'http://news.unn.net/news/articleList.html?page={}&total=393&sc_area=A&view_type=sm&sc_word={}'.format(page, keyword)
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
    url = 'http://news.unn.net/news/articleList.html?page={}&total=393&sc_area=A&view_type=sm&sc_word={}'.format(page,keyword)
    doc = requests.get(url)

    soup = BeautifulSoup(doc.text, 'html.parser')
    news_list = soup.select('section.article-list-content div.list-block')

    if flag == 1:
        break

    for news in news_list:
        # 기사 날짜 추출(범위 정하기위해 날짜 계산)
        date_line = news.select('div.list-dated')[0].text
        pre_date = date_line[-16:-9]
        date = pre_date.replace('-', '')

        if int(date) <= 201812:
            flag = 1
            break

        count += 1
        href = 'http://news.unn.net' + news.select('div.list-titles > a')[0]['href']
        doc = requests.get(href)

        bs4 = BeautifulSoup(doc.text, 'html.parser')
        title = bs4.select('div.article-head-title')[0].text.strip()
        content_list = bs4.select('div#article-view-content-div P')

        contents = ''
        for i, p in enumerate(content_list):
            if i == 0:
                num = p.get_text().find(']')
                contents = p.get_text()[num+2:].strip()
                continue
            contents += p.get_text().strip()
        print('[DATE] →', date)
        print('[TITLE] →', title)
        print('[CONTENTS] →', contents)

        total_doc += title + ' ' + contents
        # total_doc += title
    page += 1

print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
print('▒▒ 한국대학신문에서 \'{}\'관련 뉴스 {}건 수집되었습니다.'.format(keyword, count))
print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')

# 파일로 저장
if os.path.isfile('../files/total_contents.txt'):
    with open('../files/total_contents.txt', 'a', encoding='UTF8') as f:
        f.write(' ' + total_doc)
else:
    with open('../files/total_contents.txt', 'w', encoding='UTF8') as f:
        f.write(total_doc)
f.close()

