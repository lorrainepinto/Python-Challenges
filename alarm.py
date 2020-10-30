""" Create an alam and play sound and message"""

import time,multiprocessing
from playsound import playsound

p = multiprocessing.Process(target=playsound, args=("C:\\Users\\pinto\\Documents\\GitHub\\Python-Challenges\\alarm.wav",))
p.start()
input("press ENTER to stop playback")
p.terminate()
