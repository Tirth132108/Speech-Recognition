
import csv
import pandas as pd
import pyaudio
import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

with sr.AudioFile('english.wav') as source:
    print("Say Something.....")
    audio = r.listen(source)
    print("recognizing......")
try:
    from translate import Translator
    translator = Translator(to_lang='English')
    translation = translator.translate(r.recognize_google(audio))
    file = open('spike.txt', 'w')
    file.write(translation)
    file.close()

    read_file = pd.read_csv (r'spike.txt',delimiter=" ")
    read_file.to_csv (r'spike.csv', index=None)
    

    import pandas as pd
    df1 = pd.read_csv("spike.csv") #text file which is convert to csv file
    df2 = pd.read_csv("df2.csv") #main value of dict file
    result = ""
    for el in df1:
        if el in df2:
            result += (el)+'\n'
    x = (result)
    print(x)
        

    print("You said: " + translation)
except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
