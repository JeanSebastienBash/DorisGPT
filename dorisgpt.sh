#!/bin/bash
python3 lib/speech2text.py > output/question 2> /dev/null
cat output/question
thequestion=$(cat output/question)
python3 lib/text2speech.py "${thequestion}"
