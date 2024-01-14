# DorisGPT

This script allows users to dictate a voice command, send the transcribed text request to ChatGPT, and receive the corresponding text response, which is then vocally transcribed back to the user.

Additionally:
- The script is executed in the console on a Linux machine equipped with a microphone.
- The transcription of the user's audio question and the text output from ChatGPT are displayed in the console during the execution of the DorisGPT script.
- In the end, the DorisGPT script assembles the fragments of audio files to merge them into a single file named response.wav. You will also find other output files in the output/ directory.

### DEPLOYMENT

1. **Clone** DorisGPT Repo on your laptop or server using the micro device input: :
```bash
git clone https://github.com/JeanSebastienBash/DorisGPT
```

2. **Download** and **Extract** the Vosk model of your choice :
```bash
# Official Vosk Page Models
# https://alphacephei.com/vosk/models
# French models
# https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip
# or https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip
```

3. **Configure** the vosk template you wish to use in **lib/speech2text.py** :
```bash
nano lib/text2speech.py # comment or uncomment as you want
# https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip
# or https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip
```

4. **Set** the duration between the start and end beeps (for the voice question) in **lib/speech2text.py** :
```bash
nano lib/text2speech.py # change number as duration you want
duration = 5 # change here
```

5. **Configure** your OpenAiI API Key in **lib/text2speech.py** :
```bash
openai.api_key = "YOUR TOKEN HERE```
```

6. **Install** the pre-requisites :
```bash
sudo apt install sox
python3 -m venv venv
source venv/bin/activate
pip install openai==0.28

# tree -L 5
├── dorisgpt.sh
├── lib
│   ├── models
│   │   └── vosk
│   │       ├── vosk-model-fr-0.22
│   │       │   ├── am
│   │       │   ├── conf
│   │       │   ├── graph
│   │       │   ├── ivector
│   │       │   ├── README
│   │       │   ├── rescore
│   │       │   └── rnnlm
│   │       └── vosk-model-small-fr-0.22
│   │           ├── am
│   │           ├── conf
│   │           ├── graph
│   │           ├── ivector
│   │           └── README
│   ├── speech2text.py
│   └── text2speech.py
└── output
    ├── question
    ├── question.wav
    ├── reponse_0.wav
    ├── reponse_2.wav
    ├── reponse_4.wav
    ├── reponse_clean.txt
    ├── reponse_global.wav
    └── reponse.txt
```

<p align="center">
  <img src="dorisgpt.jpg" alt="doris image"/>
</p>
