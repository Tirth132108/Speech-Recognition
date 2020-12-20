import speech_recognition as sr
import pyaudio
import io
import pandas as pd
 
def main():
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
 
 
        # recognize speech using google
 
        try:
            print("You have said \n" + r.recognize_google(audio))
            converted = r.recognize_google(audio)
            print("Audio Recorded Successfully \n ")
 
 
        except Exception as e:
            print("Error :  " + str(e))
 
 
 
 
        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
        
        
        from translate import Translator
        translator = Translator(to_lang='Hindi')
        translation = translator.translate(r.recognize_google(audio,language="hi"))

        
        with io.open("spike.txt", "w", encoding="utf-8") as f:
            f.write(translation)

        read_file = pd.read_csv(r'spike.txt', delimiter=" ")
        read_file.to_csv(r'spike.csv', index=None)

        

        df1 = pd.read_csv("spike.csv")  # text file which is convert to csv file
        df2 = pd.read_csv("hindi.csv")  # main value of dict file
        result = ""
        for el in df1:
            if el in df2:
                result += (el) + '\n'
        x = (result)
        print(x)

main()