import urllib.request
import re,time
import os
import urllib

print('Welcome to use crawlers. __author__: Sacred Universe')

chaper_url="https://zh.nyahentai.fun/g/342513/"

path = 'D:\\pictures\\pictures\\E hentai\\test'  # 保存地址

if not os.path.isdir(path):
    os.makedirs(path)  
paths = path + '\\' 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

req = urllib.request.Request(url=chaper_url, headers=headers)

def get_html(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    print('初めまして')
    return html_a.decode('utf-8')

html_b = get_html(req)  

html=html_b
print('jpg format:')

reg = r'https://[^\s]*?\.jpg'
imgre = re.compile(reg)  
imglist = imgre.findall(html)  
x = 0        
print('finished searching')


opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
print('total list length:%d'%len(imglist))
for imgurl in imglist:
    time.sleep(1)
    print('#',end='')
    urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths, x))  
    x = x + 1


print('finished. __author__: Sacred Universe. El psy Congroo')


