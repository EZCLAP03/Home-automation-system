import webbrowser
import win32com.client as wincl
import os
import requests, json


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
        cmd = f'{app}.exe'
        os.system(cmd) 
        print(cmd)
        self.cmd = cmd
    
    def close(self):
        terminate(self.cmd)
    
    def lights(self):
        pass
    
    def weather(self):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = "Hyderabad"
        API_KEY = "Your API Key"
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']

            report = data['weather']
            return(f"{CITY:-^30}, Temperature: {temperature}, Humidity: {humidity} \
            , Pressure: {pressure}, Weather Report: {report[0]['description']} ")
        else:
            return "Error in the HTTP request"


        
        

        
    
        