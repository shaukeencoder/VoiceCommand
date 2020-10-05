# project 01 its the end of course
# making the "Atrene" project automations of tasks just in 5yrs
# install pyttsx3 module
import pyttsx3                                             #for voice of atrene
import speech_recognition as sr                            #to recogonise what i speak
import wikipedia                                           #this is just wikipedia and its results
import webbrowser
import os                                                  #to open files through their path
import random
import smtplib                                             #for this we have to enable less secured in gmail
from googletrans import Translator                         #lets see will it work or not
translator = Translator()
import datetime
from gtts import gTTS
import requests
import json                                                #for telling news
# from covid import Covid
# covid = Covid()
# covid.get_data()
# active = covid.get_total_active_cases()
# confirmed = covid.get_total_confirmed_cases()
# recovered = covid.get_total_recovered()
# deaths = covid.get_total_deaths()
# covid = Covid(source="worldometers")


#Here is the atrene voice  begins
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices[1].id)

#Here is the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour =int(datetime.datetime.now().hour)
    d=datetime.datetime.now()
    day=d.strftime("%A")
    stTime = datetime.datetime.now().strftime("%H:%M:%S")

    if hour>=0 and hour<=12:
        speak(" Good Morning Sir!")
        speak("I am Atrene, your personal voice assistant")
        speak(f"Its {day} morning ")
        speak(f" And ,the time is {stTime}")
        speak("How may i help you?")

    elif hour>=12 and hour<=16:
        speak("Good Afternoon Sir!")
        speak("I am Atrene,your personal voice assistant")
        speak(f"It's {day} afternoon")
        speak(f" And Sir,the time is {stTime}")
        speak("How may i help you?")

    else:
        speak("Good evening Sir!")
        speak("I am Atrene,your personal voice assistant")
        speak(f"It's {day} evening")
        speak(f" And,the time is {stTime}")
        speak("How may i help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1 #see its documnetation pree ctrl+click
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query} \n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

    # Mail Function
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('manojsheokand111@gmail.com','password')
    server.sendmail('youramil@gmail.com',to,content)
    server.close()

#Here is somethinf to light the mood
def joke():
    joknum=random.randint(0,1)
    if joknum==0:
        speak("this is the funniest joke. okay hold your seat")
        speak("Your life is a joke,Boom!")
    elif joknum==1:
        speak("This one is a PJ what we call to an obedient table  ")
        speak("Timetable Ha ha ha")
    else:
        exit()

def coronacases():
    speak("Here the total cases in the world")

