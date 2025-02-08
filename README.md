# Voice-Controlled-Virtual-Assistant-Alexa-Clone
Developed a Python-based voice-controlled assistant using **speech recognition** and **text-to-speech** technologies. The assistant performs tasks like playing YouTube songs, searching Google, and telling the time. It provides both voice and text input options, enhancing user interaction with seamless task automation.



## Overview

This Python project implements a basic voice-controlled virtual assistant similar to Alexa. It leverages **speech recognition**, **text-to-speech**, and **YouTube automation** to perform tasks such as playing songs, searching Google, and telling the time. It is designed to enhance user interaction through voice commands, offering both voice and text input options. The assistant also asks if the user wants to continue after each task, improving usability and providing a personalized experience.

## Features

- **Voice Interaction:** The assistant listens to user commands and responds via speech.
- **Task Automation:**
  - **Play Songs**: Searches and plays songs on YouTube.
  - **Search Google**: Allows users to search queries on Google.
  - **Tell Time**: Retrieves and tells the current time.
- **Seamless Input Options**: Accepts both **voice and text inputs**.
- **Menu-Driven**: Displays options on the console for user selection.
- **Continual Interaction**: Asks if the user wants to continue after completing each task.

## Libraries Used

- **speech_recognition**: Converts speech into text to process commands.
- **pyttsx3**: Converts text into speech to make the assistant speak.
- **pywhatkit**: Automates YouTube search and Google search.
- **datetime**: Retrieves the current system time for display.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

   `requirements.txt` contains the following libraries:
   ```
   speechrecognition
   pyttsx3
   pywhatkit
   datetime
   ```

## Usage

1. Run the program using:
   ```
   python alexa_assistant.py
   ```

2. The assistant will introduce itself and display a menu of available tasks, such as playing a song, searching Google, and telling the time.

3. **Voice Input:** Simply speak your command after the assistant asks for input.
4. **Text Input:** You can also type your choice if voice input is not working.

5. After performing the task, the assistant will ask if you would like to continue or exit.

## Example Interaction

```
Alexa: Hello, I am your Alexa. How can I help you today?
You can either type your choice or speak it.
Options:
1. Play a song 🎵
2. Search Google 🔍
3. Tell time 🕒
4. Exit ❌

Type here or say aloud: play a song
Alexa: Which song do you want me to play?
Type the song name: Despacito
Alexa: Playing Despacito on YouTube.
Alexa: Playback started. Enjoy your song!
Alexa: Do you want to continue?
Do you want to continue? (yes/no): no
Alexa: Goodbye! Have a nice day!
```

## Contribution

Feel free to fork this repository and contribute to its development. You can:
- Add new features.
- Fix bugs or improve code quality.
- Improve documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


