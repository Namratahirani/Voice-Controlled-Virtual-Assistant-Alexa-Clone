
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Initialize speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    """Function to make Alexa speak"""
    print(f"Alexa: {text}")  # Display Alexa's message on the console
    engine.say(text)
    engine.runAndWait()

def alexa_command():
    """Function to take user input via voice"""
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except Exception as e:
        print(f"Error: {e}")
        return ""  # Return an empty string in case of errors

def get_choice():
    """Function to get user input (voice or text)"""
    talk("Please say or type your choice.")
    print("\nYou can either type your choice or speak it.")
    print("Options:")
    print("1. Play a song 🎵")
    print("2. Search Google 🔍")
    print("3. Tell time 🕒")
    print("4. Exit ❌")

    user_choice = input("Type here or say aloud: ").strip().lower()
    
    if not user_choice:  # If input is empty, try voice input
        user_choice = alexa_command()

    return user_choice

def play_song():
    """Function to play a song on YouTube"""
    talk("Which song do you want me to play?")
    song = alexa_command() or input("Type the song name: ").strip()

    if song:
        talk(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
        talk("Playback started. Enjoy your song!")
    else:
        talk("I didn't get the song name. Please try again.")

def search_google():
    """Function to search something on Google"""
    talk("What do you want to search?")
    query = alexa_command() or input("Type your search query: ").strip()

    if query:
        talk(f"Searching Google for {query}.")
        pywhatkit.search(query)
    else:
        talk("I didn't get the search query. Please try again.")

def tell_time():
    """Function to tell the current time"""
    time = datetime.datetime.now().strftime("%I:%M %p")
    talk(f"The current time is {time}")
    print(f"Time: {time}")

def run_alexa():
    """Main function to run Alexa with menu options"""
    talk("Hello, I am your Alexa. How can I help you today?")

    while True:
        user_choice = get_choice()

        if "play" in user_choice or "1" in user_choice:
            play_song()
        elif "search" in user_choice or "2" in user_choice:
            search_google()
        elif "time" in user_choice or "3" in user_choice:
            tell_time()
        elif "exit" in user_choice or "4" in user_choice:
            talk("Goodbye! Have a great day!")
            break
        else:
            talk("Sorry, I didn't understand. Please try again.")

        # Ask if the user wants to continue
        talk("Do you want to continue?")
        cont = alexa_command() or input("Do you want to continue? (yes/no): ").strip().lower()
        if "no" in cont or "exit" in cont:
            talk("Goodbye! Have a nice day!")
            break

# Run Alexa
run_alexa()

