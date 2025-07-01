# import speech_recognition as sr
# import pyttsx3
# import wikipedia
# import webbrowser
# import pywhatkit
# import os
# import sys
# import requests
# import re
# import difflib
# from bs4 import BeautifulSoup

# # ✅ Load custom Q&A data
# sys.path.append(r"C:\Users\HP\Downloads\chatbot_data")
# from custom_qa import custom_answers

# # 🎤 Text-to-Speech Setup
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # Female voice
# engine.setProperty('rate', 170)

# def speak(text):
#     print("Assistant:", text)
#     engine.say(text)
#     engine.runAndWait()

# def take_command():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎤 Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         try:
#             audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
#         except sr.WaitTimeoutError:
#             speak("No speech detected.")
#             return ""
#     try:
#         query = recognizer.recognize_google(audio, language="en-IN")
#         print(f"You said: {query}")
#         return query.lower()
#     except sr.UnknownValueError:
#         speak("Sorry, I didn't catch that.")
#         return ""
#     except sr.RequestError:
#         speak("Sorry, I couldn't reach Google services.")
#         return ""

# def is_relevant(text, query):
#     irrelevant_keywords = [
#         'open google maps', 'aadhaar', 'pan card', 'hours',
#         'cost of the restaurant', 'book tickets', 'train booking', 'irctc'
#     ]
#     if re.search(r'[\u4e00-\u9fff]', text):  # Skip Chinese
#         return False
#     if any(bad in text.lower() for bad in irrelevant_keywords):
#         return False
#     if not any(k in text.lower() for k in query.lower().split()):
#         return False
#     return True

# def search_bing(query):
#     headers = {"User-Agent": "Mozilla/5.0"}
#     url = f"https://www.bing.com/search?q={query}&setlang=en"
#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         selectors = [
#             ('div', {'class': 'b_focusTextLarge'}),
#             ('div', {'class': 'b_focusTextMedium'}),
#             ('div', {'class': 'b_lAnswer'}),
#             ('div', {'class': 'b_xlText'}),
#             ('div', {'class': 'b_vPanel'}),
#         ]

#         for tag, attrs in selectors:
#             box = soup.find(tag, attrs)
#             if box:
#                 text = box.get_text(strip=True)
#                 if is_relevant(text, query) and len(text) > 30 and text.isascii():
#                     print("✅ Bing Answer Box:", text)
#                     return text

#         for p in soup.find_all('p'):
#             text = p.get_text(strip=True)
#             if is_relevant(text, query) and len(text) > 50 and text.isascii():
#                 print("✅ Bing Paragraph:", text)
#                 return text

#         return ""
#     except Exception as e:
#         print("❌ Bing search failed:", e)
#         return ""

# def handle_query(query):
#     query = query.lower().strip()
#     query = re.sub(r'[^\w\s]', '', query)

#     # 1. Custom Q&A
#     if query in custom_answers:
#         speak(custom_answers[query])
#         return True
#     else:
#         match = difflib.get_close_matches(query, custom_answers.keys(), n=1, cutoff=0.85)
#         if match:
#             speak(custom_answers[match[0]])
#             return True

#     # 2. System commands
#     if 'open youtube' in query:
#         speak("Opening YouTube.")
#         webbrowser.open("https://www.youtube.com")
#     elif 'play' in query and 'on youtube' in query:
#         song = query.replace("play", "").replace("on youtube", "").strip()
#         speak(f"Playing {song} on YouTube.")
#         pywhatkit.playonyt(song)
#     elif 'open google' in query:
#         speak("Opening Google.")
#         webbrowser.open("https://www.google.com")
#     elif 'search' in query and 'google' in query:
#         search_query = query.replace("search", "").replace("on google", "").strip()
#         speak(f"Searching for {search_query} on Google.")
#         webbrowser.open(f"https://www.google.com/search?q={search_query}")
#     elif 'open github' in query:
#         speak("Opening GitHub.")
#         webbrowser.open("https://github.com")
#     elif 'open stackoverflow' in query:
#         speak("Opening Stack Overflow.")
#         webbrowser.open("https://stackoverflow.com")
#     elif 'open whatsapp' in query:
#         speak("Opening WhatsApp.")
#         path = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
#         if os.path.exists(path):
#             os.startfile(path)
#         else:
#             speak("WhatsApp not found on your system.")
#     elif 'local disk d' in query:
#         speak("Opening Local Disk D.")
#         os.startfile("D:\\")
#     elif 'local disk c' in query:
#         speak("Opening Local Disk C.")
#         os.startfile("C:\\")
#     elif 'local disk e' in query:
#         speak("Opening Local Disk E.")
#         os.startfile("E:\\")
#     elif 'who are you' in query or 'what is your name' in query:
#         speak("I am Amigo, your personal voice assistant.")
#     elif query in ['exit', 'quit', 'stop', 'sleep']:
#         speak("Goodbye!")
#         return False
#     else:
#         # 3. Bing fallback
#         speak("Let me check Bing for that.")
#         result = search_bing(query)
#         if result:
#             speak(f"According to Bing: {result}")
#             return True
#         else:
#             # 4. Wikipedia fallback
#             speak("Bing wasn't helpful. Checking Wikipedia instead.")
#             try:
#                 summary = wikipedia.summary(query, sentences=2)
#                 speak(summary)
#             except wikipedia.exceptions.DisambiguationError:
#                 speak("Too many matches on Wikipedia. Please be more specific.")
#             except wikipedia.exceptions.PageError:
#                 speak("Couldn't find anything on Wikipedia.")
#             except:
#                 speak("Wikipedia failed too.")
#     return True

