# Orion – My Voice Assistant

## 🚀 About

Orion is a Python-based voice assistant inspired by assistants like Alexa and Google Assistant. It uses voice commands to perform everyday tasks such as opening applications, launching websites, playing music, and answering basic queries.

This project is being built from scratch as a learning project with the goal of creating a powerful desktop AI assistant.

---

## ✨ Current Features

* 🎙️ Wake word activation ("come back")
* 🗣️ Speech recognition using Faster Whisper
* 🔊 Text-to-Speech responses
* 🌐 Open websites (Google, YouTube, GitHub)
* 💻 Open desktop applications
* 🎵 Play songs from YouTube
* ⏰ Tell the current time
* 🪪 Introduce itself
* 🛑 Voice command to stop the assistant

---

## 🛠️ Technologies Used

* Python 3.14
* Faster Whisper
* CTranslate2
* sounddevice
* NumPy
* yt-dlp
* webbrowser
* subprocess

---

## 📂 Project Structure

```text
Orion/
│
├── Main.py
├── commands.py
├── speech.py
├── speak.py
├── music.py
├── mic_test.py
├── requirement.txt
└── .gitignore
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/SarvadnyaDhondge/Orion-My-voice-assistant.git
```

2. Go to the project folder:

```bash
cd Orion-My-voice-assistant
```

3. Create and activate a virtual environment.

4. Install the required packages:

```bash
pip install -r requirement.txt
```

5. Run Orion:

```bash
python Main.py
```

---

## 🎤 Example Commands

* come back open google
* come back open chrome
* come back open calculator
* come back play believer
* come back what is the time
* come back what is your name
* come back stop

---

## 🗺️ Roadmap

### ✅ Completed

* Wake word detection
* Speech recognition
* Text-to-Speech
* Website launcher
* Desktop application launcher
* Music playback
* Time queries

### 🚧 Coming Soon

* Weather information
* Web search
* Notes and reminders
* Folder navigation
* AI-powered conversations
* Camera and vision features
* GUI for Orion
* Memory and personalization
* Smart home integrations

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

---

## 📄 License

This project is currently available for learning and personal use.

---

**Created with ❤️ by Sarvadnya Dhondge**
