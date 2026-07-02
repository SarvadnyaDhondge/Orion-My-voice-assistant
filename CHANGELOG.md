# Changelog

All notable changes to **Orion Voice Assistant** are documented in this file.

The project follows **Semantic Versioning (vMAJOR.MINOR.PATCH)** during development.

---

## [Unreleased]

### Planned
- Brightness control system
- Internet speed monitoring
- Screenshot capture
- Wi-Fi information module
- Timers and alarms
- Calendar integration
- Media controls (play, pause, next, previous)
- AI conversation improvements
- Memory and context awareness system

---

## [0.5.0] - Volume Control Upgrade

### Added
- System volume status retrieval
- Increase/decrease volume controls
- Set volume by percentage
- Mute and unmute functionality

### Improved
- More natural voice responses
- Better command parsing and recognition
- Volume boundary protection (0–100%)
- Improved integration with `pycaw`

### Fixed
- Audio interface compatibility issues
- Edge-case command parsing bugs
- Incorrect volume scaling in some cases

---

## [0.4.0] - System Monitoring

### Added
- Battery status monitoring
- CPU usage tracking
- RAM usage analysis
- Disk usage monitoring
- Internet connectivity checker

### Improved
- Clean separation of system logic into `system_service.py`
- More structured system response formatting

---

## [0.3.0] - Search & Notes System

### Added
- Google search via voice
- Voice-based note creation
- Local note storage system

### Improved
- Command routing structure in `commands.py`
- Better modular skill handling

---

## [0.2.0] - Weather System

### Added
- OpenWeather API integration
- Current temperature retrieval
- Humidity reporting
- Weather description support
- City-based weather queries

### Improved
- Fully modular weather service design
- Cleaner API separation (`service` vs `skill` layer)

---

## [0.1.0] - Initial Release

### Added
- Basic Orion project structure
- Virtual environment setup
- Speech recognition (Whisper integration)
- Text-to-speech engine
- Wake word detection system
- Command dispatcher architecture