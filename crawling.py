from bs4 import BeautifulSoup
from urllib.request import urlopen

print("start")
response = urlopen('https://naver.com/')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("C:/Users/master/새파일.txt", 'w')
for anchor in soup.select('span.an_txt'):
    data = str(i) + "위 :" + anchor.get_text() + "\n"
    print(anchor.get_text())
    f.write(data)

f.close()
print("end")


