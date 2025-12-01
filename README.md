# J.A.R.V.I.S - Advanced AI Assistant System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/purvanshjoshi/jarvis-ai-assistant?style=social)](https://github.com/purvanshjoshi/jarvis-ai-assistant)

## Overview

J.A.R.V.I.S is a sophisticated, full-stack AI assistant system featuring real-time system monitoring, live camera feed, voice control capabilities, and intelligent command execution. Inspired by Tony Stark's AI from Iron Man, this advanced system combines cutting-edge technologies to create a powerful personal assistant.

## Key Features

- **Real-time System Monitoring**: CPU, Memory, Disk, Temperature, Battery tracking
- **Live Camera Feed**: Integrated camera support with face detection
- **Voice Control**: Advanced voice recognition and command processing  
- **AI-Powered Commands**: Natural language understanding and execution
- **Window Management**: Control applications via voice or GUI
- **File Operations**: Smart file/folder management with fuzzy search
- **Memory System**: Persistent conversation memory with retrieval
- **Advanced HUD Interface**: Animated neon design with multiple themes

## Core Components

- `jarvis_gui.py` - Main futuristic GUI interface with real-time metrics
- `Jarvis_prompts.py` - Command processing engine with memory system
- `Jarvis_window_CTRL.py` - Application and window management
- `Jarvis_file_opner.py` - Intelligent file/folder operations

## Installation

```bash
git clone https://github.com/purvanshjoshi/jarvis-ai-assistant.git
cd jarvis-ai-assistant
pip install -r requirements.txt
```

## Usage

```bash
# Launch main GUI
python jarvis_gui.py

# Or run file manager
python Jarvis_file_opner.py
```

## Dependencies

- PySide6>=6.4.0 - Modern Qt GUI framework
- psutil>=5.9.0 - System monitoring
- opencv-python>=4.6.0 - Computer vision
- SpeechRecognition>=3.10.0 - Voice recognition
- fuzzywuzzy>=0.18.0 - Fuzzy string matching
- PyAutoGUI>=0.9.53 - GUI automation
- pygetwindow>=0.0.9 - Window management

## Features Breakdown

### System Monitoring
- Real-time CPU, Memory, Disk, Temperature tracking
- Battery status and network speed monitoring
- Top processes listing
- System uptime tracking

### Voice Commands
- Natural language processing
- Application launching
- File operations (create, delete, rename)
- System commands execution
- Fuzzy matching for command resilience

### GUI Features
- Multiple theme support (Blue, Red, Green)
- Live camera feed with face detection
- Screenshot and snapshot capture
- Interactive console for debugging
- Real-time metrics dashboard

### Memory System
- Persistent conversation logging
- Context-aware response generation
- User preference learning
- Conversation history retrieval

## Configuration

Edit settings in config files:
```python
# Theme: 'blue', 'red', 'green'
THEME = 'blue'

# Voice enabled
VOICE_ENABLED = True

# Camera settings
CAMERA_FPS = 30
CAMERA_RESOLUTION = (320, 240)
```

## Troubleshooting

### Camera Issues
- Check camera connection and permissions
- Reinstall OpenCV: `pip install --upgrade opencv-python`

### Voice Recognition
- Ensure microphone is connected
- Install PyAudio: `pip install pyaudio`

### GUI Loading
- Verify PySide6: `pip install --upgrade PySide6`
- Check Python 3.8+ requirement

## Performance Tips

1. Optimize system monitoring - disable unused metrics
2. Reduce GUI update frequency
3. Regular memory.json cleanup
4. Enable GPU acceleration if available

## Security

- Do NOT hardcode sensitive credentials
- Use environment variables for API keys
- Encrypt memory.json if storing sensitive data
- Run with minimal required permissions

## Future Enhancements

- [ ] Multi-language support
- [ ] Advanced NLP integration
- [ ] Cloud synchronization
- [ ] Mobile companion app
- [ ] Extended platform support (Mac, Linux)
- [ ] Plugin system
- [ ] Advanced analytics

## License

MIT License - See LICENSE file for details

## Author

**Purvansh Joshi**
- Computer Science Engineering Student @ Graphic Era Hill University
- Full-Stack Developer | ML Enthusiast | Open Source Contributor
- [GitHub](https://github.com/purvanshjoshi) | [LinkedIn](https://linkedin.com/in/purvansh-joshi)

## Support

If you find this useful:
- Star the repository
- Report issues
- Contribute code
- Suggest improvements

## Contact

- Email: purvanshjoshi7534@gmail.com
- GitHub Issues: [Report Bug](https://github.com/purvanshjoshi/jarvis-ai-assistant/issues)
- LinkedIn: [Purvansh Joshi](https://linkedin.com/in/purvansh-joshi)

---

**Made with ❤️ by Purvansh Joshi | December 2025**
