# -*- coding: utf-8 -*-
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""			"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"																	   "			"																	  "
"        				   ASSISTENTE VIRTUAL   	     			   "			"		> Instruções de Código:										  "
"																	   "			"																	  "
"	> Versão: 1.0.0  (Beta)											   "			"			- Escrever as instruções pra quem for utilizar			  "
"																	   "			"																	  "
"	> Objetivos de Implementação:									   "			"																	  "
"																	   "			"																	  "
"		(*)Concluido	(-)Desenvolvendo							   "			"																	  "
"																	   "			"																	  "
"		* Pesquisa Wikipédia (Concluido)							   "			"																	  "
"		- Abrir Facebook											   "			"																	  "
"		- Abrir Twitter												   "			"																	  "
"		- Melhorar Conversação Chatbot								   "			"																	  "
"		- Arrumar Bugs nos códigos									   "			"																	  "
"		- Função ajudar a decidir									   "			"																	  "
"		- Ligar as X horas											   "			"																	  "
"		- Criar agenda e lembretes									   "			"																	  "
"		- Controlar eletronicos										   "			"																	  "
"		- Controlar luzes											   "			"																	  "
"		- Controlar janelas											   "			"																	  "
"		- Controlar alarme											   "			"																	  "
"		- Controlar trancas											   "			"																	  "
"		- Controlar Robo Limpeza									   "			"																	  "
"		- Realizar Calculos											   "			"																	  "
"		- Gerir finanças											   "			"																	  "
"		- Aux. controle de calorias									   "			"																	  "
"		- Ler página webbrowser										   "			"																	  "
"		- Abrir media player										   "			"																	  "
"		- Musica no youtube											   "			"																	  "
"		- Abrir aplicativos											   "			"																	  "
"		- Fechar aplicativos										   "			"																	  "
"		- Contar História / Piada									   "			"																	  "
"		- Tutor (Ensina a usar)										   "			"																	  "
"		- Buscar preço + barato (zoom)								   "			"																	  "
"		- Realizar conversão										   "			"																	  "
"		- Base de conhecimentos básica								   "			"																	  "
"		- Lista telefonica											   "			"																	  "
"		- Emergencia (Auto-Chamada)									   "			"																	  "
"		- Leitor de Textos											   "			"																	  "
"		- Feriados (Mes, proximo, tipo)								   "			"																	  "
"		- Conselhos (Ex.Levar guarda-chupa)							   "			"																	  "
"		- Detecção facial											   "			"																	  "
"		- Sugestao de comida										   "			"																	  "
"		- Controle de luminosidade									   "			"																	  "
"		- Modo economia de energia 									   "			"																	  "
"		- Tradutor													   "			"																	  "
"		- Lista de compras											   "			"																	  "
"		- Monitoramento inteligente (Pet)							   "			"																	  "
"		- Sugestao de filme											   "			"																	  "
"		- Despertador												   "			"																	  "
"		- Analise de gastos com Energia								   "			"																	  "
"		- Limitar tempo de eletronicos (Economia)					   "			"																	  "
"		- Analise de atividades fisicas								   "			"																	  "
"		- Entretenimento (Adivinhar quem você esta pensando)	 	   "			"																	  "
"		- Resolver problemas (Informatica)							   "			"																	  "
"																	   "			"																	  "
"																	   "			"		Autor: Gustavo Gino Scotton	 	-  	  Nasc.: 12/04/2018		  "
"																	   "			"																	  "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""			 """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from chatterbot import ChatBot 
import speech_recognition as Sr
import paho.mqtt.publish as publish
from playsound import playsound
import Weather
import cv2
from Email import Send_Email_Settings
import codecs
import pyttsx3
from datetime import datetime
import webbrowser
import random
import time
import os
import wikipedia

from googlesearch import search


#Keys (escrever tudo em minusculo sempre)

key_wikipedia = ['o que é', 'quem é', 'quem foi', 'definição', 'defina', 'me fale sobre']
key_google = ['pesquisar por', 'pesquise por'] 
key_futebol = ['meu time é','futebol buscar por']
key_desligar = ['sofia desligar']
key_ligar =['sofia ligar']
key_tempo =['previsão do tempo','hoje vai chover', 'previsão do tempo para hoje', 'qual a previsão do tempo para hoje']
key_desligar_min=['programar para desligar', 'programação para desligar']
key_ligar_min=['programar para ligar', 'programação para ligar']
key_noticias=['últimas notícias', 'abrir últimas notícias', 'notícias', 'abrir notícias']
key_atv_camera=['ativar câmera', 'câmera ativar', 'abrir câmera', 'câmera abrir']
key_bolsa_valores=['bolsa de valores', 'abrir bolsa de valores', 'como está a bolsa de valores', 'bolsa de valores abrir']
key_horoscopo=['horóscopo','horóscopo de hoje', 'abrir horóscopo', 'horóscopo abrir']
key_help=['me ajude','pode me ajudar','preciso da sua ajuda','help']
key_sofia=['quem é você','como é seu nome', 'quem você é','seu nome é', 'qual o seu nome', 'qual é seu nome']
key_dia=['que dia é hoje', 'qual o dia de hoje', 'que dia é', 'hoje é que dia', 'dia atual', 'dia de hoje']
key_hora=['que horas são','que hora é agora','me diga as horas', 'hora atual', 'hora de agora']
key_obrigado=['obrigado', 'obrigado sofia', 'muito obrigado', 'valeu']
key_biblia=['abrir bíblia online','bíblia online', 'ver bíblia online', 'bíblia online abrir']
key_ola=['olá sofia', 'oi sofia','hey sofia', 'ei sofia', 'bom dia sofia', 'boa tarde sofia', 'sofia']
key_adeus=['adeus sofia','até logo', 'adeus', 'tchau', 'até breve','até mais' ]
key_devocional=['abir devocional', 'devocional diário', 'abrir devocional de hoje', 'devocional de hoje']
key_comida=['pedir comida','peça comida','quero comida','quero comer']
key_moeda=['cotação do','qual a cotação do']
key_ditar=['digite para mim', 'escreva para mim', 'escreva o que eu falar', 'anote o que eu falar' ,'escreva por mim', 'digite por mim', 'escreva o que eu disser' ,'digite o que eu falar', 'digite o que eu disser']
key_rota=['definir rota', 'fazer rota', 'realizar rota', 'preciso de uma rota']
key_email=['enviar e-mail','escrever e-mail', 'mandar e-mail', 'quero enviar um e-mail', 'quero mandar um e-mail', 'quero escrever um e-mail']






wikipedia.set_lang('pt')
bot = ChatBot('Sophia') 
cont = 0
speaker = pyttsx3.init()

def speak(text): 
	speaker.say(text)
	speaker.runAndWait()
	
def get_answer(text):  # Busca no wikipedia
	text = text.lower()
	result = None 
	results= None 
	
	if text is not None:
		for key in key_wikipedia:
			if text.startswith(key):
				result = text.replace(key,'')

	if result !=  None:		
		results = wikipedia.search(result)		
	
	if result == None:
		result = None		
	else:	
		result = wikipedia.summary(results[0],sentences=2)
		
	return result
	
def search_web(text): #Busca no Google
	result = None
	text = text.lower()
	if text is not None:
		for key in key_google:
			if text.startswith(key):
				result = text.replace(key,'')
				
		if result != None:	
			webbrowser.open("www.google.com.br/search?q="+result, autoraise=True)
			return 'Pesquisando por '+result
	return result	
	
	
def search_fut(text): #Busca GloboEsporte (Futebol)
	result = None
	text = text.lower()	
	if text is not None:
		for key in key_futebol:
			if text.startswith(key):
				result = text.replace(key,'')
				
		if result != None:	
			webbrowser.open("http://globoesporte.globo.com/futebol/times/"+result,autoraise=True)	
			return 'Pesquisando por '+result
	return result	
	

def myfor(keywords,recog_voice): #Meu For
	result = None	
	voice = recog_voice.lower()
	if voice is not None:
		for key in keywords:
			if voice == key:
				result = 'True'
				break				
	return result		
	
print("""


	    ___                _      _        
	   / __|  ___   _ __  | |_   (_)  __ _ 
	   \__ \ / _ \ | '_ \ | ' \  | | / _` |
	   |___/ \___/ | .__/ |_||_| |_| \__,_|
		       |_|                                   
			   
			
                 Sua assistente pessoal!
				 
			""")



print("""
	+--------------------------------------+
	|         Selecione uma Opção          |
	+--------------------------------------+

	+--------------------------------------+
	| [1] Conversar com a Sophia           |
	+--------------------------------------+
	| [2] Obter ajuda                      |
	+--------------------------------------+
	| [3] Treinar Chatbot                  |
	+--------------------------------------+
            """)

try:
	Option = int(input("	Digite sua opção: "))
	
	while Option == 1 or Option == 2 or Option == 3:
		if Option == 1:
			Inst_Recog = Sr.Recognizer()

			Mic_Name = "Microphone (Realtek High Defini"  		#"Microfone (Realtek High Definit" <= Nome do Microfone Padrão do Windows...
			Mic_List = Sr.Microphone.list_microphone_names()
	
			print('Eu já iniciei meu sistema e eu estou pronta para começar! ')			
			#pronta = 'Eu já iniciei meu sistema e eu estou pronta para começar'
			#speak(pronta)

			for m, microphone_name in enumerate(Mic_List):
				if microphone_name == Mic_Name:
					device_id = m

			with Sr.Microphone(device_index = device_id, chunk_size = 1024) as source:
				Inst_Recog.adjust_for_ambient_noise(source)

				while True:				
					print(">Ouvindo... ")					
					try:
						Hearing = Inst_Recog.listen(source)
						Recog_Google_Voice = Inst_Recog.recognize_google(Hearing, language='pt-br')

						print("Você disse: ",Recog_Google_Voice)

					
						if myfor(key_ligar,Recog_Google_Voice) == 'True':
							response = 'Entendido, Ligado!'				
							print('Sophia: ', response)
							speak(response) 
							publish.single("cmnd/sonoff/POWER", "ON", hostname="iot.eclipse.org")
							
							
						
						elif myfor(key_desligar,Recog_Google_Voice) == 'True':
							response = 'Entendido, estou desligando! '				
							print('Sophia: ', response)
							speak(response) 
							publish.single("cmnd/sonoff/POWER", "OFF", hostname="iot.eclipse.org")	

							

						elif myfor(key_tempo,Recog_Google_Voice) == 'True':
							response = 'Para qual cidade você deseja a previsão? '				
							print('Sophia: ', response)
							speak(response) 
							#TA COM AIDS ---- RESOLVER
							Prediction_City = Inst_Recog.recognize_google(Hearing, language='pt-br')
							print('Sophia: ', Prediction_City)
							PrevisionTemp = os.system("python Weather.py " + Prediction_City)
							speak(PrevisionTemp) 	


							
						elif myfor(key_ligar_min,Recog_Google_Voice) == 'True':
							voice = 'Daqui a quantos minutos você deseja ligar?' 				
							print('Sophia: ', voice)
							speak(voice) 
							Count_Time_On = float(input("Minutos: "))	
							time.sleep(Count_Time_On*60)				#mudar pra horario definido
							publish.single("cmnd/sonoff/POWER", "ON", hostname="iot.eclipse.org")
							response ='Ligado!'  
							
							
						
						elif myfor(key_desligar_min,Recog_Google_Voice) == 'True':
							voice = 'Daqui a quantos minutos você deseja desligar? '				
							print('Sophia: ', voice)
							speak(voice) 
							Count_Time_Off = float(input("Minutos: "))
							time.sleep(Count_Time_Off*60)	#mudar pra horario definido
							publish.single("cmnd/sonoff/POWER", "OFF", hostname="iot.eclipse.org")
							response ='Desligado!'
						
						else:
							try:
								voice_respost = Recog_Google_Voice

								if myfor(key_noticias,Recog_Google_Voice) == 'True':
									response = 'Abrindo as últimas notícias de hoje!'
									webbrowser.open("http://g1.globo.com/ultimas-noticias.html", autoraise=True)
									
								elif myfor(key_atv_camera,Recog_Google_Voice) == 'True':
									response = 'Iniciando captura de vídeo, pressione a letra Q para fechar.'				

									Capture = cv2.VideoCapture(0)

									while(True):
										Ret, Frame = Capture.read()
										cv2.imshow('Sophia - Video Stream', Frame)
										if cv2.waitKey(1) & 0xFF == ord('q'):
											break

									Capture.release()
									cv2.destroyAllWindows()	

								elif myfor(key_bolsa_valores,Recog_Google_Voice) == 'True':
									response = 'Abrindo as últimas notícias de hoje!'
									webbrowser.open("http://www.infomoney.com.br/mercados/acoes-e-indices", autoraise=True)

								elif myfor(key_horoscopo,Recog_Google_Voice) == 'True':
									response = 'Abrindo lista de horóscopo'
									webbrowser.open("http://www.wemystic.com.br/horoscopo/", autoraise=True)


								elif myfor(key_help,Recog_Google_Voice) == 'True':
									response = 'Sim, no que você precisa de ajuda?'

								elif myfor(key_sofia,Recog_Google_Voice) == 'True':
									response = 'Meu nome é Sofia e eu sou sua assistente virtual!'

								elif myfor(key_dia,Recog_Google_Voice) == 'True':
									now = datetime.now()
									months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
									response = 'Hoje é dia '+ str(now.day) + ' de '+ months[now.month -1]+' de '+str(now.year)	

								elif myfor(key_hora,Recog_Google_Voice) == 'True':
									now = datetime.now()
									response = 'Agora são '+ str(now.hour) +' horas e '+ str(now.minute) +' minutos.'

								elif myfor(key_obrigado,Recog_Google_Voice) == 'True':
									response = 'Não tem de que.'

								elif myfor(key_ola,Recog_Google_Voice) == 'True':
									response = 'Olá, em que posso te ajudar?'

								elif myfor(key_biblia,Recog_Google_Voice) == 'True':
									response = 'Abrindo bíblia online ...'
									Bible_List = ["https://www.bibliaonline.com.br", "https://www.bibliaon.com"]
									webbrowser.open(random.choice(Bible_List), autoraise=True)

								elif myfor(key_adeus,Recog_Google_Voice) == 'True':
									response = 'Adeus, até mais!'

								elif myfor(key_devocional,Recog_Google_Voice) == 'True':
									response = 'Abrindo o devocional de hoje...'
									Devotional_List = ["http://www.devocionaldiario.com.br", "http://www.maxlucado.com.br/devocional-diario/","http://ultimato.com.br/sites/devocional-diaria/", "http://www.devocionaisdiarios.com"]
									webbrowser.open(random.choice(Devotional_List), autoraise=True)
									
								elif myfor(key_comida,Recog_Google_Voice) == 'True':
									response = 'Abrindo Ifood...'
									webbrowser.open('https://www.ifood.com.br/', autoraise=True)
									
								elif myfor(key_moeda,Recog_Google_Voice) == 'True':
									voice = 'Qual moeda você deseja cotar? '				
									print('Sophia: ', voice)
									speak(voice)
									Key_Words_Coin = Inst_Recog.recognize_google(Hearing, language='pt-br')
									
									if (Key_Words_Coin == "Dólar Americano" or Key_Words_Coin=="Dólar"):
										response = 'Abrindo o valor do dólar Americano... '				
										webbrowser.open("https://www.melhorcambio.com/dolar-hoje", autoraise=True)
			 
									elif Key_Words_Coin == "Dólar Canadense":
										response = 'Abrindo o valor do dólar Canadense... '				
										webbrowser.open("https://www.melhorcambio.com/dolar-canadense-hoje", autoraise=True)

									elif Key_Words_Coin == "Dólar Australiano":
										response = 'Abrindo o valor do dólar Australiano... '				
										webbrowser.open("https://www.melhorcambio.com/dolar-australiano-hoje", autoraise=True)

									elif Key_Words_Coin == "Euro":
										response = 'Abrindo o valor do Euro... '				
										webbrowser.open("https://www.melhorcambio.com/euro-hoje", autoraise=True)

									elif Key_Words_Coin == "Libra":
										response = 'Abrindo o valor da Libra... '				
										webbrowser.open("https://www.melhorcambio.com/libra-hoje", autoraise=True)
										
									else:
										webbrowser.open("https://economia.uol.com.br/cotacoes/cambio/", autoraise=True)
								
								elif myfor(key_ditar,Recog_Google_Voice) == 'True':
									voice = 'Pode falar, eu estou te ouvindo e irei digitar para você! '
									print('Sophia: ', voice)
									speak(voice)
									
									Hearing_To_Read = Inst_Recog.listen(source)
									Recog_Google_To_Read = Inst_Recog.recognize_google(Hearing_To_Read, language='pt')
									
									print("Você disse: ", Recog_Google_To_Read)
									
									Recog_Google_Reading = open('Reconhecimento_Escrito.txt', 'w')
									Recog_Google_Reading.write(Recog_Google_To_Read)
									Recog_Google_Reading.close()
									
									response = 'Salvei seu texto no arquivo "Reconhecimento_Escrito.txt" ! '	

								elif myfor(key_rota,Recog_Google_Voice) == 'True':
									voice = 'Onde você está no momento? '				
									print('Sophia: ', voice)
									speak(voice) 				

									Key_Words_Starting_Point = Inst_Recog.recognize_google(Hearing, language='pt-br')
									print('Sophia: ', Key_Words_Starting_Point,' definido como local de partida. Qual o seu local de destino?')
									speak(Key_Words_Starting_Point,' definido como local de partida. Qual o seu local de destino?') 							
									
									Key_Words_Point_Of_Arrival = Inst_Recog.recognize_google(Hearing, language='pt-br')
									print('Sophia: ', Key_Words_Point_Of_Arrival,' definido como local de destino.')
									speak(Key_Words_Point_Of_Arrival,' definido como local de destino') 
									
									response = 'Abrindo rota de viagem'									
									webbrowser.open("www.google.com.br/maps/dir/%s/%s" % (Key_Words_Starting_Point, Key_Words_Point_Of_Arrival))
									
								elif myfor(key_email,Recog_Google_Voice) == 'True':
									while True:
										try:
											Send_From = 'email-sofia@outlook.com' ##Dados do email
											Password  = 'senha123'

											voice = 'Para quem você deseja enviar?!'		#FAZER LISTA DE CONTATOS		 
											print('Sophia: ', voice)
											speak(voice)
											Send_To = Inst_Recog.recognize_google(Hearing, language='pt-br')
											
											voice = 'Qual o assunto?'								
											print('Sophia: ', voice)   			
											speak(voice)
											Hearing = Inst_Recog.listen(source)
											Subject = Inst_Recog.recognize_google(Hearing, language='pt-br')

											voice = 'O que deseja escrever no e-mail?'				
											print('Sophia: ', voice)
											speak(voice)
											Hearing = Inst_Recog.listen(source)
											Compose_Email = Inst_Recog.recognize_google(Hearing, language='pt-br')
											
											voice = 'Seu email será enviado para: '+Send_To+' \n O assunto é: '+Subject+' \n E a mensagem escrita:\n'+Compose_Email+'. \n \n Deseja enviar este email?'
											print(voice)
											speak(voice)
											
											Hearing = Inst_Recog.listen(source)
											respost = (Inst_Recog.recognize_google(Hearing, language='pt-br')).lower()
											if (respost == 'sim' or respost == 'sim enviar' or respost == 'enviar' or respost == 'envie' ):									
												Send_Email_Settings(Send_From, Password, Send_To, Subject, Compose_Email) #ENVIAR 
												response='Seu e-mail foi enviado!'
												break
										except:
											voice = 'Tem certeza que deseja cancelar? Reponda "Sim, quero cancelar" '
											print(voice)
											speak(voice)
											Hearing = Inst_Recog.listen(source)
											respost = (Inst_Recog.recognize_google(Hearing, language='pt-br')).lower()
											if (respost == 'sim' or respost == 'sim quero cancelar' or respost=='quero cancelar' or respost=='cancelar'):
												response = 'E-mail cancelado!'
												break
											else:
												continue																	

								else: 
									response = get_answer(voice_respost) 
									
									if response == None:
										response = search_web(voice_respost)
										
										if response == None:
											response = search_fut(voice_respost) # Necessário ainda remover os acentos das palavras
											
											if response == None:
												response = bot.get_response(voice_respost)	
												

								print('Sophia: ', response)
								speak(response)		
							
							except:
								print('\n Ocorreu um erro, fale novamente!')
								mensage = 'Ocorreu um erro, fale novamente!'
								speak(mensage)	

					except: 
						print('')
						
		elif Option == 2:

			print("""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                        SEJA BEM-VINDO AO MENU DE AJUDA!                                        |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                                                                |
|SOPHIA É UMA ASSISTENTE VIRTUAL, COM ELA VOCÊ PODE FAZER ACIONAMENTOS DE ELETRODOMÉSTICOS, LÂMPADAS             |
|ENTRE OUTROS OBJETOS ELÉTRICOS QUE SE ENCONTRAM DENTRO DE CASA APENAS POR COMANDOS DE VOZ. SUA FAIXA DE OPERAÇÃO|
|DE TENSÃO FUNCIONA ENTRE 90-250V AC ENTRE 50/60Hz, COM CORRENTE MÁXIMA DE 10A.SOPHIA AINDA É CAPAZ DE RECONHECER|
|OUTROS COMANDOS PRÉ-CONFIGURADOS QUE ADICIONAM FUNCIONALIDADES À ELA COMO VOCÊ PODE VER Á SEGUIR:               |
|                                                                                                                |
|=> COMANDOS CONFIGURADOS:                                                                                       |
|   => "OLÁ SOPHIA"                                 |	=> "SOPHIA BOLSA DE VALORES"                             |
|   => "GOSTARIA DE SABER COMO VOCÊ ESTÁ"           |	=> "SOPHIA PESQUISAR"                                    |
|   => "EU ESTOU BEM OBRIGADO"                      |	=> "SOPHIA FUTEBOL"                                      |
|   => "QUEM É VOCÊ"                                |   => "SOPHIA LIGAR AGORA"                                  |
|   => "VOCÊ É MUITO INTELIGENTE"                   |   => "SOPHIA DESLIGAR AGORA"                               |
|   => "OBRIGADO SOPHIA"                            |	=> "SOPHIA PROGRAMAR TEMPO PARA LIGAR"                   |
|   => "ATÉ LOGO SOPHIA"                            |	=> "SOPHIA PROGRAMAR TEMPO PARA DESLIGAR"                |
|   => "SOPHIA PREVISÃO DO TEMPO"                   |	=> "SOPHIA RECONHECIMENTO ESCRITO"                       |
|   => "SOPHIA QUE HORAS SÃO"                       |   => "SOPHIA NOTÍCIAS"                                     |
|   => "SOPHIA QUE DIA É HOJE"                      |   => "SOPHIA ENVIAR EMAIL"                                 |
|   => "SOPHIA DEFINIR ROTA"                        |   => "SOPHIA CRIPTOGRAFIA"                                 |
|   => "SOPHIA COTAÇÃO DE MOEDAS"                   |   => "SOPHIA DESCRIPTOGRAFIA"                              |
|      => "DOLAR AMERICANO"                         |   => "SOPHIA DEVOCIONAL DIÁRIO"                            |
|      => "DOLAR CANADENSE"                         |   => "SOPHIA BÍBLIA ONLINE"                                |
|      => "DOLAR AUSTRALIANO"                       |   => "SOPHIA ATIVAR CÂMERA"                                |
|      => "EURO"                                    |   => "SOPHIA PEDIR COMIDA"                                 |
|      => "LIBRA"                                   |   => "FUTURA AGENDA E LEMBRETES" (BREVE)                   |
|      => "VAZIO"                                   |   => "FUTURA CALCULADORA PARA ENGENHARIA" (BREVE)          |
|                                                                                                                |
|=> CONEXÃO DO HARDWARE:                                                                                         |
|   => A CONEXÃO DO HARDWARE SONOFF É MUITO SIMPLES, BASTA COLOCAR A ENTRADA (input) EM QUALQUER TOMADA          |
|      (QUE FUNCIONE ENTRE A FAIXA DE OPERAÇÃO DETERMINADA) E A SAÍDA (output) NO OBJETO ELÉTRICO QUE VOCÊ       |
|      DESEJA LIGAR.                                                                                             |
|                                                                                                                |
|=> CONEXÃO DO WIFI:                                                                                             |
|   => PARA REALIZAR A CONEXÃO DO SONOFF COM SUA REDE WIFI, BASTA BAIXAR O APLICATIVO "ESP8266 SmartConfig"      |
|      NA PLAYSTORE OU APPLE STORE, COLOCAR A SENHA DE SUA REDE INTERNA NA CAIXA DE OPÇÃO "password" QUE IRÁ     |
|      APARECER EM SEU SMARTPHONE E SIMULTANEAMENTE PRESSIONAR O BOTÃO ACIMA DO SONOFF DE FORMA BREVE 3 VEZES.   |
|                                                                                                                |
|      OBS:                                                                                                      |
|      => PARA VERIFICAR SE SEU SONOFF ESTÁ CONECTADO À SUA REDE, VOCÊ PODE BAIXAR O APLICATIVO "FING" NA        |
|         PLAYSOTRE OU APPLE STORE, CONECTAR COM SEU WIFI E REALIZAR UMA VARREDURA DE SUA REDE INTERNA. SE O     |
|         SONOFF ESTIVER CONECTADO COM SUA REDE, ALÉM DOS OUTROS DISPOSITIVOS CONECTADOS AO SEU WIFI, IRÁ        |
|         APARECER ALGO PARECIDO COM O NOME "Light  Espressif" E O ENDEREÇO IP QUE O SONOFF ASSUMIU, ALGO COMO   |
|         "192.168.25.4" OU "10.0.0.115" DEPENDENDO DO SEU PROVEDOR DE INTERNET.                                 |
|                                                                                                                |
|=> CONEXÃO DO MICROFONE:                                                                                        |
|   => PARA UTILIZAR O MICROFONE PADRÃO OU EXTERNO É NECESSÁRIO EXECUTAR O PROGRAMA "Microfone.py". QUANDO       |
|      EXECUTADO, O PROGRAMA IRÁ MOSTRAR UMA LISTA DE ENTRADAS E SAÍDAS DE SOM DISPONÍVEIS EM SEU COMPUTADOR.    |
|      PARA UTILIZAR O MICROFONE DESEJADO, BASTA COPIAR O NOME DO MICROFONE MOSTRADO NA LISTA E COLOCAR NA       |
|      VARIÁVEL DO PROGRAMA PRINCIPAL "Mic_Name". O PROJETO PADRÃO UTILIZA O SMARTPHONE COMO MICROFONE PARA O    |
|      RECONHECIMENTO DE VOZ. PARA ISSO, É UTILIZADO O PROGRAMA "WO Mic". PARA UTILIZAR DESSA FORMA, BASTA BAIXAR|
|      O "WO Mic" NA PLAYSTORE OU APPLESTORE E INSTALAR. TAMBÉM DEVE SER BAIXADO O "WO Mic" EM SEU COMPUTADOR,   |
|      PESQUISE NO GOOGLE E BAIXE O "WO Mic" E O "WO Mic Client". PARA FAZER A CONEXÃO, ABRA O APLICATIVO EM SEU |
|      SMARTPHONE, VÁ EM CONFIGURAÇÕES, SELECIONE O TIPO DE TRANSPORTE DE DADOS (NESSE CASO, WIFI), DEIXE AS     |
|      PORTAS PADRÕES E PRESSIONE "START". LOGO EM SEGUIDA IRÁ APARECER UM NÚMERO DE IP. ABRA O "WO Mic Client"  |
|      DO SEU COMPUTADOR, VÁ EM OPÇÕES, PORTS, E CONFIGURE AS PORTAS EM CONFORMIDADE COM AS PORTAS DO APLICATIVO |
|      DO SMARTPHONE. DEPOIS VÁ EM CONEXÃO, CONECTAR, SELECIONE O MODO DE RECEPÇÃO WIFI E COLOQUE O ENDEREÇO DE  |
|      IP QUE APARECEU EM SEU SMARTPHONE. CASO TUDO ESTEJA CORRETO, SEU COMPUTADOR JÁ ESTARÁ RECEBENDO AUDIOS EM |
|      TEMPO REAL E RECONHECENDO SEU SMARTPHONE COMO MICROFONE.                                                  |
|                                                                                                                |
|=> PARA CONVERSAR COM SOPHIA, SELECIONE A OPÇÃO 1.                                                               |
|                                                                                                                |
|=> PARA OBTER AJUDA, SELECIONE A OPÇÃO 2.                                                                       |
|                                                                  1                                             |
|=> PARA TREINAR A REDE, SELECIONE A OPÇÃO 3.                                                                    |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                        SEJA BEM-VINDO AO MENU DE AJUDA!                                        |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")
			break

		elif Option == 3:
			
			print("""	----------------------------------------
			
			
			
   _____               _                           _       
  |_   _|  _ _   ___  (_)  _ _    __ _   _ _    __| |  ___ 
    | |   | '_| / -_) | | | ' \  / _` | | ' \  / _` | / _ \
  
    |_|   |_|   \___| |_| |_||_| \__,_| |_||_| \__,_| \___/
	   
	Que tal tomar um café enquanto treinamos a rede?!
		Isso pode demorar alguns minutos...

			
	+--------------------------------------+
	|         Selecione uma Opção          |
	+--------------------------------------+

	+--------------------------------------+
	| [1] Treinar Rede .TXT                |
	+--------------------------------------+
	| [2] Treinar Rede Corpus              |
	+--------------------------------------+
	| [3] Treinar Rede Films		       |
	+--------------------------------------+
						""")
			res = input('	Digite sua opção: ')

			if res=='1':
				# Treinamento do .TXT
				from chatterbot.trainers import ListTrainer

				bot.set_trainer(ListTrainer) 

				for arq in os.listdir('chats'): 
					chats = open('chats/' + arq, 'r', encoding='utf-8').readlines() 
					bot.train(chats)		
				continue						
				
			elif res=='2':
				# Treinamento do Corpus			
				bot = ChatBot('Sophia', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
				bot.train('corpus.data.portuguese')
				continue
				
			elif res=='3':
				# Treinamento de Filmes
				from chatterbot.trainers import ListTrainer

				bot.set_trainer(ListTrainer) 

				for arq in os.listdir('films'): 
					films = open('films/' + arq, 'r', encoding='utf-8').readlines() 
					bot.train(films)		
				
	
			else:
				response = 'Você não selecionou nenhuma rede para treinar, portanto, nenhum treinamento foi executado.'				
				print(response)
				speak(response)	
				break
				exit()
				
				
			response = 'O treinamento foi um sucesso!'				
			print(response)
			speak(response)	
			
			
				
				
	while Option not in range(1,4):
		print("\n[!] O valor digitado não consta no menu.")
		break
		#Option = int(input("\nOpt -->  "))
		#if Option in range(1,4):
		#	break

except KeyboardInterrupt:
    print('\n[!] Saindo...')
except ValueError:
    print('\n[!] Insira um valor correto.')
#except Range_Option_Menu_Error():
#	print('\n[!] Insira um valor de opção correta.')
#	Option = int(input("Opt -->  "))
#except TimeoutError:
#	print('\n[!] Continue falando!')
#	Hearing = Inst_Recog.listen(source)