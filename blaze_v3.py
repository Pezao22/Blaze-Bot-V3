import requests
import telebot
import time
import os

TOKEN = 'coloque aqui o token' # BOT TOKEN

bot = telebot.TeleBot(TOKEN)

chat_id = 'coloque aqui o id do chat' # CHAT ID DO CANAL ONDE DESEJA ENVIAR MSG

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
    ['Vermelho']
]

# CONECAO COM A API BLAZE

def blazeAPI(): # RETORNA O CONTEUDO DO ARRAY
    url_api = 'https://blaze.com/api/roulette_games/recent'

    response = requests.get(url_api)

    if response.status_code != 200: # VERIFICANDO POSSIVEL ERRO DE COMUNICAÇÃO COM A API
        debug = False
        while not debug: # LOOPA ATÉ OBTER O RESULTADO ESPERADO DA API
            if response.status_code == 200:
                debug = True
            print('corrigindo falha de resposta HTTPS')
            response = None
            time.sleep(5)
            response = requests.get(url_api)
            
            

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

def martinGale(decisao):  # recebe array, Palpite
    global acertos
    global erros
    giro = False

    time.sleep(10)
    # ATIVE CASO QUEIRA INFORMAR QUE O RESULTADO ESTA SENDO VERIFICADO

    # text = '''🔍 VERIFICANDO RESULTADO ... !!!'''
    # enviarMenssagem(text)
    cont = 0
    while not giro:
        ray = blazeAPI()
        if ray2[0:10] == ray[6:16]:
            for z in ray[:6]:
                cont = cont + 1
                if decisao == z:
                    g = corCheck(decisao)
                    text = f'''🟢 𝗣𝗮𝗹𝗽𝗶𝘁𝗲 𝗖𝗼𝗿𝗿𝗲𝘁𝗼 🟢\n\n🎯 Investimos no: {(g)}\n🔰 Resultado = {([cont])} x Martingale\n'''
                    enviarMenssagem(text)
                    acertos += 1
                    giro = True
                    cont = 0
                    break
                if cont == 6:
                    g = corCheck(decisao)
                    text = f'''🔴 𝗣𝗮𝗹𝗽𝗶𝘁𝗲 Incorreto 🔴\n\n🎯 Investimos no: {(g)}\n🔰 Erramos os = {([cont])} x Martingale\n'''
                    enviarMenssagem(text)
                    erros += 1
                    giro = True
                    cont = 0
                    break
                    
        time.sleep(5)

# METODOS DE APOSTA

def metodos(num):  # recebe array,    OBS: FUTURA ATT DEIXAR ESSA FUNCAO DINAMICA
    met = False

    if num[1:9] == jogadas[0] or num[2:10] == jogadas[0]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: ⚫ [ Preto ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.Wiliam)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Preto')
    elif num[1:7] == jogadas[1] or num[2:8] == jogadas[1]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: 🔴 [ Vermelho ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.Wiliam)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Vermelho')
    elif num[1:9] == jogadas[2] or num[2:10] == jogadas[2]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: 🔴 [ Vermelho ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.Wiliam)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Preto')
    elif num[1:9] == jogadas[3] or num[2:10] == jogadas[3]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: ⚫ [ Preto ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Preto')
    elif num[1:9] == jogadas[4] or num[2:10] == jogadas[4]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: ⚫ [ Preto ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Preto')
    elif num[1:9] == jogadas[5] or num[2:10] == jogadas[5]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: 🔴 [ Vermelhor ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Vermelho')
    elif num[1:9] == jogadas[6] or num[2:10] == jogadas[6]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: ⚫ [ Preto ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Preto')
    elif num[1:9] == jogadas[7] or num[2:10] == jogadas[7]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: 🔴 [ Vermelhor ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Vermelho')
    elif num[1:9] == jogadas[8] or num[2:10] == jogadas[8]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: 🔴 [ Vermelhor ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Vermelho')
    elif num[1:9] == jogadas[9] or num[2:10] == jogadas[9]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: ⚫ [ Preto ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Preto')
    elif num[1:9] == jogadas[10] or num[2:10] == jogadas[10]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: ⚫ [ Preto ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Preto')
    elif num[1:9] == jogadas[11] or num[2:10] == jogadas[11]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: 🔴 [ Vermelhor ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Vermelho')
    elif num[1:9] == jogadas[12] or num[2:10] == jogadas[12]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: ⚫ [ Preto ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.WEB)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Preto')
    elif num[1:2] == jogadas[13] or num[2:3] == jogadas[13]:

        text = '''🟢 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 🟢\n\n🎯Entrada: 🔴 [ Vermelho ]\n\nSUGESTÕES: \n\n💭 6x Martingale (Metodo.teste nao siga)\n'''
        enviarMenssagem(text)
        met = True
        time.sleep(5)
        martinGale('Vermelho')
    return met

# ENVIA O STATUS DE TEMPO EM TEMPO (FUTURO UPDATE)

def enviarStatus(): # RETORNA O TEXT COM INFORMAÇOES DE STATUS DE ACERTOS E ERROS
    text = f'''💥🟢 𝗣𝗮𝗹𝗽𝗶𝘁𝗲 𝗦𝘁𝗮𝘁𝘂𝘀 🟢💥\n\n🎯 Acertos: {([acertos])} \n\n⛔️ Erros: {([erros])}'''
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
        loop += 1
        gale = met
    else:
        ray2 = []
        met = None
        gale = False
        time.sleep(120)

    if loop > 10:
        enviarStatus()
        loop = 0
    time.sleep(5)
