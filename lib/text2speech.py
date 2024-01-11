import os
import sys
import openai
import re
openai.api_key = "OPENAI-TOKEN"
if len(sys.argv) > 1:
    question = sys.argv[1]
else:
    question = "Je veux que tu me parles bri?vement du mod?le JANUS de Jean Pierre Petit."
retry_limit = 3
retry_count = 0
while retry_count < retry_limit:
    retry_count += 1
    print(f"Tentative {retry_count}...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=256
        )
        if response.choices:
            break
    except openai.error.APIError:
        pass
with open('output/reponse.txt', 'w') as f:
    f.write(response.choices[0].message.content)
clean_text = re.sub(r"-\s", "", response.choices[0].message.content)
with open('output/reponse_clean.txt', 'w') as f:
    f.write(clean_text)
phrases = clean_text.split('\n')
for phrase in phrases:
    phrase = phrase.strip()
    if phrase:
        print(phrase)
        os.system(f'pico2wave -l fr-FR -w output/reponse_{phrases.index(phrase)}.wav "{phrase}" 2>/dev/null && play output/reponse_{phrases.index(phrase)}.wav 2>/dev/null')
os.system('sox output/reponse_*.wav output/reponse_global.wav')


