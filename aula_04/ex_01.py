from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_04_a.html'
browser.get(url)
sleep(15)

ul = browser.find_elements_by_tag_name('ul')
print(ul[0].find_element_by_tag_name('li').find_element_by_tag_name('a').text)
