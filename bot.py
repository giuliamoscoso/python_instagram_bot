import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(5)

# login
campo_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
campo_senha = '//*[@id="loginForm"]/div/div[2]/div/label/input'
notif_classe = '_a9_1'
notif_conversa_classe = 'xzolkzo'
msg_padrao_fullpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span'
contato_cliente_classe = 'x1yrsyyn'
mensagens_classe = 'x1mzt3pk'
text_area_classe = 'x1odjw0f'


login = driver.find_element(By.XPATH, campo_login)
login.click()
login.send_keys('projectstest123')
time.sleep(1)

senha = driver.find_element(By.XPATH, campo_senha)
senha.click()
senha.send_keys('quUqAfYqBTl@SI4')
time.sleep(1)
senha.send_keys(Keys.ENTER)
time.sleep(5)

# chat
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)
notif_classe = driver.find_element(By.CLASS_NAME, notif_classe)
time.sleep(1)
notif_classe.click()

def handling_notifications():
	try:
		# Acessa última conversa
		notif_conversa = driver.find_element(By.CLASS_NAME, notif_conversa_classe)
		notif_conversa = driver.find_elements(By.CLASS_NAME, notif_conversa_classe)
		clica_notif_conversa = notif_conversa[-1] # obtém última notificação recebida
		acao_notif_conversa = webdriver.common.action_chains.ActionChains(driver)
		acao_notif_conversa.move_to_element_with_offset(clica_notif_conversa, 0, -20)
		acao_notif_conversa.click()
		acao_notif_conversa.perform()
		time.sleep(3)

		# Obtém contato da conversa
		contato = driver.find_elements(By.CLASS_NAME, contato_cliente_classe)
		contato_final = contato[1]
		contato_nome = contato_final.text

		# Obtém última mensagem da conversa
		mensagens = driver.find_elements(By.CLASS_NAME, mensagens_classe)
		mensagens_texto = [mensagem.text for mensagem in mensagens]
		mensagem = mensagens_texto[-1]
		print(contato_nome, ' -> ', mensagem)
		time.sleep(2)

		# Responde mensagem
		text_area = driver.find_element(By.CLASS_NAME, text_area_classe)
		text_area.send_keys("Olá, sou um robô de atendimento!", Keys.ENTER)
		time.sleep(3)

		# Retorna para listagem das conversas
		msg_padrao = driver.find_element(By.XPATH, msg_padrao_fullpath)
		time.sleep(1)
		msg_padrao.click()
	except:
		print('aguarde')
		time.sleep(1)

while True:
	handling_notifications()
