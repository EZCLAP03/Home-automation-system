import speech_recognition as sr
import commands
import webbrowser
import win32com.client as wincl

class UserInput:
    def __init__(self, recognizer, source, text_output):
        source = sr.Microphone()
        recognizer = sr.Recognizer()
        audio = recognizer.listen(source)
        text_output = audio.recognize_google(audio)

        self.source = source
        self.recognizer = recognizer
        self.text_output = text_output
    
    def search(self, param_query):
        open_query = f"https://www.google.com/search?q={param_query}&rlz=1C1APWK_enIN766IN766&oq=yo+&aqs=chrome..69i57j0j69i59l2j69i60l4.1394j0j7&sourceid=chrome&ie=UTF-8"
        webbrowser.open_new_tab(open_query)
        
        

        
    
        