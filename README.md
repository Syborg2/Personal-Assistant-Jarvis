# Jarvis AI Assistant 🤖

A comprehensive voice-controlled AI assistant built in Python that can perform various tasks through speech recognition and text-to-speech capabilities. Inspired by Iron Man's JARVIS, this assistant can help you control your computer, search the web, get weather updates, play music, and much more!

## 🎯 Features

### 🗣️ Voice Control
- **Speech Recognition** - Responds to voice commands
- **Text-to-Speech** - Provides vocal feedback
- **Wake/Sleep Commands** - "wake up" to activate, "go to sleep" to deactivate

### 🎵 Media Control
- **YouTube Control** - Play, pause, mute videos with voice commands
- **Volume Control** - Adjust system volume up/down
- **Personal Playlist** - Plays random songs when you're tired
- **Screenshot Capture** - Take screenshots with voice command
- **Camera Control** - Take photos through voice command

### 🌐 Web & Search
- **Google Search** - Search anything on Google
- **YouTube Search** - Find and play YouTube videos
- **Wikipedia Search** - Get information from Wikipedia
- **News Reading** - Get latest news updates
- **Weather Updates** - Real-time temperature for Kolkata

### 💻 System Control
- **App Management** - Open and close applications
- **System Shutdown** - Safely shutdown your computer
- **Internet Speed Test** - Check upload/download speeds
- **Calculator** - Perform mathematical calculations

### 📱 Communication & Productivity
- **WhatsApp Automation** - Send messages automatically
- **Alarm Setting** - Set custom alarms
- **Memory Function** - Remember and recall information
- **Translation** - Translate text between languages
- **Time Announcement** - Get current time

### 🎮 Entertainment
- **Interactive Games** - Built-in games to play
- **Random Music Player** - Curated playlist for relaxation

## 🛠️ Technologies Used
- Python 3.x - Core programming language
- `pyttsx3` - Text-to-speech conversion
- `speech_recognition` - Speech-to-text conversion
- `requests` - HTTP requests for web scraping
- `BeautifulSoup4` - HTML parsing for web scraping
- `pyautogui` - GUI automation and screenshot
- `webbrowser` - Web browser control
- `speedtest` - Internet speed testing
- Weather API - Real-time weather data

## 📦 Installation

### Clone the repository:
```bash
git clone <repository-url>
cd jarvis-ai-assistant
```

### Install required packages:
```bash
pip install -r requirements.txt
```

### Set up additional modules (ensure these files exist in your project):
- `INTRO.py` - Introduction/welcome module
- `GreetMe.py` - Greeting functionality
- `keyboard.py` - Volume control functions
- `Dictapp.py` - App opening/closing functions
- `SearchNow.py` - Search functionality
- `NewsRead.py` - News reading module
- `Calculatenumbers.py` - Calculator functions
- `Whatsapp.py` - WhatsApp automation
- `game.py` - Game functions
- `Translator.py` - Translation module

### Configure API Keys:
- Weather API key is included (replace with your own if needed)
- Set up WhatsApp automation credentials if using that feature

## 🚀 Usage

### Start the assistant:
```bash
python Jarvis_main.py
```

### Wake up Jarvis:
- Say **"wake up"** to activate the assistant

### Use voice commands like:
- `"Hello"` - Greet Jarvis
- `"What's the time"` - Get current time
- `"Temperature"` - Get weather in Kolkata
- `"Play"` / `"Pause"` - Control media playback
- `"Volume up"` / `"Volume down"` - Adjust volume
- `"Google search [query]"` - Search Google
- `"YouTube [query]"` - Search YouTube
- `"Take screenshot"` - Capture screen
- `"Set an alarm"` - Create alarm
- `"News"` - Get latest news
- `"Internet speed"` - Test connection speed
- `"Remember that [message]"` - Store information
- `"What do you remember"` - Recall stored info
- `"Translate [text]"` - Translate text
- `"I'm tired"` - Play relaxing music
- `"Go to sleep"` - Deactivate assistant
- `"Finally sleep"` - Exit program

