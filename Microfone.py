import speech_recognition as SR

mic_list = SR.Microphone.list_microphone_names()
print("""


	-----------------------------------------------------
	|           Lista de Dispositivos de som:           |
	-----------------------------------------------------
	[!] Você deve selecionar o nome exato do Microfone. 
	       Exemplo:   "Microphone (Realtek High Defini"
	
		""")
for m in mic_list:
	print ('	> ',m)
	
print("""

	-----------------------------------------------------
	|                    Intruções:                     |
	-----------------------------------------------------
	
	1) Navegue até o arquivo "Main.py"
	
	2) Cole o nome do dispositivo de microfone na linha 219:
		Mic_Name = "Aqui vai o nome do microfone"
		
	3) Execute o arquivo "Main.py"


	
		Desenvolvido por: Gustavo Gino Scotton
		   Engenharia da Computação - UFSC

		""")	
