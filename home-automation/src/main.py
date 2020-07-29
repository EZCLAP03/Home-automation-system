import comms
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
            if text.startswith('hello'):
                handler = 0
            else:
                handler = 1
            self.handler = handler
    def event_handler(self):
        if self.handler == 0:
            print('works till here')
            args = self.text.split('hello ')
            
            print(args)
    def end_program(self):
        if self.text.startswith('exit'):
            exit()

run = True
while True:
    p = Event_listeners()
    p.end_program()
    p.event_handler()


            




