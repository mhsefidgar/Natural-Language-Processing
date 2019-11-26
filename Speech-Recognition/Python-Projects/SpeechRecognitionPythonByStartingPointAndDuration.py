# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:39:00 2019

@author: Moh
"""
" this code only works when the audio file and the source code is at the same directory. "


import speech_recognition as sr
r = sr.Recognizer()
AudioFile = sr.AudioFile('AudioFile.wav')
with AudioFile as source:
 audio = r.record(source)
type(audio)
with AudioFile as source:

"OFFSET is the time when the audio file commence and the speech will be recognized during the DURATION value"

audio_offset = r.record(source, offset=4, duration=3)
recognizer.recognize_google(audio_offset)
















