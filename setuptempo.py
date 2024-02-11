from PyQt5 import QtWidgets, uic
import requests
from PyQt5.QtCore import Qt

# Carregando o arquivo .ui
app = QtWidgets.QApplication([])
tela_principal = uic.loadUi('telaprincipal.ui')
tela_cidade = uic.loadUi('telacidade.ui')

lista_cidades = ['apuiarés', 'tokio', 'bangkok', 'cingapura', 'madrid', 'frankfurt', 'paris', 'hong kong', 'istambul']

# Definindo a função para exibir a tela_cidade
def mostrar_dados(cidade):

    # Usando API OpenWeatherMap
    api_key = '4673b70bc51873a632faaf2574937911'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br'
    requisitar = requests.get(link)
    requisitar_dic = requisitar.json()
    umidade = f'{requisitar_dic["main"]["humidity"]}%'
    veto_vel = f'{int(requisitar_dic["wind"]["speed"] * 3.6)}Km/h'
    clima = f'{requisitar_dic["weather"][0]["description"]}'
    temperatura = f'{(requisitar_dic["main"]["temp"] - 273.15):.1f}°C'

    # Verificando se a cidade foi encontrada na API
    if requisitar_dic['cod'] == 200:
        # Configurando o alinhamento centralizado para o label_5 da tela_cidade
        tela_cidade.label_5.setAlignment(Qt.AlignLeft)
        # Exibindo o texto no label_5 da tela_cidade
        tela_cidade.label_5.setText(cidade)
        # Configurando o alinhamento centralizado para o label_8 da tela_cidade
        tela_cidade.label_8.setAlignment(Qt.AlignCenter)
        # Exibindo o texto no label_8 da tela_cidade
        tela_cidade.label_8.setText(clima)
        # Configurando o alinhamento centralizado para o label_14 da tela_cidade
        tela_cidade.label_14.setAlignment(Qt.AlignCenter)
        # Exibindo o texto no label_14 da tela_cidade
        tela_cidade.label_14.setText(str(veto_vel))
        #Configurando o alinhamento centralizado para o label_11 da tela_cidade
        tela_cidade.label_11.setAlignment(Qt.AlignCenter)
        #Exibindo o testo no label_11 da tela_cidade
        tela_cidade.label_11.setText(str(umidade))
        #Configurando o alinhamento centralizado para o label_7 da tela_cidade
        tela_cidade.label_7.setAlignment(Qt.AlignCenter)
        #Exibindo a temperatura
        tela_cidade.label_7.setText(str(temperatura))
        # Exibindo o emoji de localização no label_4 da tela_cidade
        emoji_localizacao = "\U0001F310"
        tela_cidade.label_4.setText(emoji_localizacao)
        # Exibindo o emoji de localização no label_12 da tela_cidade
        emoji_umidade = "\U0001F4A7"
        tela_cidade.label_12.setText(emoji_umidade)
        # Exibindo o emoji de localização no label_13 da tela_cidade
        emoji_vento = "\U0001F32C"
        tela_cidade.label_13.setText(emoji_vento)

        tela_cidade.show()
    else:
        # Caso a cidade não seja encontrada, exibir uma mensagem de erro
        QtWidgets.QMessageBox.critical(tela_principal, 'Erro', 'Cidade não encontrada.')

def btn_apuiares():
    cidade = lista_cidades[0].capitalize()
    mostrar_dados(cidade)
def btn_tokio():
    cidade = lista_cidades[1].capitalize()
    mostrar_dados(cidade)
def btn_bangkok():
    cidade = lista_cidades[2].capitalize()
    mostrar_dados(cidade)
def btn_cingapura():
    cidade = lista_cidades[3].capitalize()
    mostrar_dados(cidade)
def btn_madrid():
    cidade = lista_cidades[4].capitalize()
    mostrar_dados(cidade)
def btn_frankfurt():
    cidade = lista_cidades[5].capitalize()
    mostrar_dados(cidade)
def btn_paris():
    cidade = lista_cidades[6].capitalize()
    mostrar_dados(cidade)
def btn_hongkong():
    cidade = lista_cidades[7].capitalize()
    mostrar_dados(cidade)
def btn_istambul():
    cidade = lista_cidades[8].capitalize()
    mostrar_dados(cidade)

def pesquisar1():
    # Obtendo o texto do textEdit da tela_principal
    cidade = tela_principal.textEdit.toPlainText().capitalize()
    mostrar_dados(cidade)
def pesquisar2():
    # Obtendo o texto do textEdit da tela_principal
    cidade = tela_cidade.textEdit.toPlainText().capitalize()
    mostrar_dados(cidade)

# Conectando o sinal de clique do botão a função exibir_tela_cidade
tela_principal.pushButton.clicked.connect(pesquisar1)
tela_cidade.pushButton.clicked.connect(pesquisar2)
tela_principal.pushButton_2.clicked.connect(btn_apuiares)
tela_principal.pushButton_3.clicked.connect(btn_tokio)
tela_principal.pushButton_4.clicked.connect(btn_cingapura)
tela_principal.pushButton_5.clicked.connect(btn_bangkok)
tela_principal.pushButton_6.clicked.connect(btn_frankfurt)
tela_principal.pushButton_7.clicked.connect(btn_madrid)
tela_principal.pushButton_8.clicked.connect(btn_paris)
tela_principal.pushButton_9.clicked.connect(btn_hongkong)
tela_principal.pushButton_10.clicked.connect(btn_istambul)

# Exibindo a janela
tela_principal.show()
app.exec()

