from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # this shit aint doin nothin

driverPath = 'chromedriver.exe' # Specify the chrome driver location. LOL I DID :D
url = 'https://free-proxy-list.net/' # Of course you can change this bruuuh.

driver = webdriver.Chrome(executable_path=driverPath)

driver.get(url)
select = Select(driver.find_element_by_xpath('//*[@id="proxylisttable_length"]/label/select'))
select.select_by_value('80')

for i in range(1,81):
    with open('proxylist.txt','a',encoding='utf8') as f:
        ip = driver.find_element_by_xpath(f'//*[@id="proxylisttable"]/tbody/tr[{i}]/td[1]').text
        port = driver.find_element_by_xpath(f'//*[@id="proxylisttable"]/tbody/tr[{i}]/td[2]').text
        proxy = "'http'" + ' : ' + f"'http://{ip}:{port}',"

        print(proxy)
        f.write(proxy + '\n')