def trans():

    speak("please speak what do you want to translate, and i will translate it in your desired language")
    t = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        t.pause_threshold = 1  # see its documentation press ctrl+click
        audio = t.listen(source)
    try:

        print("Recognising...")
        txt = t.recognize_google(audio, language='en-in')
        # print(f"user want to translate: {txt} \n")

        with sr.Microphone() as source:
            speak("In which language you want to translate")
            print("listening..")
            t.pause_threshold = 1  # see its documentation press ctrl+click
            audio = t.listen(source)
            print("Recognising......")
            lang = t.recognize_google(audio, language='en-in')
            print(f"user want to translate: {txt} \n")
            print(f"Language chosen for translation {lang} ")
            speak("please wait working on translation..")
        # if "hindi"==lang or "Hindi" == lang:
        #         print(lang)
        #         translations = translator.translate(txt, dest='hi')
        # elif "urdu"==lang or "Urdu" == lang:
        #         print(lang)
        #         translations = translator.translate(txt, dest='ur')
        # elif "Polish"==lang or "polish"== lang:
        #         print(lang)
        #         translations = translator.translate(txt, dest='pl')
        # else:
        #         speak("Didnt  recognise")
        #



        if 'Hindi' == lang or 'hindi' == lang:
            translations = translator.translate(txt, dest='hi')
            # print(lang)
            # trans_result = translations.text
            # speak("translation is on your screen")
            # print(trans_result)
            # tran_ans = t.recognize_google(audio, language='hi')
            # speak(trans_result)
        elif 'Urdu' == lang or 'urdu'== lang:
            # print(lang)
            translations = translator.translate(txt, dest='ur')
        elif 'Hebrew' == lang or 'hebrew' == lang:
            translations = translator.translate(txt, dest='he')
        elif 'Filipino' == lang or 'filipino' == lang:
            translations = translator.translate(txt, dest='fil')
        elif 'Zulu' == lang or 'zulu' == lang:
            translations = translator.translate(txt, dest='zu')
        elif 'Yiddish' == lang or 'yiddish' == lang:
            translations = translator.translate(txt, dest='yi')
        elif 'Ukrainian' == lang or 'ukrainian' == lang:
            translations = translator.translate(txt, dest='uk')
        elif 'Telugu' == lang or 'telugu' == lang:
            translations = translator.translate(txt, dest='te')
        elif 'Tamil' == lang or 'tamil' == lang:
            translations = translator.translate(txt, dest='ta')
        elif 'Thai' == lang or 'thai' == lang:
            translations = translator.translate(txt, dest='th')
        elif 'Turkish' == lang or 'turkish' == lang:
            translations = translator.translate(txt, dest='tr')
        elif 'Vietnamese' == lang or 'vietnamese' == lang:
            translations = translator.translate(txt, dest='vi')
        elif 'Spanish' == lang or 'spanish' == lang:
            translations = translator.translate(txt, dest='es')
        elif 'Somali' == lang or 'somali' == lang:
            translations = translator.translate(txt, dest='so')
        elif 'Sindhi' == lang or 'sindhi' == lang:
            translations = translator.translate(txt, dest='sd')
        elif 'Swedish' == lang or 'swedish' == lang:
            translations = translator.translate(txt, dest='sv')
        elif 'Russian' == lang or 'russian' == lang:
            translations = translator.translate(txt, dest='ru')
        elif 'Punjabi' == lang or 'punjabi' == lang:
            translations = translator.translate(txt, dest='pa')
        elif 'Romanian' == lang or 'romanian' == lang:
            translations = translator.translate(txt, dest='ro')
        elif 'Portuguese' == lang or 'portuguese' == lang:
            translations = translator.translate(txt, dest='pt')
        elif 'Polish' == lang or 'polish' == lang:
            translations = translator.translate(txt, dest='pl')
        elif 'Persian' == lang or 'persian' == lang:
            translations = translator.translate(txt, dest='fa')
        elif 'Nepali' == lang or 'nepali' == lang:
            translations = translator.translate(txt, dest='ne')
        elif 'Arabic' == lang or 'arabic' == lang:
            translations = translator.translate(txt, dest='ar')
        elif 'Albanian' == lang or 'albanian' == lang:
            translations = translator.translate(txt, dest='sq')
        elif 'Armenian' == lang or 'armenian' == lang:
            translations = translator.translate(txt, dest='hy')
        elif 'Belarusian' == lang or 'belarusian' == lang:
            translations = translator.translate(txt, dest='be')
        elif 'Bengali' == lang or 'bengali' == lang:
            translations = translator.translate(txt, dest='bn')
        elif 'Bulgarian' == lang or 'bulgarian' == lang:
            translations = translator.translate(txt, dest='bg')
        elif 'Chinese' == lang or 'chinese' == lang:
            translations = translator.translate(txt, dest='zh-cn')
        elif 'Traditional Chinese' == lang or 'traditional chinese' == lang:
            translations = translator.translate(txt, dest='zh-tw')
        elif 'Croatian' == lang or 'croatian' == lang:
            translations = translator.translate(txt, dest='hr')
        elif 'Czech'== lang or 'czech' == lang:
            translations = translator.translate(txt, dest='cs')
        elif 'Danish' == lang or 'danish' == lang:
            translations = translator.translate(txt, dest='da')
        elif 'Dutch' == lang or 'dutch' == lang:
            translations = translator.translate(txt, dest='nl')
        elif 'Finnish' == lang or 'finnish' == lang:
            translations = translator.translate(txt, dest='fi')
        elif 'Filipino' == lang or 'filipino' == lang:
            translations = translator.translate(txt, dest='tl')
        elif 'French' == lang or 'french' == lang:
            translations = translator.translate(txt, dest='fr')
        elif 'Georgian' == lang or 'georgian' == lang:
            translations = translator.translate(txt, dest='ka')
        elif 'German' == lang or 'german' == lang:
            translations = translator.translate(txt, dest='de')
        elif 'Greek' == lang or 'greek' == lang:
            translations = translator.translate(txt, dest='el')
        elif 'Gujarati' == lang or 'gujarati' == lang:
            translations = translator.translate(txt, dest='gu')
        elif 'Hungarian' == lang or 'hungarian' == lang:
            translations = translator.translate(txt, dest='hu')
        elif 'Indonesian' == lang or 'indonesian' == lang:
            translations = translator.translate(txt, dest='id')
        elif 'Irish' == lang or 'irish' == lang:
            translations = translator.translate(txt, dest='ga')
        elif 'Italian' == lang or 'italian' == lang:
            translations = translator.translate(txt, dest='it')
        elif 'Japanese' == lang or 'japanese' == lang:
            translations = translator.translate(txt, dest='ja')
        elif 'Kannada' == lang or 'kannada' == lang:
            translations = translator.translate(txt, dest='kn')
        elif 'Korean' == lang or 'korean' == lang:
            translations = translator.translate(txt, dest='ko')
        elif 'Kurdish' == lang or 'kurdish' == lang:
            translations = translator.translate(txt, dest='ku')
        elif 'Latin' == lang or 'latin' == lang:
            translations = translator.translate(txt, dest='la')
        elif 'Latvian' == lang or 'latvian' == lang:
            translations = translator.translate(txt, dest='lv')
        elif 'Lithuanian' == lang or 'lithuanian' == lang:
            translations = translator.translate(txt, dest='lt')
        elif 'Malayalam' == lang or 'malayalam' == lang:
            translations = translator.translate(txt, dest='ml')
        elif 'Marathi' == lang or 'marathi' == lang:
            translations = translator.translate(txt, dest='mr')
        elif 'Mongolian' == lang or 'mongolian' == lang:
            translations = translator.translate(txt, dest='mn')
        elif 'Norwegian' == lang or 'norwegian' == lang:
            translations = translator.translate(txt, dest='no')

        else:
            speak("Try Again! either it is not available or you did not speak right ")
            # translations = translator.translate(txt, dest='hi')
            # speak(" Sorry I did not find your language so i converted it in hindi")
            # translations = translator.translate(txt, dest='hi')
            # for translation in translations:
            #
            #     print(translation.text)
            #     speak(translation.text)
            # return speak(translation.text)
            # print(translations)
        speak("Translation is on your screen..")
        print(f"Translation language is {lang}")
        print(translations.text)

        # reslt=translations.text
        tranres = pyttsx3.init('sapi5')
        voices = tranres.getProperty('voices')
        # print(voices[1].id)
        tranres.setProperty('voice', voices[1].id)
        tranres.say(translations.text)
        tranres.runAndWait()

        # language='hi'
        # myobj=gTTS(text=reslt,lang=language,slow=False)
        # myobj.save("tr.mp3")
        # os.system("mpg321 tr.mp3")
        # speak(translations.text)
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    # return txt
#     it takes microphone input from the user
if __name__ == "__main__":
    wishme()
    while True:
        #logic for executing the tasks
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Results...')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'which language you can translate' in query:
            print("I can translate in hindi,spanish,urdu,punjabi,italian,kannad,french,german,chinese,korean,marathi,tamil,bengali,malayalam,japanese,latin,russian,arabic,persian"
                  "greek,turkish,romanian and many more")
            speak("I can translate in hindi,spanish,urdu,punjabi,italian,kannad,french,german,chinese,korean,marathi,tamil,bengali,malayalam,japanese,latin,russian,arabic,persian"
                  "greek,turkish,romanian and many more")
        elif 'translate' in query:
            speak("taking you to the translation section..")
            trans()
        elif 'who are you' in query:
            speak("I am a personal voice assistant who will help you to make your life easy")
        elif 'do you know hindi' in query:
            speak("Sir! mujhe thodi thodi hindi aata hai")
        elif 'what you can do' in query:
            speak("I can speak,recognize,search wikipedia results,open google for you,youtube,websites like code chef ,geeksforgeeks,github,can play music"
                  "open notepad and the most recent feature i can do translation more than 30 languages ")
        elif 'your birthplace' in query:
            speak("Sir i was developed in a room by a programmer who is a kunjean, his  name is Manoj 2 3 ")
        elif 'what is your age' in query:
            speak("I keep on update myself so i have no age")
        elif 'quit' in query:
            speak("Quitting the program ")
            exit()
        elif 'rap god'in query:
            speak("playing rap god")
            webbrowser.open("https://www.youtube.com/watch?v=XbGs_qK2PQA")
        elif 'garry sandhu' in query:
            speak("playing yeah baby..")
            webbrowser.open("https://www.youtube.com/watch?v=G7RW-KVDeEo")
        elif 'joke' in query:
            speak("Ohh! you want me to be funny ")
            speak("Okay! let me tell you joke")
            joke()
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com/")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://github.com/")
        elif 'open geeksforgeeks' in query:
            speak("opening geeksforgeeks")
            webbrowser.open("https://www.geeksforgeeks.org/")
        elif 'open codechef' in query:
            speak("opening codechef")
            webbrowser.open("https://www.codechef.com/")
        elif 'play music' in query:
            music_dir ='F:\\Music'
            songs=os.listdir(music_dir)
            speak("playing music...")
            # print(songs)
            num=random.randint(0,10)
            os.startfile(os.path.join(music_dir, songs[num]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            speak("opening vs code")
            path="F:\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'notepad' in query:
            speak("opening notepad")
            npath="C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
            os.startfile(npath)
        elif 'word' in query:
            speak("opening ms word")
            mpath = ""
            os.startfile(mpath)
        elif 'turbo' in query:
            speak("opening code blocks...")
            cpath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(cpath)
        elif 'open instagram' in query:
            speak("opening instagram"
                  "sir please login you details there")
            webbrowser.open("https://www.instagram.com/")
        elif 'open facebook' in query:
            speak("opening facebook.."
                  "please login you details there")
            webbrowser.open("https://www.facebook.com/")
        elif 'news'  in query:
              url = "http://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=a85299c00e2e424ea630b7b3b591e50b"
              news=requests.get(url).text
              news_dict=json.loads(news)
              speak("please enter number of headlines you want to listen")
              headnumb=int(input("Enter here\t"))
              speak("Here are the top headlines")
            #   print(news_dict["articles"])
            #   arts=news_dict["articles"]
              for i in range(0,headnumb):
                  print(i+1,news_dict['articles'][i]['title'])
                  speak(news_dict['articles'][i]['title'])
                #   speak("next news")
        elif 'headline' in query:
              url = "http://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=a85299c00e2e424ea630b7b3b591e50b"
              news=requests.get(url).text
              news_dict=json.loads(news)
              speak("please enter number of headlines you want to listen")
              headnumb=int(input("Enter here\t"))
              speak("Here are the top headlines")
            #   print(news_dict["articles"])
            #   arts=news_dict["articles"]
              for i in range(0,headnumb):
                  print(i+1,news_dict['articles'][i]['title'])
                  speak(news_dict['articles'][i]['title'])
                #   speak("next news")
        elif 'headlines'  in query:
              url = "http://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=a85299c00e2e424ea630b7b3b591e50b"
              news=requests.get(url).text
              news_dict=json.loads(news)
              speak("please enter number of headlines you want to listen")
              headnumb=int(input("Enter here\t"))
              speak("Here are the top headlines")
            #   print(news_dict["articles"])
            #   arts=news_dict["articles"]
              for i in range(0,headnumb):
                  print(i+1,news_dict['articles'][i]['title'])
                  speak(news_dict['articles'][i]['title'])
                #   speak("next news")
        elif 'radha soami shabad' in query:
            speak("playing shabad")
            webbrowser.open("https://www.youtube.com/watch?v=ijP4Lb_egEU")

        elif 'email to mk' in query:
            try:
                speak("what should i write sir?")
                content=takecommand()
                to="guidingefforts111@gmail.com"
                sendemail(to,content)
                speak("Email sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry soemthing went wrong, I am unable to send it")





    # speak("Yo")






