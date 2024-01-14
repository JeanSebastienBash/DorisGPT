# DorisGPT

This script enables users to dictate a vocal prompt, send the request to ChatGPT, and receive the corresponding response, all in a vocal manner.

1. **Install** the pre-requisites :
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

2. **Download** the Vosk model of your choice :
```bash
# https://alphacephei.com/vosk/models

# French models
# https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip
# or https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip
```

<p align="center">
  <img src="dorisgpt.jpg" alt="doris image"/>
</p>
