//AUTHOR OF THIS PROJECT IS MANOJ
import pyttsx3                                             
import speech_recognition as sr                            
import wikipedia                                           
import webbrowser
import os                                                  
import random                                            
from googletrans import Translator                        
translator = Translator()
import datetime
from gtts import gTTS
import requests
import json                                             

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

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
        speak("I am Jinni, your personal voice assistant")
        speak(f"Its {day} morning ")
        speak(f" And ,the time is {stTime}")
        speak("How may i help you?")

    elif hour>=12 and hour<=16:
        speak("Good Afternoon Sir!")
        speak("I am Jinni,your personal voice assistant")
        speak(f"It's {day} afternoon")
        speak(f" And Sir,the time is {stTime}")
        speak("How may i help you?")

    else:
        speak("Good evening Sir!")
        speak("I am Jinni,your personal voice assistant")
        speak(f"It's {day} evening")
        speak(f" And,the time is {stTime}")
        speak("How may i help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query} \n")
    except Exception as e:
        print("say that again please...")
        return "None"
    return query

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

def trans():
    speak("please speak what do you want to translate, and i will translate it in your desired language")
    t = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        t.pause_threshold = 1  
        audio = t.listen(source)
    try:
        print("Recognising...")
        txt = t.recognize_google(audio, language='en-in')
        with sr.Microphone() as source:
            speak("In which language you want to translate")
            print("listening..")
            t.pause_threshold = 1  
            audio = t.listen(source)
            print("Recognising......")
            lang = t.recognize_google(audio, language='en-in')
            print(f"user want to translate: {txt} \n")
            print(f"Language chosen for translation {lang} ")
            speak("please wait working on translation..")
       
        if 'Hindi' == lang or 'hindi' == lang:
            translations = translator.translate(txt, dest='hi')            
        elif 'Urdu' == lang or 'urdu'== lang:
            translations = translator.translate(txt, dest='ur')
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
   
        else:
            speak("Try Again! either it is not available or there was some recognition issue ")
            
        speak("Translation is on your screen..")
        print(f"Translation language is {lang}")
        print(translations.text)

       
        tranres = pyttsx3.init('sapi5')
        voices = tranres.getProperty('voices')
        tranres.setProperty('voice', voices[1].id)
        tranres.say(translations.text)
        tranres.runAndWait()
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Results...')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'which language you can translate' in query:
            speak("I can translate in hindi,spanish,urdu,punjabi,italian,kannad,french,german,chinese,tamil,japanese,latin,russian"
                  "and many more")
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
            speak("Sir i was made a shaukeen coder")
        elif 'what is your age' in query:
            speak("I keep on update myself so i have no age")
        elif 'exit' in query:
            speak("Exiting the program ")
            exit()
        elif 'rap god'in query:
            speak("playing rap god")
            webbrowser.open("https://www.youtube.com/watch?v=XbGs_qK2PQA")
        elif 'garry sandhu' in query:
            speak("playing yeah baby..")
            webbrowser.open("https://www.youtube.com/watch?v=G7RW-KVDeEo")
        elif 'joke' in query:
            speak("Ohh! you want me to be funny ")
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
            #Add your music files path below
            music_dir =''              
            songs=os.listdir(music_dir)
            speak("playing music...")
            num=random.randint(0,10)
            os.startfile(os.path.join(music_dir, songs[num]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            speak("opening vs code")
            path=""
            os.startfile(path)
        elif 'notepad' in query:
            speak("opening notepad")
            npath=""
            os.startfile(npath)
        elif 'word' in query:
            speak("opening ms word")
            mpath = ""
            os.startfile(mpath)
        elif 'turbo' in query:
            speak("opening code blocks...")
            cpath = ""
            os.startfile(cpath)
        elif 'open instagram' in query:
            speak("opening instagram"
                  "sir please login you details there")
            webbrowser.open("https://www.instagram.com/")
        elif 'open facebook' in query:
            speak("opening facebook.."
                  "please login you details there")
            webbrowser.open("https://www.facebook.com/")
        elif 'news' or 'headlines'  in query:
            #Add your own API Key
              url = ""
              news=requests.get(url).text
              news_dict=json.loads(news)
              speak("please enter number of headlines you want to listen")
              headnumb=int(input("Enter here\t"))
              speak("Here are the top headlines")
          
              for i in range(0,headnumb):
                  print(i+1,news_dict['articles'][i]['title'])
                  speak(news_dict['articles'][i]['title'])
