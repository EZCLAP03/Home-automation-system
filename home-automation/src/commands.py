import webbrowser
import win32com.client as wincl
import os
import requests, json
import calendar
import imaplib
import email
from email.header import decode_header


class UserInput:
    def convert_input(self, args):
        if len(args) == None:
            response = 'What would you like me to do human'
            return response
        elif args[0] == 'search':
            if len(args) == 1:
                response = 'what do you want to search'
                return response
            else:
                query = args[1]
                response = (f'Ok searching {args[1]}.')
                search(query)
        elif args[0] == 'open':
            open(args[1])
        elif args[0] == 'exit':
            exit()
        elif args[0] == 'inbox':
            inbox_invoker()


def search(param_query):
    open_query = f"https://www.google.com/search?q={param_query}"
    webbrowser.open_new_tab(open_query)

def open(app):
    cmd = f'{app}.exe'
    os.system(cmd) 
    print(cmd)
    self.cmd = cmd
    
def close():
    terminate(self.cmd)
    
def lights():
    pass
    
def calendar(self, date):
    date = date.split('/')
    event = calendar.TextCalendar(calendar)

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

def convert(lst): 
    return ([i for item in lst for i in item.split()]) 

def inbox_invoker():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login("ezclapisalive@gmail.com", "harisai143")

    status, messages = imap.select("INBOX")
    N = 3
    messages = int(messages[0])

    for i in range(messages, messages-N, -1):
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
            from_ = msg.get("From")
            print("Subject:", subject)
            print("From:", from_)
        
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in \
                    content_disposition:
                        print(body)
                    elif "attachment" in content_disposition:
                        filename = part.get_filename()
                        if filename:
                            if not os.path.isdir(subject):
                                os.mkdir(subject)
                            filepath = os.path.join(subject, filename)
                            open(filepath, "wb").write(part.get_payload(decode=True))
            else:
                content_type = msg.get_content_type()
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    print(body)
            print("="*100)
    imap.close()
    imap.logout()


        
        

        
    
        