# ChatMoji

ChatMoji is a real-time audio transcription chat application written in Python using the Kivy library. The application allows users to connect to a server, send and receive messages, and view the chat history in a scrollable interface.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Before running the application, you will need to have the following installed on your machine:

* Python 3.x
* Kivy 2.1.0 or later
* Selenium
* pywin 
* pyaudio
* websockets
### Installation

### Windows
```bash
pip install pywin 
pipwin install pyaudio 
pip install kivy
pip install websockets
pip install Selenium
```

1. Clone the repository:
   `git clone https://github.com/alirafee21/ChatMoji.git`
2. Run Server
   1. `python socket_server.py`
   2. IP: 127.0.0.1
   3. PORT: 1234
  
3. Run Main application 
   `python ChatMoji.py`
