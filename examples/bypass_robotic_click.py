from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("file:///home/thalison/Documentos/beemon/antiscraping-toolkit/examples/robotic_click.html")

# utiliza action chains para hover
hover = ActionChains(driver)
hover.move_to_element(driver.find_element(By.ID, 'botao')).perform()

# clica no botão
driver.find_element(By.ID, 'botao').click()

input()
