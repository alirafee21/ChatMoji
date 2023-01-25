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
   `python socket_server.py`
3. Run Main application 
   `python ChatMoji.py`
 
 ### Usage
   1. Enter your desired IP, port, and username in the input fields.
   2. Press the join button to connect to the server.
   3. Once connected, you can start sending messages through audio transcription.
   4. You can resize the main chat interface by dragging the edges.

### Authors
* Rafee Ali

### Acknowledgments
* Inspiration: To create a chat application that utilizes audio transcription as a way to send messages with text & emoji for those with writiing disabilities.
