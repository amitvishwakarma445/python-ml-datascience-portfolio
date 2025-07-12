## multi-Threading with threadpoolexecutor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number : {number}"

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

with ThreadPoolExecutor(max_workers=3) as executors:
    for num in numbers:
        executors.submit(print_number, num)
    
print("work is done")

### max_workers=3 → एक समय में 3 Threads कार्य कर सकते हैं।
### submit(print_number, num) → print_number() फ़ंक्शन को Threads में भेजता है।
