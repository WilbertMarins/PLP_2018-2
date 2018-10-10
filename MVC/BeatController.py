 #controla a execução do programa
def BeatController():
	#define modelo
	#instancia o modelo
	disableStopMenuItem()
	enableStartMenuItem()
	initialize()
	
#inicia e permite a parada, mas bloqueia a opção primária
def start():
	on()
	disableStartMenuItem()
	enableStopMenuItem()

#para e permite o inicio, mas bloqueia a opção primária
def stop():
	off()
	disableStopMenuItem()
	enableStartMenuItem()
    
#incrementa 1 ao bpm
def increaseBPM():
	#no modelo
        bpm += 1
	
#decrementa 1 ao bpm
def decreaseBPM():
	#no modelo
        bpm -= 1
   
 def alteraBPM(novo_bpm):
	bpm=novo_bpm
	
