from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.trivago.com.br")

cidade = driver.find_element_by_id("querytext").send_keys('Manaus')
sleep(2)
buscar = driver.find_element_by_class_name('search-button__label').click()
fechar = driver.find_element_by_css_selector('[class="dealform-button js-dealform-button-calendar dealform-button--checkin dealform-button--highlight"]').click()
ordenar = driver.find_element_by_id("mf-select-sortby").click()
avaliacoes = driver.find_element_by_css_selector('[value="7"]').click()

#verifica_nome = driver.find_elements_by_css_selector('[class="accommodation-list__title--9a21e"]')


#tamanho = len(verifica_nome)


#if(tamanho > 0):
#    for nome in verifica_nome:
#       print("Nome verificado: " + nome.text)
    
#else:
#   print("Nome nao existe")
