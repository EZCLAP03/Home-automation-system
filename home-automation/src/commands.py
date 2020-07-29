import speech_recognition as sr
import commands
import webbrowser
import win32com.client as wincl

def convert(lst): 
    return ([i for item in lst for i in item.split()]) 

class UserInput:
    def convert_input(self, args):
        if args[0] == 'search':
            if args[1] == None:
                response = 'what do you want to search'
                return response
            else:
                query = args[1]
                response = (f'Ok searching {args[1]}.')
                converter = UserInput()
                converter.search(query)

    def search(self, param_query):
        open_query = f"https://www.google.com/search?q={param_query}"
        webbrowser.open_new_tab(open_query)
        
        

        
    
        