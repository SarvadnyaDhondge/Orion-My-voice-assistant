# 🎙️ Orion – Python Voice Assistant

Orion is a modular voice assistant built in Python using Faster-Whisper for speech recognition and Text-to-Speech for voice responses.

The goal of this project is to build a personal assistant similar to Alexa or Google Assistant while following good software engineering practices such as modular architecture, configuration management, and version control.

---

## ✨ Features

* 🎤 Wake word detection ("Come back")
* 🗣️ Speech recognition using Faster-Whisper
* 🔊 Text-to-Speech responses
* 💻 Open desktop applications
* 📂 Open folders
* 🌐 Open websites
* 🔍 Google Search
* 🎵 Play music from voice commands
* 📝 Create notes
* 🌡️ Live temperature information using the OpenWeather API
* ⏰ Reminders Management
* ⚙️ Modular project architecture
* 🔐 Secure API key management using `.env`
* 📦 Git & GitHub version control

---

## 🛠️ Technologies Used

* Python 3.14
* Faster-Whisper
* SpeechRecognition
* pyttsx3
* Requests
* python-dotenv
* OpenWeather API

---

## 📁 Project Structure

```text
Orion/
│
├── config/
├── data/
├── services/
├── skills/
├── utils/
│
├── Main.py
├── commands.py
├── speech.py
├── speak.py
├── music.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```env
WEATHER_API_KEY=your_openweather_api_key
```

5. Run the assistant:

```bash
python Main.py
```

---

## 📌 Current Version

**Orion v0.8**

---

## 🎯 Future Features

* 📅 Calendar integration
* 📧 Email support
* 🤖 AI chat assistant
* 📰 News updates
* 📸 Screenshot utility
* 🔋 System monitoring
* 🔊 Volume and brightness control

---

## 👨‍💻 Author

**Sarvadnya Dhondge**
