import speech_recognition as sr
mic = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Start Speaking ....")
        voice = mic.listen(source)
        text = mic.recognize_google(voice)
        print("You said this :",text)

except sr.UnknownValueError :
    print("I couldn't understand what you said. Please try again.")