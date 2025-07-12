## now uExample 1

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(1)
        print(f"number = {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(1)
        print(f"letter = {letter}")

## calculate the total time to execute
t = time.time()

## create threads
thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_letter)

## start threads
thread1.start()
thread2.start()

## wait for the threads to complete
thread1.join()
thread2.join()

finished_time = time.time()-t
print(f"total time to execute = {finished_time}")