import webbrowser
import win32com.client as wincl
import os


def convert(lst): 
    return ([i for item in lst for i in item.split()]) 

class UserInput:
    def convert_input(self, args):
        if len(args) == None:
            response = 'What would you like me to do sir'
            return response
        elif args[0] == 'search':
            if len(args) == 1:
                response = 'what do you want to search'
                return response
            else:
                query = args[1]
                response = (f'Ok searching {args[1]}.')
                converter = UserInput()
                converter.search(query)
        elif args[0] == 'open':
            con = UserInput()
            con.open(args[1])

    def search(self, param_query):
        open_query = f"https://www.google.com/search?q={param_query}"
        webbrowser.open_new_tab(open_query)

    def open(self, app):
        app = app.capitalize()
        cmd = f'{app}'
        os.system(cmd) 


        
        

        
    
        