# 🎙️ Orion – Python Voice Assistant

Orion is a **modular voice assistant built in Python** using Faster-Whisper for speech recognition and text-to-speech for responses.

The goal of this project is to build a personal assistant similar to **Alexa or Google Assistant**, while following clean software engineering principles such as modular architecture, separation of concerns, and version control.

---

## ✨ Features

- 🎤 Wake word detection ("Come back")
- 🗣️ Speech recognition using Faster-Whisper
- 🔊 Text-to-Speech responses
- 💻 Open desktop applications
- 📂 Open system folders
- 🌐 Open websites
- 🔍 Google search via voice
- 🎵 Music playback from voice commands
- 📝 Voice-based note creation
- 🌡️ Live weather information (OpenWeather API)
- ⏰ Reminder management system
- ⚙️ Fully modular architecture
- 🔐 Secure API key management using `.env`
- 📦 Git & GitHub version control

---

## 🛠️ Technologies Used

- Python 3.14
- Faster-Whisper
- SoundDevice
- NumPy
- Pyttsx3 (Text-to-Speech)
- Requests
- Python-dotenv
- OpenWeather API

---

## 📁 Project Structure

```text
Orion/
│
├── config/
├── data/
├── services/        # System-level APIs (no speech/logic)
├── skills/          # Command understanding layer
├── utils/           # Helpers and utilities
│
├── Main.py          # Entry point
├── commands.py      # Command router
├── speech.py        # Speech-to-text engine
├── speak.py         # Text-to-speech engine
├── music.py         # Music engine
├── requirements.txt
└── README.md
````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/orion.git
cd orion
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file in the project root:

```env
WEATHER_API_KEY=your_openweather_api_key
```

---

## ▶️ Run Orion

```bash
python Main.py
```

---

## 📌 Current Version

**Orion v0.8.0 (Development Build)**

---

## 🧠 Architecture Philosophy

Orion follows a strict layered architecture:

* **services/** → System-level operations (no speech or logic)
* **skills/** → Command understanding + response logic
* **commands.py** → Central command router
* **Main.py** → Runtime loop & wake word detection

This ensures:

* Clean separation of responsibilities
* Easy scalability
* Easy debugging
* Plugin-ready structure

---

## 🚀 Future Features

* 📅 Calendar integration
* 📧 Email automation
* 🤖 AI conversational assistant
* 📰 News updates
* 📸 Screenshot utility
* 🔋 System performance dashboard
* 🔊 Advanced volume & brightness control
* 🧠 Memory + context awareness system

---

## 👨‍💻 Author

**Sarvadnya Dhondge**

---

## ⭐ Project Status

> Orion is under active development. Features are being added step-by-step with a focus on clean architecture and scalability.

```