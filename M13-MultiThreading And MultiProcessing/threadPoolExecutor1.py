## multi Threading with pool thread executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number : {number}"

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

with ThreadPoolExecutor(max_workers=3) as executors:
    results = executors.map(print_number, numbers)

### max_workers=3 → एक समय में 3 थ्रेड्स कार्य कर सकते हैं।

for result in results:
    print(result)