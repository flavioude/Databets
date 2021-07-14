from selenium import webdriver
import time
from pprint import pprint
import csv
from selenium.common.exceptions import NoSuchElementException



navegador = webdriver.Chrome()
navegador.maximize_window()
url = 'https://www.totalcorner.com/league/view/'
page = 1
while page < 10:
    navegador.implicitly_wait(10)
    #---- Encontrando todos botões "O." de escanteios ----
    navegador.get(f'{url}{page}')
    botaoO = navegador.find_elements_by_xpath('//a[contains(@href,"/match/odds-handicap/")]')
    x = 0
    dic ={}
    for botao in botaoO:    # Dic com todos os botões "O."
        dic[x] = botao.get_attribute('href')
        x = x + 1
    #----

    #----Loop para clicar nos botões----
    cliques = int(len(dic))
    y = 0
    while y < cliques:
        navegador.get(dic[y])
        time.sleep(2)

        #---- Encontrando a Tabela de Cantos, e selecionando as linhas da tabela
        try:
            tabelacorner = navegador.find_element_by_id("corners_full")
            linhas = tabelacorner.find_elements_by_tag_name('tr')
            row1 = ['MinJogo','CornerCasa','CornerFora', 'OddOver','LinhaCorner','OddUnder','Dia','hora']  #indice do csv
            # ----Criando o Título para o CSV
            titulocasa = (navegador.find_element_by_xpath('//*[@id="match_title_div"]/h1/a[2]')).text
            titulofora = (navegador.find_element_by_xpath('//*[@id="match_title_div"]/h1/a[3]')).text
            titulodata = (navegador.find_element_by_xpath('//*[@id="match_title_div"]/h1/small')).text
            titulodatalimpo = (titulodata.split(" "))[0]
            nome = str(f'{titulocasa}{titulofora}{titulodatalimpo}')
            #----Loop para formatar as linhas da tabela de cantos (id=corner_full)
            linha = 0
            teste = {}
            while linha < len(linhas):
                row = linhas[linha].text
                rowlimpa = row.split(" ")
                rowlimpa.pop(1)
                rowlimpa.pop(2)
                teste[linha] = (rowlimpa)
                linha = linha +1
            teste.pop(0) #retirando a primeira linha ( já foi criado a linha indice anteriormente = row1)
            rowsvalendo = teste.values()  #rows com os dados importados
            time.sleep(2)
            #----Criando o CSV
            f = open(nome+".csv","a",newline="",encoding='utf-8')   #se for para usar no excel, tirar o encoding
            with f:
                writer = csv.writer(f)
                writer.writerow(row1)
                writer.writerows(rowsvalendo)
            f.close()
                    #----
            y = y + 1 #passo para o clique
            print(y)
            print(nome)
            navegador.back()
        except NoSuchElementException:
            y = y + 1
            navegador.back() #retornar para a página inicial
    page = page + 1







