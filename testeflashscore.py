import pandas as pd
from pprint import pprint
from selenium import webdriver
import csv


navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://www.flashscore.com.br/futebol/brasil/serie-b/resultados/')
navegador.implicitly_wait(10)


resultados = {}
x = 0
jogos = navegador.find_elements_by_css_selector(".event__match.event__match--static.event__match--oneLine")
foras = navegador.find_elements_by_css_selector(".event__participant.event__participant--away")
casas = navegador.find_elements_by_css_selector(".event__participant.event__participant--home")
horarios = navegador.find_elements_by_class_name("event__time")
placares = navegador.find_elements_by_class_name("event__part")

dic = {}
codigos= navegador.find_elements_by_xpath("//*[starts-with(@id, 'g_1_')]")

for codigo in codigos:
    ids = codigo.get_attribute('id')
    idslimpa = ids[4:]
    dic[idslimpa]= (f'https://www.flashscore.com.br/jogo/{idslimpa}/#resumo-de-jogo')

links = list(dic.values())

while x < len(jogos):
    fora = foras[x].text
    casa = casas[x].text
    placar = placares[x].text
    horario = horarios[x].text
    linksjogo = links[x]
    resultados[x] = (horario,casa,fora,placar[1:3],placar[-3:-1],linksjogo)
    x = x + 1

row1 = ['Data','TimeCasa', 'TimeFora','PlacarCasa','PlacarFora','LinkJogo']
coluna1 = resultados.keys()
rows = resultados.values()
#pprint(resultados)

f = open("teste.csv","a",newline="",encoding='utf-8')   #se for para usar no excel, tirar o encoding
with f:
    writer = csv.writer(f)
    writer.writerow(row1)
    writer.writerows(rows)
f.close()


## até aqui deu certo! faltou aprender adicionar 1 coluna à tabela
#df = pd.read_csv('teste2.csv')
#df.insert(0,"ID",[coluna1])