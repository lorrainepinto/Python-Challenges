"""tell player how much he/she has to wait, press enter to start end"""
import random,time

wait_time = random.randint(3,9)
s = "Press enter to start, stop after {} seconds\n".format(wait_time)
_=input(s)
start = time.time()
_=input()
stop = time.time()
print("Your time is {}\nYou were {} seconds late/early".format(stop-start,abs(stop-start-wait_time)) )