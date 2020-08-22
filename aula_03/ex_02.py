from selenium.webdriver import Chrome
from time import sleep


browser = Chrome()

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)
sleep(15)

a = browser.find_element_by_tag_name('a')

while True:
    a.click()
    el = browser.find_elements_by_tag_name('p')
    if 'Você ganhou' in el[-1].text:
        break
    sleep(1)
