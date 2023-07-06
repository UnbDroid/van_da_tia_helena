from pybricks.hubs import *
ev3 = EV3Brick()
ev3.speaker.set_speech_options('pt-br', "f1")


def beep(freq, duration=100):
    ev3.speaker.beep(freq, duration)


def talk(txt):
    ev3.speaker.say(txt)


def beep_success():
    talk('van da tia helena, melhor equipe')
    # speaker.play_file("mariowin.mp3") ###############


def sound_catch_15():
    beep(800, 500)
    beep(000, 500)
    beep(800, 500)


def sound_catch_10():
    beep(300, 500)


def success_15():
    talk('larguei um passageiro de 15 cm')


def success_10():
    talk('larguei um passageiro de 10 cm')