## 📁 Project Structure
```
jarvis-ai-assistant/
├── Jarvis_main.py          # Main application file
├── INTRO.py                # Introduction module
├── GreetMe.py              # Greeting functions
├── keyboard.py             # Volume control
├── Dictapp.py              # App management
├── SearchNow.py            # Search functionality
├── NewsRead.py             # News reading
├── Calculatenumbers.py     # Calculator
├── Whatsapp.py             # WhatsApp automation
├── game.py                 # Game functions
├── Translator.py           # Translation module
├── alarm.py                # Alarm functionality
├── Alarmtext.txt           # Alarm storage
├── Remember.txt            # Memory storage
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## 🔧 Configuration

### Weather API
The assistant uses Visual Crossing Weather API. The current API key is included, but you can get your own at [Visual Crossing Weather](https://www.visualcrossing.com/weather-data-editions).

### Personal Playlist
Update the YouTube links in the "tired" command section with your favorite songs:
```python
# Replace these URLs with your preferred songs
webbrowser.open("YOUR_YOUTUBE_LINK_1")
webbrowser.open("YOUR_YOUTUBE_LINK_2")
webbrowser.open("YOUR_YOUTUBE_LINK_3")
```

## 🎤 Voice Commands Reference

### Basic Conversation
- `"Hello"` → Greeting response
- `"How are you"` → Status response
- `"Thank you"` → Acknowledgment

### Media Control
- `"Play"` / `"Pause"` → Control video playback
- `"Mute"` → Mute/unmute audio
- `"Volume up"` / `"Volume down"` → Adjust volume

### Search & Information
- `"Google [query]"` → Search Google
- `"YouTube [query]"` → Search YouTube
- `"Wikipedia [query]"` → Search Wikipedia
- `"Temperature"` → Get weather info
- `"News"` → Get latest news
- `"The time"` → Current time

### System Operations
- `"Open [app name]"` → Launch application
- `"Close [app name]"` → Close application
- `"Screenshot"` → Take screenshot
- `"Click my photo"` → Open camera
- `"Internet speed"` → Speed test
- `"Shutdown the system"` → System shutdown

### Productivity
- `"Set an alarm"` → Create alarm
- `"Calculate [expression]"` → Math calculations
- `"Remember that [message]"` → Store information
- `"What do you remember"` → Recall stored info
- `"Translate [text]"` → Translation
- `"WhatsApp"` → Send WhatsApp message

### Entertainment
- `"I'm tired"` → Play random music
- `"Start game"` → Launch game

### Control Commands
- `"Wake up"` → Activate assistant
- `"Go to sleep"` → Deactivate (return to wake mode)
- `"Finally sleep"` → Exit program completely

## 🔒 Privacy & Security
- Voice commands are processed locally when possible
- Internet connection required for web searches, weather, and news
- No voice data is permanently stored
- Memory function stores text locally in `Remember.txt`

## 🐛 Troubleshooting

### Common Issues:
- **Microphone not working:** Check microphone permissions and default device
- **Speech not recognized:** Speak clearly and ensure quiet environment
- **Import errors:** Make sure all required modules are installed
- **Weather not working:** Check internet connection and API key validity

### Dependencies Issues:
If you encounter installation issues:
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 🚀 Future Enhancements
- Smart home device integration
- Email management
- Calendar scheduling
- Multiple language support
- Machine learning for better command recognition
- GUI interface
- Mobile app companion

## 🤝 Contributing
Feel free to contribute to this project by:
- Forking the repository
- Creating a feature branch
- Making your changes
- Submitting a pull request

## 📝 License
This project is open source and available under the MIT License.

## 🎯 Acknowledgments
- Inspired by Marvel's JARVIS AI assistant
- Built using various open-source Python libraries
- Weather data provided by Visual Crossing Weather API

> **Note:** This assistant requires a microphone and speakers/headphones for full functionality. Some features may require additional setup or API keys.
