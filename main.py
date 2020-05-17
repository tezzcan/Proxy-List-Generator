from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import json

data = {}
data['proxies'] = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # this shit aint doin nothin

driverPath = 'chromedriver.exe' # Specify the chrome driver location. ( LOL I DID :D )
url = 'https://free-proxy-list.net/' # Of course you can change this bruuuh.

driver = webdriver.Chrome(executable_path=driverPath)

driver.get(url)
select = Select(driver.find_element_by_xpath('//*[@id="proxylisttable_length"]/label/select'))
select.select_by_value('80')

f = open('proxylist.txt','a',encoding='utf8')

for i in range(1,81):
    ip = driver.find_element_by_xpath(f'//*[@id="proxylisttable"]/tbody/tr[{i}]/td[1]').text
    port = driver.find_element_by_xpath(f'//*[@id="proxylisttable"]/tbody/tr[{i}]/td[2]').text
    #proxy = "'http'" + ' : ' + f"'http://{ip}:{port}',"
    proxy = f"'http' : 'http://{ip}:{port}',\n"

    data['proxies'].append({
        'ip' : f'{ip}',
        'port' : f'{port}'
    })

    print(proxy)
    f.write(proxy)

f.close()

with open('proxylist.json','a',encoding='utf8') as p:
    json.dump(data,p)