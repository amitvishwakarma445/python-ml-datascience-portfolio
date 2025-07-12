import multiprocessing
import time

def print_square():
    for i in [3,4,5,6,7]:
        time.sleep(1)
        print(f"square = {i*i}")


def print_cube():
    for i in [3,4,5,6,7]:
        time.sleep(1.5)
        print(f"cube = {i*i*i}")

## execution start from here
if __name__ == "__main__":

    ##create 2 process
    p1 = multiprocessing.Process(target=print_square)
    p2 = multiprocessing.Process(target=print_cube)

    t = time.time()

    ## start the process
    p1.start()
    p2.start()

    ## wait for the process to complete
    p1.join()
    p2.join()

    ## FINISHED TIME
    finished_time = time.time()-t
    print("total execution time = ",finished_time)
    