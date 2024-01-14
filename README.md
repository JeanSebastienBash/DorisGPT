# DorisGPT

This script enables users to dictate a vocal prompt, send the request to ChatGPT, and receive the corresponding response, all in a vocal manner.

<audio controls>
  <source src="./output/question.wav" type="audio/wav">
</audio>

1. **Clone** DorisGPT Repo on you laptop or server with micro device entry :
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

3. **Configure** the vosk model you want use in **lib/speech2text.py** :
```bash
nano lib/text2speech.py # comment or uncomment as you want
# https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip
# or https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip
```

4. **Configure** the time duration between start bip & end bip (for vocal micro entry)  in **lib/speech2text.py** :
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
mkdir output/
mkdir -p lib/models/vosk

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
