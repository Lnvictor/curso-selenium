from selenium.webdriver import Firefox
from time import sleep
from ex_02 import find_by_text

browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_04_b.html'
browser.get(url)
sleep(5)

for text in ['um', 'dois', 'tres', 'quatro']:
    find_by_text(browser, 'div', text).click()
