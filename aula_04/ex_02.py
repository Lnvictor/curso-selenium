from selenium.webdriver import Firefox
from time import sleep


def find_by_text(browser, tag, text):
    """
    Encontrar um elemento com o texto

    Argumentos:
        browser - Instancia do browser
        text - texto do elemento
        tag - tag onde o texto será procurado

    retorno:
        elemento em si
    """

    elementos = browser.find_elements_by_tag_name(tag)  # retornará uma lista

    for elemento in elementos:
        if elemento.text == text:
            elemento.click()
            return elemento


def find_by_href(browser, link):
    """
    Encontrar um elemento 'a' com o link

    Argumentos:
        - browser: Instância do navegador
        - link: link de apontamento na âncora

    Retorno:
        - elemento procurado
    """

    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if elemento.get_attribute('href') == link:
            return elemento

if __name__ == '__main__':
    browser = Firefox()
    url = 'http://selenium.dunossauro.live/aula_04_a.html'
    browser.get(url)
    sleep(5)
    elemento_ddg = find_by_href(browser, 'http://google.com.br/')
    elemento_ddg.click()
