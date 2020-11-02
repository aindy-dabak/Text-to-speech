



#import the pyttsx3 module
import pyttsx3

#initialise the module
engine = pyttsx3.init()

#open the text file and read into a variable
file = open("Test.txt", "r")
myText = file.read().replace("/n", " ")

#Convert to speech----Use Variable in order to save to mp3---
output = engine.say(myText)



'''
                   To set voices
voices = engine.getProperty('voices')
engine.setProperty(voices, voices[1].id)
'''



engine.runAndWait()

#Close the File
file.close()

#Save to mp3
#engine.save_to_file(output, "output.mp3", name = None)