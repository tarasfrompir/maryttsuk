#!/usr/bin/env python3

from os import path
import shutil # Подключаем модуль

#Подключаем модуль 
import os 

import speech_recognition as sr


# читаем текст книги
book = open('slovar_out.dic', 'r')
outdic = open('slovarsmal.txt', 'w')

i=0
for line in book.readlines():
    # blah-blah
    if i>6:
         outdic.write(line)
         i=0
    else:
        i=i+1

outdic.close()
        
