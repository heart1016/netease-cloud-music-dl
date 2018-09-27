import requests
import random
from ncm.constants import headers
from bs4 import BeautifulSoup

ip_list = []
def ip_change():
    proxies = get_random_ip(ip_list)
    return proxies

def url_index(num):
    url = 'http://www.xicidaili.com/nn/%s'% num
    return url

def get_ip_list():
    for j in range(1, 2):
        print("正在获取代理列表...")
        url = url_index(j)
        try:
            html = requests.get(url=url, headers=headers, timeout=10).text
        except:
            html = requests.get(url=url, headers=headers, timeout=10).text
        soup = BeautifulSoup(html, 'lxml')
        ips = soup.find(id='ip_list').find_all('tr')
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            if tds[5].text == 'HTTPS':
                continue
            ip_list.append(tds[1].text + ':' + tds[2].text)
            try:
                requests.get('http://music.163.com', proxies={"http":"http://" + ip_list[-1]}, headers=headers, timeout=10)
            except:
                print ('connect failed')
                ip_list.remove(ip_list[-1])
            else:
                print ('success')
                print("可用ip", len(ip_list))
                print(ip_list[-1])#
            #time.sleep(random.randint(0, 3))
            #print("代理列表抓取成功.")

def get_random_ip(ip_list):
    if ip_list:
        print("正在设置随机代理...")
        proxy_list = []
        while True:
            ip = ip_list[random.randint(0, len(ip_list)-1)]
            try:
                requests.get('http://music.163.com', proxies={"http":"http://" + ip}, headers=headers, timeout=10)
            except:
                print ('connect failed')
                ip_list.remove(ip)
            else:
                print ('success')
                print("可用ip", len(ip_list))
                proxy_list.append('http://' + ip)
                proxy_ip = random.choice(proxy_list)
                proxies = {'http': proxy_ip}
                print("代理设置成功.")
                return proxies
    else:
       get_ip_list()
       get_random_ip(ip_list)
