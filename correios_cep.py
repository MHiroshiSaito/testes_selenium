from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.buscacep.correios.com.br")

buscacep = driver.find_element_by_css_selector('[alt="Buscar CEP"]').click()
endereco = driver.find_element_by_name("endereco").send_keys('69082-700')
pesquisar = driver.find_element_by_name("btn_pesquisar").click()