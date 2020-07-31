import pyttsx3
# Initialize the converter 
converter = pyttsx3.init() 
  
 
converter.setProperty('rate', 150) 

converter.setProperty('volume', 1.0) 
  

converter.say("Hello there") 
converter.say("this is a simple program to convert text to speech") 
converter.save_to_file("This is a simple program to convert text to speech","style.mp3")
converter.say()
converter.runAndWait()