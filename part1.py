import threading
import time
# Number of threads
num_threads=5
Lock = threading.Lock()
Expected = 1000000

# Class representing a thread that increments the counter
class CounterThread(threading.Thread):
    # Shared counter variable
    counter = 0
    def run(self):
        global Expected
        Lock.acquire()
        for _ in range(1000):
            i = CounterThread.counter
            for _ in range(1000):
                i += 1
            CounterThread.counter = i
        print(f'Expected: {Expected}')
        Expected += 1000000
        print(f'Fixed: {CounterThread.counter}')
        Lock.release()

# Create a list to hold the thread objects
threads =[]

start = time.time()
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
print("Counter:", CounterThread.counter)
print("Run time: %f"%(end -start))
