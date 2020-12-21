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
    server.login('your email Id', 'Password of your email ID')
    email = EmailMessage()
    email['From'] = 'Name Of Sender'
    email['To'] = reciver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    
  #In place of multiple'x' write the correct email to whom you want to send mail 
email_list = {
              'james': 'xxxxxxxxx@gmail.com',
              'me': 'xxxxxxxxxx@gmail.com',
              'ball': 'xxxxxx@gmail.com'
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
    talk('Hey lazy. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()


