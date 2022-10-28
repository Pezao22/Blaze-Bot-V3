import requests
import telebot
import time
import os

TOKEN = '5600428486:AAEWlt0xTIVd8C5kZf2bm5wrN_YtRchynAQ' # BOT TOKEN

bot = telebot.TeleBot(TOKEN)

chat_id = '-1001770985497' # CHAT ID DO CANAL ONDE DESEJA ENVIAR MSG

ray2 = []    # NAO ALTERAR
loop = 0     # NAO ALTERAR
gale = False # NAO ALTERAR
acertos = 0  # NAO ALTERAR
erros = 0    # NAO ALTERAR

jogadas = [  # ADICIONE SEUS PALPITES PREDEFINIDOS AQUI, USE OS ABAIXO COMO EXEMPLO
    ['Preto', 'Preto', 'Preto', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Vermelho'], # PADRAO WILLIAM
    ['Branco', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho'], # PADRAO WILLIAM
    ['Preto', 'Preto', 'Preto', 'Preto', 'Preto', 'Preto', 'Vermelho', 'Preto'], # PADRAO WILLIAM
    ['Preto', 'Preto', 'Vermelho', 'Vermelho', 'Preto', 'Preto', 'Vermelho', 'Vermelho'], # PADRAO 2X2
    ['Vermelho', 'Vermelho', 'Preto', 'Preto', 'Vermelho', 'Vermelho', 'Preto', 'Preto'], # PADRAO 2X2
    ['Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho'], # PADRAO XADREZ
    ['Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto'], # PADRAO XADREZ
    ['Vermelho', 'Vermelho', 'Vermelho', 'Preto', 'Vermelho', 'Vermelho', 'Vermelho', 'Preto'], # PADRAO 3X1
    ['Preto', 'Preto', 'Preto', 'Vermelho', 'Preto', 'Preto', 'Preto', 'Vermelho'], # PADRAO 3X1
    ['Vermelho', 'Vermelho', 'Preto', 'Vermelho', 'Vermelho', 'Preto', 'Preto', 'Vermelho'], # PADRAO 2X1
    ['Preto', 'Preto', 'Vermelho', 'Preto', 'Preto', 'Vermelho', 'Vermelho', 'Preto'], # PADRAO 2X1
    ['Preto', 'Preto', 'Preto', 'Preto', 'Preto', 'Preto', 'Preto', 'Preto'], # PADRAO SURF
    ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho', 'Vermelho'], # PADRAO SURF
    ['Vermelho'], # PADRAO PEZAO
    ['Branco'] # PADRAO PEZAO
]

entredas = [
    'Preto',       # Entrada 1
    'Vermelho',    # Entrada 2
    'Preto',       # Entrada 3
    'Preto',       # Entrada 4
    'Preto',       # Entrada 5
    'Vermelho',    # Entrada 6
    'Preto',       # Entrada 7
    'Vermelho',    # Entrada 8
    'Vermelho',    # Entrada 9
    'Preto',       # Entrada 10
    'Preto',       # Entrada 11
    'Vermelho',    # Entrada 12
    'Preto',       # Entrada 13
    'Vermelho',    # Entrada 14
    'Preto'        # Entrada 15
    ]

# CONECAO COM A API BLAZE

def blazeAPI(): # RETORNA O CONTEUDO DO ARRAY
    url_api = 'https://blaze.com/api/roulette_games/recent'

    response = requests.get(url_api)

    if response.status_code != 200: # VERIFICANDO POSSIVEL ERRO DE COMUNICAÇÃO COM A API
        debug = True
        print(response.status_code)
        while debug: # LOOPA ATÉ OBTER O RESULTADO ESPERADO DA API
            if response.status_code != 200:
                print('corrigindo falha de resposta HTTPS')
                response = None
                response = requests.get(url_api)
                print(response.status_code)
            if response.status_code == 200:
                debug = False
            time.sleep(5)

    r = response.json()

    ray = []

    for x in range(len(r)):
        val = r[x]['color']
        if val == 1:
            val = 'Vermelho'

        if val == 2:
            val = 'Preto'

        if val == 0:
            val = 'Branco'
        ray.append(val)
    return ray

# ENVIAR MENSSAGENS

def enviarMenssagem(text):  # recebe um texto,
    url_base = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url_base)

# CCHECAR A COR ( evita repetir esse codigo)

def corCheck(z):# recebe decisao
    if z == 'Vermelho':
        z = '🔴'
    if z == 'Preto':
        z = '⚫'
    if z == 'Branco':
        z = '⚪️'
    return z

# TOMA A DECISAO SE O BOT ACERTOU OU NAO O PALPITE

def martinGale(decisao,g):  # recebe array, Palpite
    global acertos
    global erros
    giro = False
    # ATIVE CASO QUEIRA INFORMAR QUE O RESULTADO ESTA SENDO VERIFICADO
    # time.sleep(10)
    # text = '''🔍 VERIFICANDO RESULTADO ... !!!'''
    # enviarMenssagem(text)
    cont = 0
    while not giro:
        ray = blazeAPI()
        if ray2[:10] == ray[5:15]:
            for z in ray[:5]:
                cont = cont + 1
                if decisao == z:
                    text = f'''🟢 𝗦𝗜𝗡𝗔𝗟 𝗖𝗢𝗥𝗥𝗘𝗧𝗢 🟢\n\n🎯 Investimos no: {(g)}\n🔰 Resultado no = {([ cont ])} x Martingale\n'''
                    enviarMenssagem(text)
                    acertos += 1
                    giro = True
                    cont = 0
                    break
                if cont == 6:
                    text = f'''🔴 𝗦𝗜𝗡𝗔𝗟 𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗧𝗢 🔴\n\n🎯 Investimos no: {(g)}\n🔰 Erramos os = {([ cont ])} x Martingale\n'''
                    enviarMenssagem(text)
                    erros += 1
                    giro = True
                    cont = 0
                    break
                    
        time.sleep(2)

# METODOS DE APOSTA

def metodos(num):  # recebe array,    OBS: FUTURA ATT DEIXAR ESSA FUNCAO DINAMICA
    met = False
    if num != ray2:
        for i in range(len(jogadas)):
            x = len(jogadas[i])
            if num[:x] == jogadas[i]:
                cor = entredas[i]
                check = corCheck(cor)
                text = f'''🟢 𝗦𝗜𝗡𝗔𝗟 𝗖𝗢𝗡𝗙𝗜𝗥𝗠𝗔𝗗𝗢 🟢\n\n🎯Entrada:  {(check)} [ {(cor)} ]\n\n⚠️ 𝗔𝗹𝗲𝗿𝘁𝗮: \n\nEntre até o 6x Martingale\nDobre a aposta em cada Gale\nAo ganhar espera o proximo sinal !!'''
                enviarMenssagem(text)
                met = True
                time.sleep(3)
                martinGale(cor,check)
                break
    return met

# ENVIA O STATUS DE TEMPO EM TEMPO (FUTURO UPDATE)

def enviarStatus(): # RETORNA O TEXT COM INFORMAÇOES DE STATUS DE ACERTOS E ERROS
    text = f'''💥🟢 𝗦𝗜𝗡𝗔𝗟 𝗦𝗧𝗔𝗧𝗨𝗦 🟢💥\n\n🎯 𝗔𝗰𝗲𝗿𝘁𝗼𝘀: {([acertos])} \n\n⛔️ 𝗘𝗿𝗿𝗼𝘀: {([erros])}\n\n📌 𝗥𝗼𝗱𝗮𝗱𝗮𝘀: {([acertos + erros])}'''
    enviarMenssagem(text)

# MAIN ONDE REALIZA BUSCA AOS DADOS

while True:
    ray = blazeAPI()
    os.system('cls') or None
    print('## INFORMACOES DA API ##\n\n')
    print(ray)

    if ray2 == []:        
        ray2 = ray

    if not gale:
        met = metodos(ray)
        gale = met
    else:
        ray2 = []
        met = None
        loop += 1
        gale = False
        time.sleep(10)

    if loop > 10:
        enviarStatus()
        loop = 0
    time.sleep(5)
