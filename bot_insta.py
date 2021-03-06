"""
Autor: Raul Braga
Bot de comentarios para instagram...
Linkedin: https://www.linkedin.com/in/raulbragaof/
Contato: raulsilva67@outlook.com.br
Baixar o driver da sua preferencia.
Duvidas leia a documentação do Selenium.
https://www.selenium.dev/pt-br/
"""

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

usuario_login = input("Usuario: ")
usuario_senha = input("Senha: ")
link_foto = input("Link publicação: ")
texto_escrever = input("O que deseja escrever: ")
comentario_quant = input("Quantas vezes: ")
comentario_quant = int(comentario_quant)

navegador = webdriver.Edge()
navegador.maximize_window()
navegador.get("https://www.instagram.com/")
time.sleep(8)

navegador.find_element(
    By.XPATH,
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label"
    "/input",
).send_keys(usuario_login)
time.sleep(5)
navegador.find_element(
    By.XPATH,
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/"
    "label/input",
).send_keys(usuario_senha)
time.sleep(5)
navegador.find_element(
    By.XPATH,
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]" "",
).click()
time.sleep(8)
navegador.find_element(
    By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button"
).click()
navegador.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/"
    "div/div/div/div[3]/button[2]",
).click()

time.sleep(8)
navegador.get(link_foto)
time.sleep(8)

inicio = 0
while inicio <= comentario_quant:
    navegador.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea",
    ).click()
    time.sleep(0.8)
    navegador.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea",
    ).send_keys(texto_escrever)
    time.sleep(8)
    navegador.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea",
    ).send_keys(Keys.ENTER)
    navegador.refresh()
    time.sleep(9)
    inicio = inicio + 1
else:
    print("Comentarios enviados!, Encerrando...")
