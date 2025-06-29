# import pyttsx3
# import speech_recognition as sr
# import wikipedia
# import webbrowser
# import os

# # init pyttsx
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")

# engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print("User said:" + query + "\n")
#     except Exception as e:
#         print(e)
#         speak("I didnt understand")
#         return "None"
#     return query


# if __name__ == '__main__':

#     speak("Amigo assistance activated ")
#     speak("How can i help you")
#     while True:
#         query = take_command().lower()
#         if 'wikipedia' in query:
#             speak("Searching Wikipedia ...")
#             query = query.replace("wikipedia", '')
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to wikipedia")
#             speak(results)
#         elif 'are you' in query:
#             speak("I am amigo developed by Jaspreet Singh")
#         elif 'open youtube' in query:
#             speak("opening youtube")
#             webbrowser.open("youtube.com")
#         elif 'open google' in query:
#             speak("opening google")
#             webbrowser.open("google.com")
#         elif 'open github' in query:
#             speak("opening github")
#             webbrowser.open("github.com")
#         elif 'open stackoverflow' in query:
#             speak("opening stackoverflow")
#             webbrowser.open("stackoverflow.com")
#         elif 'open spotify' in query:
#             speak("opening spotify")
#             webbrowser.open("spotify.com")
#         elif 'open whatsapp' in query:
#             speak("opening whatsapp")
#             loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
#             os.startfile(loc)
#         elif 'play music' in query:
#             speak("opening music")
#             webbrowser.open("spotify.com")
#         elif 'play music' in query:
#             speak("opening music")
#             webbrowser.open("spotify.com")
#         elif 'local disk d' in query:
#             speak("opening local disk D")
#             webbrowser.open("D://")
#         elif 'local disk c' in query:
#             speak("opening local disk C")
#             webbrowser.open("C://")
#         elif 'local disk e' in query:
#             speak("opening local disk E")
#             webbrowser.open("E://")
#         elif 'sleep' in query:
#             exit(0)








# import speech_recognition as sr
# import pyttsx3
# import datetime
# import wikipedia
# import webbrowser
# import os

# # Initialize the voice engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # Speed of speech

# # Log user queries
# user_questions_log = []

# def speak(audio):
#     print("Amigo says:", audio)
#     engine.say(audio)
#     engine.runAndWait()

# def wish_user():
#     hour = int(datetime.datetime.now().hour)
#     if 0 <= hour < 12:
#         speak("Good morning!")
#     elif 12 <= hour < 18:
#         speak("Good afternoon!")
#     else:
#         speak("Good evening!")
#     speak("I am Amigo, your assistant. How can I help you today?")

# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
    
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")
#     except Exception:
#         speak("Sorry, I didn’t catch that. Could you repeat?")
#         return "None"
#     return query.lower()

# def main():
#     wish_user()
#     while True:
#         query = take_command()
#         if query == "None":
#             continue

#         user_questions_log.append(query)

#         # === Predefined commands ===
#         if 'open youtube' in query:
#             webbrowser.open("https://www.youtube.com")
#             speak("Opening YouTube.")

#         elif 'open google' in query:
#             webbrowser.open("https://www.google.com")
#             speak("Opening Google.")

#         elif 'play music' in query:
#             music_dir = 'C:\\Users\\HP\\Music'  # Change this to your actual path
#             try:
#                 songs = os.listdir(music_dir)
#                 if songs:
#                     os.startfile(os.path.join(music_dir, songs[0]))
#                     speak("Playing music.")
#                 else:
#                     speak("No music files found.")
#             except:
#                 speak("Unable to play music. Folder may not exist.")

#         elif 'time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"The time is {strTime}")

#         elif 'exit' in query or 'quit' in query:
#             speak("Goodbye!")
#             break

