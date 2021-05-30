# speak("I bear witness that there is no god other than allah and prophet mohammad is last messenger")
import datetime
import  pyttsx3
import sys
import speech_recognition as sr


def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows',
        'win64':'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]
# from espeak
os = get_platform()

if os =='linux':
    engine =pyttsx3.init('espeak')
elif os =='OS X':
    engine =pyttsx3.init('nsss')
elif os =='Windows':
    engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# for i in range(1,21):
print(voices[12].id)
engine.setProperty('voice',voices[12].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print("Trying to understand....")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("Say that agin please....")
        return "None"
if __name__ == '__main__':
    speak('hello world ')
     # for i in range(1,21):
     #    speak(i)
    while True:
        said = listener().lower()
        if said == 'none' or 'quit now' in said :
            speak("I am quit ing ")
            break
        elif'help'in said:
            speak("what do you need help in")
            if 'coding' in said or 'programing'in said or 'computer' in said or 'help one' in said or 'help 1' in said:
                speak("which labhuage")
                if 'python' in said or 'help two':
                    speak("Go to python.org or visit stackoverflow website")
                else:
                    continue
            else:
                continue

        elif'the time'in said:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"The time is {time}")


        # speak(said)
