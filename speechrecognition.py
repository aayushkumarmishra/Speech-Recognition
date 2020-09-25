import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listning....")
    r.pause_threshold = 1
    audio = r.listen(source)

    try:
        print("Recognising...") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        print("Network connection error,say again please") 
    


     
    