#         # === Wikipedia fallback for all other questions ===
#         else:
#             speak("Let me check that on Wikipedia...")
#             clean_query = query.replace("wikipedia", "").replace("what is", "").replace("who is", "").replace("tell me about", "").replace("meaning of", "").strip()
#             try:
#                 results = wikipedia.summary(clean_query, sentences=2)
#                 speak("According to Wikipedia:")
#                 speak(results)
#             except wikipedia.exceptions.DisambiguationError:
#                 speak("There are multiple meanings. Please be more specific.")
#             except wikipedia.exceptions.PageError:
#                 speak("Sorry, I couldn't find any information on that.")
#             except:
#                 speak("Something went wrong while searching Wikipedia.")

#     # Save all user questions after session ends
#     with open("user_questions_log.txt", "w", encoding="utf-8") as f:
#         for q in user_questions_log:
#             f.write(q + "\n")

# if __name__ == "__main__":
#     main()
























# import speech_recognition as sr
# import pyttsx3
# import datetime
# import os
# import requests
# from bs4 import BeautifulSoup
# from gtts import gTTS
# from playsound import playsound
# import wikipedia


# # Speak function with gTTS and fallback
# def speak(text):
#     print("Amigo says:", text)
#     try:
#         mp3 = "temp.mp3"
#         tts = gTTS(text=text, lang="en")
#         tts.save(mp3)
#         playsound(mp3)
#         os.remove(mp3)
#     except Exception:
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()


# # Wish user based on time
# def wish_user():
#     hour = datetime.datetime.now().hour
#     if hour < 12:
#         speak("Good morning!")
#     elif hour < 18:
#         speak("Good afternoon!")
#     else:
#         speak("Good evening!")
#     speak("I am Amigo, your assistant. How can I help you today?")


# # Take voice command
# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         r.adjust_for_ambient_noise(source)
#         try:
#             audio = r.listen(source, timeout=5, phrase_time_limit=6)
#             speak("Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#             print("User said:", query)
#             return query.lower()
#         except sr.WaitTimeoutError:
#             speak("No speech detected.")
#         except sr.UnknownValueError:
#             speak("Sorry, I didn’t catch that.")
#         except sr.RequestError:
#             speak("Speech recognition service is unavailable.")
#     return None


# # Google Search
# def search_google_answer_box(query):
#     try:
#         url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
#         headers = {
#             "User-Agent": "Mozilla/5.0"
#         }
#         res = requests.get(url, headers=headers, timeout=5)
#         soup = BeautifulSoup(res.text, "html.parser")

#         selectors = [
#             "div[data-attrid='wa:/description'] span",
#             "div.Z0LcW",
#             "div.BNeawe.iBp4i.AP7Wnd",
#             "div.BNeawe.s3v9rd.AP7Wnd",
#             "div.kno-rdesc span",
#             "div span.hgKElc"
#         ]

#         for sel in selectors:
#             result = soup.select_one(sel)
#             if result and result.text.strip():
#                 return result.text.strip()
#     except Exception as e:
#         print("Google scrape error:", e)
#     return None


# # Wikipedia Search
# def search_wikipedia(query):
#     try:
#         return wikipedia.summary(query, sentences=2)
#     except wikipedia.DisambiguationError as e:
#         if e.options:
#             try:
#                 return wikipedia.summary(e.options[0], sentences=2)
#             except:
#                 return None
#     except Exception as e:
#         print("Wikipedia error:", e)
#     return None


# # Handle query
# def handle_query(query):
#     if not query:
#         return

#     speak("Let me search that for you...")
#     answer = search_google_answer_box(query)

#     if answer:
#         speak("Here's what I found:")
#         speak(answer)
#     else:
#         speak("Checking Wikipedia...")
#         answer = search_wikipedia(query)
#         if answer:
#             speak("Here's what I found on Wikipedia:")
#             speak(answer)
#         else:
#             speak("Sorry, I couldn't find any answer.")


# # Main function
# def main():
#     wish_user()
#     while True:
#         query = take_command()
#         if query:
#             if "exit" in query or "quit" in query:
#                 speak("Goodbye!")
#                 break
#             elif "open youtube" in query:
#                 speak("Opening YouTube")
#                 os.system("start https://www.youtube.com")
#             elif "open whatsapp" in query:
#                 speak("Opening WhatsApp")
#                 os.system("start https://web.whatsapp.com")
#             else:
#                 handle_query(query)


# if __name__ == "__main__":
#     main()



















