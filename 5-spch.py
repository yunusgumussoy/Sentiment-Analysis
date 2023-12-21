# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:22:28 2023

@author: Yunus
"""


"""pip install gTTs"""

from gtts import gTTS
import os

"""text = "Natural language processing is good for design and development"""""
"""language = 'en'  # Change to 'es' if you want Spanish"""

text = "Man United misery continues as Galatasaray win 3-2 at Old Trafford"
language = 'en'


speech = gTTS(text=text, lang=language)

output_file = "text.mp3"
speech.save(output_file)
os.system(f"start {output_file}")
