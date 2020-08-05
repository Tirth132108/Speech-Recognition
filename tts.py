import pyttsx3
# Initialize the converter 
converter = pyttsx3.init(driverName='sapi5') 
  
 
converter.setProperty('rate', 150) 

converter.setProperty('volume', 1.0)
voices = converter.getProperty("voices")
converter.setProperty("voice",voices[1].id) 
  

# converter.say("Hello there") 
#converter.open("test.txt", "r").read().replace("\n", " ")
#converter.say("test.txt")
#converter.print("please wait...processing")
#converter.save_to_file("test.txt","style.mp3")

infile="test.txt"
f = open(infile, 'r')
theText = f.read()
f.close()
converter.say(theText)
converter.save_to_file(theText,"finale.mp3")
  

converter.runAndWait()

