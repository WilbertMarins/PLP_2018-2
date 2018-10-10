
from MVC import DJView
from MVC import BeatModel

# controla a execução do programa
def BeatController():
    # define modelo
    # instancia o modelo
    disableStopMenuItem()
    enableStartMenuItem()
    initialize()


# inicia e permite a parada, mas bloqueia a opção primária
def start():
    on()
    disableStartMenuItem()
    enableStopMenuItem()


# para e permite o inicio, mas bloqueia a opção primária
def stop():
    off()
    disableStopMenuItem()
    enableStartMenuItem()


# incrementa 1 ao bpm
def increaseBPM():
    # no modelo
    BPM += 1
    print("BPM",BPM)


# decrementa 1 ao bpm
def decreaseBPM():
    # no modelo
    BPM -= 1
    print("BPM", BPM)


def alteraBPM(novo_bpm):
    BPM = novo_bpm
    print("BPM:",BPM)