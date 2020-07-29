import speech_recognition as sr
import commands
import webbrowser
import win32com.client as wincl

def convert(lst): 
    return ([i for item in lst for i in item.split()]) 

class UserInput:
    def __init__(self, recognizer, source, text_output):
        source = sr.Microphone()
        recognizer = sr.Recognizer()
        audio = recognizer.listen(source)
        text_output = audio.recognize_google(audio)

        self.source = source
        self.recognizer = recognizer
        self.text_output = text_output
    
    def convert_input(self, list = args):
        if args[0] == 'search':
            query = args[1]
            coverter = UserInput()
            converter.search(query)
    def search(self, param_query):
        open_query = f"https://www.google.com/search?q={param_query}"
        webbrowser.open_new_tab(open_query)
        
        

        
    
        