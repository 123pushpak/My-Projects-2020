import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine =pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def get_info():
 try:
    with sr.Microphone() as source:              # making microphone as a source
        print('Listening...')
        voice = listener.listen(source)          # listner will listen from the microphone
        info = listener.recognize_google(voice)  # listner will recognize your voice using Google regonizition API
        print(info)                              # prints what you are saying
        return info.lower()
 except:
     pass

def send_email(reciver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  #starting transport layer security
    server.login('goswamipushpak645@gmail.com', 'Pushpak645@')
    email = EmailMessage()
    email['From'] = 'Pushpak Goswami'
    email['To'] = reciver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    #server.sendmail('goswamipushpak645@gmail.com', 'pushpakgoswami645@gmail.com', 'Hi man,'
                                                                           #'How are you what do you have for me')
email_list = {
              'a': 'aryanakul0526@gmail.com',
              'pink': 'pushpakgoswami645@gmail.com',
              'ball': 'digambargoswami2015@gmail.com'
              }
def get_email_info():
    talk('To whom you want to send E-mail')
    name = get_info()
    reciver = email_list[name]
    print(reciver)
    talk('What is the subject of E-mail')
    subject = get_info()
    talk('Tell me the text in the mail')
    message = get_info()
    send_email(reciver, subject, message)
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()


