from selenium import webdriver
import time
from pprint import pprint
import schedule
from datetime import datetime

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://www.totalcorner.com/match/today')
navegador.implicitly_wait(10)

tabelageral = navegador.find_element_by_xpath('//*[@id="inplay_match_table"]/tbody[3]')
jogos = tabelageral.find_elements_by_tag_name('tr')

dic = {}
for jogo in jogos:
    campeonato = (jogo.find_element_by_css_selector('.text-center.td_league')).text
    minjogo = (jogo.find_element_by_css_selector('.text-center.match_status')).text
    casa = (((jogo.find_element_by_css_selector('.text-right.match_home')).find_element_by_tag_name(
        'a')).find_element_by_tag_name('span')).text
    fora = (((jogo.find_element_by_css_selector('.text-left.match_away')).find_element_by_tag_name(
        'a')).find_element_by_tag_name('span')).text
    id = (f'{casa}{fora}')
    placar = (jogo.find_element_by_css_selector('.text-center.match_goal')).text
    placarcasa = placar[0]
    placarfora = placar[-1]
    placartot = int(placarcasa) + int(placarfora)
    dic[id] = {'Campeonato': campeonato, 'MinutosJogo': minjogo,'TimeCasa':casa,'TimeFora': fora,'PlacarCasa':int(placarcasa),'PlacarFora': int(placarfora),'PlacarTot': placartot}
    idsparatestes = dic.keys()

x = 0
while x < 1000:
#def loop():
    tabelageral = navegador.find_element_by_xpath('//*[@id="inplay_match_table"]/tbody[3]')
    jogos = tabelageral.find_elements_by_tag_name('tr')
    dic2 = {}
    for jogo in jogos:
        campeonato = (jogo.find_element_by_css_selector('.text-center.td_league')).text
        minjogo = (jogo.find_element_by_css_selector('.text-center.match_status')).text
        casa = (((jogo.find_element_by_css_selector('.text-right.match_home')).find_element_by_tag_name(
            'a')).find_element_by_tag_name('span')).text
        fora = (((jogo.find_element_by_css_selector('.text-left.match_away')).find_element_by_tag_name(
            'a')).find_element_by_tag_name('span')).text
        id = (f'{casa}{fora}')
        placar = (jogo.find_element_by_css_selector('.text-center.match_goal')).text
        placarcasa = placar[0]
        placarfora = placar[-1]
        placartot = int(placarcasa) + int(placarfora)
        dic2[id] = {'Campeonato': campeonato, 'MinutosJogo': minjogo,'TimeCasa':casa,'TimeFora': fora,'PlacarCasa':int(placarcasa),'PlacarFora': int(placarfora),'PlacarTot': placartot}
        idsparatestes2 = dic2.keys()

    for idsparateste in idsparatestes:

        try:
            placarid1 = dic[idsparateste].get('PlacarTot')
            placarid2 = dic2[idsparateste].get('PlacarTot')
            if placarid1 != placarid2:
                print(f'GOL! {dic2[idsparateste].get("MinutosJogo")}: {dic[idsparateste].get("TimeCasa")} x {dic[idsparateste].get("TimeFora")} : {dic2[idsparateste].get("PlacarCasa")}x{dic2[idsparateste].get("PlacarFora")} ')
        except KeyError:
            continue
    print(f'Len do dic: {len(dic)} e do dic2: {len(dic2)}')
    dic = dic2.copy()
    dic2.clear()
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Ciclo finalizado: {hora}')
    x = x+1


'''
schedule.every(1).minutes.do(loop)
while 1:
    schedule.run_pending()
    time.sleep(10)
'''




