import requests
from bs4 import BeautifulSoup

url1 = "http://www.theguardian.com/uk/technology"
url2 = 'http://reddit.com/r/programming'
url3 = 'https://news.ycombinator.com/'
url4 = 'http://www.nytimes.com/pages/technology/index.html'


r1 = requests.get(url1)
r2 = requests.get(url2)
r3 = requests.get(url3)
r4 = requests.get(url4)
#print r.content
soup1 = BeautifulSoup(r1.content)
soup2 = BeautifulSoup(r2.content)
soup3 = BeautifulSoup(r3.content)
soup4 = BeautifulSoup(r4.content)
#print soup.prettify()
#print soup.find_all("a")
links1 = soup1.find_all('a',{'class':'js-headline-text'})
links2 = soup2.find_all('a',{'class':'title'})
links3 = soup3.find_all('a')
links4 = soup4.find_all('a')

user_search = raw_input('Enter the search word: ').upper()

print '\n\nHEADLINES FROM THE GUARDIAN'
for link in links1:
    search_string1 = link.text
    if (search_string1.upper().find(user_search) > -1):
        print '-',search_string1

print '\n\n\n'
print 'HEADLINES FROM REDDIT'
for link in links2:
    search_string2 = link.text
    if (search_string2.upper().find(user_search) > -1):
        print '-',search_string2

print '\n\n\n'
print 'HEADLINES FROM YCOMBINATOR'
for link in links3:
    search_string3 = link.text
    if (search_string3.upper().find(user_search) > -1):
        print '-',search_string3

print '\n\n\n'
print 'HEADLINES FROM THE NY-TIMES'
for link in links4:
    search_string4 = link.text
    if (search_string4.upper().find(user_search) > -1):
        print '-',search_string4