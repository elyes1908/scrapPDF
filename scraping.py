import glob
from time import sleep

from selenium import webdriver
import os


def scroll():
    pagination_ = driver.find_element_by_css_selector('.page-number')
    driver.execute_script("arguments[0].scrollIntoView();", pagination_)


name, url, last_page = input('name: '), input('url: '), int(input('last_page: '))
course = {
    'name': name,
    'url': url,
    'last_page': last_page}

directory = course['name']
path = f'C:\\Users\\miz\\Downloads\\8\\{directory}\\'
if not os.path.exists(path):
    os.makedirs(path)

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': path}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://rafi9ni.com/')
driver.find_element_by_id('username').send_keys('94199820')
sleep(1)
driver.find_element_by_id('password').send_keys('1573')
sleep(1)
driver.find_element_by_class_name('btn.btn-large.btn-warning').click()
sleep(1)
driver.get(course['url'])
sleep(1)

scroll()
links = []
# last = int(driver.find_element_by_css_selector('.page-last').text)
last = course['last_page']
for i in range(0, last):
    nextBtn = driver.find_element_by_css_selector('.page-next a')
    nextBtn.click()
    sleep(5)
    scroll()
    pages = driver.find_elements_by_css_selector('a[href*="fileDownload"]')
    for page in pages:
        try:
            links.append(page.get_attribute('href'))
        except Exception as e:
            print(e)
            pass
for link in links:
    driver.get(link)
flag = True
while flag:
    if len(glob.glob1(path, "*.pdf")) == len(links):
        flag = False
        print("\r", end="")
        print("C'est bon")
        driver.quit()
    else:
        string = " ..."
        print(end="\r" + "Downloading")
        for char in string:
            print(char, end='')
            sleep(.25)
        sleep(1)
