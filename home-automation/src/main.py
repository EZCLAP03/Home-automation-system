import speech_recognition as sr
import win32com.client as wincl
import commands as cm

class Event_listeners:
    def __init__(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("started")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                text = text.lower()
                print("You said: {}".format(text))
                self.text = text
                unrecognized = False
            except:
                unrecognized = True
        self.unrecognized = unrecognized

    def event_listener(self):
        if self.unrecognized == False:
            if self.text.startswith('jarvis'):
                listen = 0
            else:
                listen = 1
            self.listen = listen


    def event_handler(self):
        if self.listen == 0:
            args = self.text.split('jarvis')
            output = cm.convert(args)
            comms = cm.UserInput()
            comms.convert_input(output)
        else:
            return 1

    def end_program(self):
        if self.listen == 0:
            if self.text.startswith('exit'):
                exit()

run = True
while True:
    p = Event_listeners()
    p.event_listener()
    p.event_handler()
    p.end_program()


            