# import pyttsx3
# import datetime
# import wikipedia
# import webbrowser
# import pyjokes
# import requests
# from bs4 import BeautifulSoup
# from custom_qa import custom_answers

# def speak(text):
#     print(f"Assistant: {text}")
#     try:
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#     except:
#         print("Speech output not supported.")

# def wish_user():
#     hour = int(datetime.datetime.now().hour)
#     if hour < 12:
#         speak("Good Morning!")
#     elif hour < 18:
#         speak("Good Afternoon!")
#     else:
#         speak("Good Evening!")
#     speak("I am your voice assistant. How can I help you today?")

# def take_command():
#     return input("You (type your command): ").lower()

# def search_google(query):
#     try:
#         headers = {"User-Agent": "Mozilla/5.0"}
#         url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
#         res = requests.get(url, headers=headers, timeout=5)
#         soup = BeautifulSoup(res.text, "html.parser")

#         selectors = [
#             "div[data-attrid='wa:/description'] span",
#             "div[data-attrid='hw:/collection/has_fact:who'] span",
#             "div.kno-rdesc span",
#             "div.Z0LcW",
#             "div.BNeawe.iBp4i.AP7Wnd",
#             "div.BNeawe.s3v9rd.AP7Wnd"
#         ]

#         for sel in selectors:
#             result = soup.select_one(sel)
#             if result and result.text.strip():
#                 print("DEBUG (Google Answer):", result.text.strip())
#                 return result.text.strip()

#         # Fallback: any long text block
#         for span in soup.find_all("span"):
#             if span and len(span.text.strip()) > 50:
#                 print("DEBUG (Fallback):", span.text.strip())
#                 return span.text.strip()

#     except Exception as e:
#         print("Google search error:", e)
#     return None

# def run_assistant():
#     wish_user()
#     while True:
#         query = take_command()

#         if 'open youtube' in query:
#             speak("Opening YouTube...")
#             webbrowser.open("https://www.youtube.com")

#         elif 'open google' in query:
#             speak("Opening Google...")
#             webbrowser.open("https://www.google.com")

#         elif 'time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"The current time is {strTime}")

#         elif 'joke' in query:
#             joke = pyjokes.get_joke()
#             speak(joke)

#         elif 'exit' in query or 'bye' in query:
#             speak("Goodbye! Have a nice day!")
#             break

#         else:
#             # Try Google first
#             answer = search_google(query)
#             if answer:
#                 speak("According to Google:")
#                 speak(answer)
#             else:
#                 # Fallback to Wikipedia
#                 try:
#                     result = wikipedia.summary(query, sentences=2)
#                     speak("According to Wikipedia:")
#                     speak(result)
#                 except:
#                     speak("Sorry, I couldn't find any answer.")

# if __name__ == "__main__":
#     run_assistant()






import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import requests
from bs4 import BeautifulSoup
from custom_qa import custom_answers

def speak(text):
    print(f"Assistant: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech output not supported.")

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")

def take_command():
    return input("You (type your command): ").lower()

def search_google(query):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        selectors = [
            "div[data-attrid='wa:/description'] span",
            "div[data-attrid='hw:/collection/has_fact:who'] span",
            "div.kno-rdesc span",
            "div.Z0LcW",
            "div.BNeawe.iBp4i.AP7Wnd",
            "div.BNeawe.s3v9rd.AP7Wnd"
        ]

        for sel in selectors:
            result = soup.select_one(sel)
            if result and result.text.strip():
                return result.text.strip()

        for span in soup.find_all("span"):
            if span and len(span.text.strip()) > 50:
                return span.text.strip()

    except Exception as e:
        print("Google search error:", e)
    return None

def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
            # 1. Exact match from custom_answers
            if query in custom_answers:
                speak(custom_answers[query])
                continue

            # 2. Google Search
            answer = search_google(query)
            if answer:
                speak("According to Google:")
                speak(answer)
            else:
                # 3. Wikipedia Fallback
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia:")
                    speak(result)
                except:
                    speak("Sorry, I couldn't find any answer.")

if __name__ == "__main__":
    run_assistant()