# # 🎙️ Main Loop
# if __name__ == "__main__":
#     wikipedia.set_lang("en")
#     speak("Good evening! I am your voice assistant. How can I help you today?")
#     while True:
#         command = take_command()
#         if command:
#             if not handle_query(command):
#                 break







#this is current versuion and code

# import speech_recognition as sr
# import pyttsx3
# import wikipedia
# import webbrowser
# import pywhatkit
# import os
# import sys
# import requests
# from bs4 import BeautifulSoup

# # ✅ Load custom Q&A
# sys.path.append(r"C:\Users\HP\Downloads\chatbot_data")  # Your custom_qa.py folder
# from custom_qa import custom_answers

# # ✅ Voice Engine Setup
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # Female
# engine.setProperty('rate', 170)

# def speak(text):
#     print("Assistant:", text)
#     engine.say(text)
#     engine.runAndWait()

# def take_command():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎤 Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
#     try:
#         query = recognizer.recognize_google(audio, language="en-IN")
#         print(f"You said: {query}")
#         return query.lower()
#     except sr.UnknownValueError:
#         speak("Sorry, I didn't catch that.")
#         return ""
#     except sr.RequestError:
#         speak("Sorry, I couldn't reach Google services.")
#         return ""

# def search_bing(query):
#     headers = {"User-Agent": "Mozilla/5.0"}
#     url = f"https://www.bing.com/search?q={query}"
#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         selectors = [
#             ('div', {'class': 'b_focusTextLarge'}),
#             ('div', {'class': 'b_focusTextMedium'}),
#             ('div', {'class': 'b_lAnswer'}),
#             ('div', {'class': 'b_xlText'}),
#             ('div', {'class': 'b_vPanel'}),
#         ]

#         for tag, attrs in selectors:
#             box = soup.find(tag, attrs)
#             if box:
#                 text = box.get_text(strip=True)
#                 if all(ord(c) < 128 for c in text):
#                     return text

#         for p in soup.find_all('p'):
#             text = p.get_text(strip=True)
#             if len(text) > 30 and all(ord(c) < 128 for c in text):
#                 return text

#         return "Sorry, I couldn't find a clear English answer."
#     except:
#         return "Sorry, I couldn't fetch the answer right now."

# def handle_query(query):
#     import re
#     import difflib

#     query = query.lower().strip()
#     query = re.sub(r'[^\w\s]', '', query)

#     # 1. Try custom Q&A
#     if query in custom_answers:
#         speak(custom_answers[query])
#         return True
#     else:
#         match = difflib.get_close_matches(query, custom_answers.keys(), n=1, cutoff=0.85)
#         if match:
#             speak(custom_answers[match[0]])
#             return True

#     # 2. Handle voice commands
#     if 'open youtube' in query:
#         speak("Opening YouTube.")
#         webbrowser.open("https://www.youtube.com")
#     elif 'play' in query and 'on youtube' in query:
#         song = query.replace("play", "").replace("on youtube", "").strip()
#         speak(f"Playing {song} on YouTube.")
#         pywhatkit.playonyt(song)
#     elif 'open google' in query:
#         speak("Opening Google.")
#         webbrowser.open("https://www.google.com")
#     elif 'search' in query and 'google' in query:
#         search_query = query.replace("search", "").replace("on google", "").strip()
#         speak(f"Searching for {search_query} on Google.")
#         webbrowser.open(f"https://www.google.com/search?q={search_query}")
#     elif 'open github' in query:
#         speak("Opening GitHub.")
#         webbrowser.open("https://github.com")
#     elif 'open stackoverflow' in query:
#         speak("Opening Stack Overflow.")
#         webbrowser.open("https://stackoverflow.com")
#     elif 'open whatsapp' in query:
#         speak("Opening WhatsApp.")
#         path = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
#         if os.path.exists(path):
#             os.startfile(path)
#         else:
#             speak("WhatsApp not found on your system.")
#     elif 'local disk d' in query:
#         speak("Opening Local Disk D.")
#         os.startfile("D:\\")
#     elif 'local disk c' in query:
#         speak("Opening Local Disk C.")
#         os.startfile("C:\\")
#     elif 'local disk e' in query:
#         speak("Opening Local Disk E.")
#         os.startfile("E:\\")
#     elif 'who are you' in query or 'what is your name' in query:
#         speak("I am Amigo, your personal voice assistant.")
#     elif query in ['exit', 'quit', 'stop', 'sleep']:
#         speak("Goodbye!")
#         return False

