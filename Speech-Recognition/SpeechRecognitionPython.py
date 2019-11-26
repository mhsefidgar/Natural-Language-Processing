# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:39:00 2019

@author: Moh
"""
" this code only works when the audio file and the source code is at the same directory. "

import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('AudioFile.wav')
with harvard as source:
 audio = r.record(source)
type(audio)
r.recognize_google(audio)
















