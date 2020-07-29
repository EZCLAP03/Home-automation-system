import speech_recognition as sr
import webbrowser
import win32com.client as wincl

class Event_listeners:
    def __init__(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("started")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said: {}".format(text))
                print(type(text))
                self.text = text
            except:
                print("Unrecognized")

    def event_listener(self):
        caller = ['chika', 'bonny', 'jarvis', 'friday']
        for elem in caller:
            if self.text.startswith(elem):
                listen = 0
                print('listener is 0')
                return listen
            else:
                listen = 1
                return listen

    def event_handler(self):
        l = Event_listeners()
        listener = l.event_listener()
        if listener == 0:
            args = self.text.split(listener)
            
            print(args)
    def end_program(self):
        if self.text.startswith('exit'):
            exit()

run = True
while True:
    p = Event_listeners()
    p.end_program()
    p.event_handler()


            




