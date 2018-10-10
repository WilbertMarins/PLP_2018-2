from MVC import BeatController
from MVC import DJView


BPM = 90  # valor padrão


# inicia a aplicação
def initialize():
    #inicializa

#liga
def on():
    print("Iniciando a sequência")  # imprime a mensagem
    BPM = 90
    BPM+=0
    # inicia sequencia

# desliga
def off():
    BPM = 0
    BPM+=0


# para sequencia

# altera o Bpm recebendo novo valor
def recebeBPM(bpm):
    BPM = bpm
    print("BPM",BPM)


# atualiza o modelo
def beatEvent():
    # atualiza em tela



