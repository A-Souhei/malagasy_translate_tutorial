"""
This program translates words between English-French-Malagasy using a dictionary specified in a JSON file.

1. Execute file and see how it tranlsates a word "salama"
2. Create a loop allowing to translate more words. You can make a condition that loop exits if user writes word "veloma".

3. Allow translations between three languages. It will require a different approach. My initial idea is to specify corresponding lists of words for every language:
'en-fr-ma.json'

Good luck!
"""

import json

with open('ma-en.json') as json_data:
    ma_en_dict = json.load(json_data)

while True:
    ma_word = input("Word in Malagasy: ")
    if ma_word == "veloma":
        break
    try:
        en_word = ma_en_dict[ma_word]
        print ("En: ", en_word)		
    except:
        print("this word is not in the database")



print("Veloma! Goodbye!")



