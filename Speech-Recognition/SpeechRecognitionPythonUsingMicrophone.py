# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:39:00 2019

@author: Moh
"""
" this code only works when the audio file and the source code is at the same directory. "


import speech_recognition as sr
r = sr.Recognizer()

"Get the list of available microphones"
mic_list = sr.Microphone.list_microphone_names()
sr.Microphone.list_microphone_names()

mic = sr.Microphone()
" Alternatively you can choose your microphone with mic = sr.Microphone(device_index=3) , where device is device returned bythe above list"

type(mic)
with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something! and press enter")
    audio = r.listen(source)
 r.recognize_google(audio)














