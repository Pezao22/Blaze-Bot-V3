# Blaze-Bot-V3

Um bot de palpite para a plataforma de apostas Blaze
Esse bot foi criado apenas para fins de estudo e aprendizado
não revenda esse produto

COMO FUNCIONAR

O bot pega informaçoes atraves da API da blaze faz uma verificação
com os palpites pre cadastrados nele, caso algum padrao seja encontrado
automaticamente esse palpite é enviado paga o chat do TELEGRAM escolhido pelo usuario.

FUNÇOES DO BOT

Verifica e compara os padroes de cores utilizando API blaze
Caso encontre um padrao informa atravez do telegram
verifica se o palpite foi certeiro ou não
verifica em até 6 martingale se foi encontrado o palpite
apos 10 palpites informa o status de erros e acertos do bot

![image](https://user-images.githubusercontent.com/114784744/197395429-75aede1a-b8af-449a-b020-a5441561694f.png)


COMO USAR

Instale as bibliotecas abaixo

requests
pyTelegramBotAPI

ex: pip install requests

Feito isso vamos adicionar nosso token do bot e o chat_id
crie um bot no telegram usando BOT FATHER pegue o token e coloque abaixo
Feito isso pegue o ID do chat onde deseja que o bot mande os Palpites.

![image](https://user-images.githubusercontent.com/114784744/197395496-09c8824e-5968-4589-8b22-36f7468e50cf.png)

o bot já esta quase todo pronto precisamos apenas configurar os palpites (padroes de cores)
que nosso bot vai verificar e comparar, fazemos isso na opção abaixo

![image](https://user-images.githubusercontent.com/114784744/197395517-fac8822e-b7d1-4344-b37a-7f586cc3c6e8.png)

Cada linha trata-se de um palpite, voce escolhe as cores e a quantidade de cores que cada combinação terá

