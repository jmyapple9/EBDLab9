import threading
import time
import random
# Number of threads
num_threads = 40
# Lock = threading.Lock()
semaphore_count = 40 # 20, 30
semaphore = threading.Semaphore(semaphore_count)

start = time.time()

# Class representing a thread that increments the counter
class CounterThread(threading.Thread):
    # Shared counter variable
    def run(self):
        semaphore.acquire()
        print(f'enter time: {time.time()-start}')
        parking_time = random.randint(0, 5)
        time.sleep(parking_time)

        print(f'leave time: {time.time()-start}')
        semaphore.release()


# Create a list to hold the thread objects
threads =[]

# Create and start the threads
for _ in range(num_threads):
    t = CounterThread()
    threads.append(t)
    t.start()

# Call the run() method of each thread
for t in threads:
    t.join()
end = time.time()

# Print the final value of the counter
print("Run time: %f"%(end -start))
