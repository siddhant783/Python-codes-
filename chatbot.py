import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer =sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    print(c)
  

if __name__ == "__main__":
    speak("Initializing chatbot")
    #listen for the  word "chatty"
    while True:
        r = sr.Recognizer()
        
        print("rocognizing")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="Venom"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("chatty active.. ")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command) 
        except Exception as e:
            print("Error; {0}".format(e))
 

