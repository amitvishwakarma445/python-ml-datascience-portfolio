### multiProcessing with processpool Executor

from concurrent.futures import ProcessPoolExecutor
import time

## create a function
def square(number):
    time.sleep(1)
    return f"square : {number*number}"

numbers = [1,2,3,4,5,6,7,8,9]

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)

    for result in results:
        print(result)