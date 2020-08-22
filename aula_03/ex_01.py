from selenium.webdriver import Chrome
from time import sleep


dc = {'h1': {}}
navegador = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

navegador.get(url)
sleep(30)

li = navegador.find_elements_by_tag_name('p')

for el in li:
    dc['h1'][el.get_attribute('atributo')] = el.text

navegador.quit()
print(dc)