#     # 3. Try Bing → Wikipedia fallback
#     speak("Let me check Bing for that.")
#     result = search_bing(query)
#     if result and "sorry" not in result.lower() and len(result) > 30:
#         speak(f"According to Bing: {result}")
#         return True

#     speak("Checking Wikipedia instead.")
#     try:
#         summary = wikipedia.summary(query, sentences=2)
#         speak(summary)
#     except wikipedia.exceptions.DisambiguationError:
#         speak("Too many results on Wikipedia. Try to be more specific.")
#     except wikipedia.exceptions.PageError:
#         speak("No page found on Wikipedia.")
#     except:
#         speak("Wikipedia search failed too.")

#     return True

# # Main Loop
# if __name__ == "__main__":
#     wikipedia.set_lang("en")
#     speak("Good evening! I am your voice assistant. How can I help you today?")
#     while True:
#         command = take_command()
#         if command:
#             if not handle_query(command):
#                 break















import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit
import os
import sys
import requests
from bs4 import BeautifulSoup

# ✅ Load custom Q&A
sys.path.append(r"C:\Users\HP\Downloads\chatbot_data")  # Your custom_qa.py folder
from custom_qa import custom_answers

# ✅ Voice Engine Setup
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
    try:
        query = recognizer.recognize_google(audio, language="en-IN")
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I couldn't reach Google services.")
        return ""

def search_bing(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.bing.com/search?q={query}"
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        selectors = [
            ('div', {'class': 'b_focusTextLarge'}),
            ('div', {'class': 'b_focusTextMedium'}),
            ('div', {'class': 'b_lAnswer'}),
            ('div', {'class': 'b_xlText'}),
            ('div', {'class': 'b_vPanel'}),
        ]

        for tag, attrs in selectors:
            box = soup.find(tag, attrs)
            if box:
                text = box.get_text(strip=True)
                if all(ord(c) < 128 for c in text):
                    return text

        for p in soup.find_all('p'):
            text = p.get_text(strip=True)
            if len(text) > 30 and all(ord(c) < 128 for c in text):
                return text

        return "Sorry, I couldn't find a clear English answer."
    except:
        return "Sorry, I couldn't fetch the answer right now."

def handle_query(query):
    import re
    import difflib

    query = query.lower().strip()
    query = re.sub(r'[^\w\s]', '', query)

    # 1. Try custom Q&A
    if query in custom_answers:
        speak(custom_answers[query])
        return True
    else:
        match = difflib.get_close_matches(query, custom_answers.keys(), n=1, cutoff=0.85)
        if match:
            speak(custom_answers[match[0]])
            return True

    # 2. Handle voice commands
    if 'open youtube' in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif 'play' in query and 'on youtube' in query:
        song = query.replace("play", "").replace("on youtube", "").strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
    elif 'open google' in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif 'search' in query and 'google' in query:
        search_query = query.replace("search", "").replace("on google", "").strip()
        speak(f"Searching for {search_query} on Google.")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif 'open github' in query:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")
    elif 'open stackoverflow' in query:
        speak("Opening Stack Overflow.")
        webbrowser.open("https://stackoverflow.com")
    elif 'open whatsapp' in query:
        speak("Opening WhatsApp.")
        path = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        if os.path.exists(path):
            os.startfile(path)
        else:
            speak("WhatsApp not found on your system.")
    elif 'local disk d' in query:
        speak("Opening Local Disk D.")
        os.startfile("D:\\")
    elif 'local disk c' in query:
        speak("Opening Local Disk C.")
        os.startfile("C:\\")
    elif 'local disk e' in query:
        speak("Opening Local Disk E.")
        os.startfile("E:\\")
    elif 'who are you' in query or 'what is your name' in query:
        speak("I am Amigo, your personal voice assistant.")
    elif query in ['exit', 'quit', 'stop', 'sleep']:
        speak("Goodbye!")
        return False

    # 3. Try Bing → Wikipedia fallback
    speak("Let me check Bing for that.")
    result = search_bing(query)
    if result and "sorry" not in result.lower() and len(result) > 30:
        speak(f"According to Bing: {result}")
        return True

    speak("Checking Wikipedia instead.")
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError:
        speak("Too many results on Wikipedia. Try to be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No page found on Wikipedia.")
    except:
        speak("Wikipedia search failed too.")

    return True

# Main Loop
if __name__ == "__main__":
    wikipedia.set_lang("en")
    speak("Good evening! I am your voice assistant. How can I help you today?")
    while True:
        command = take_command()
        if command:
            if not handle_query(command):
                break
















