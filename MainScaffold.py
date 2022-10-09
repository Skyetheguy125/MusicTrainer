"""
This is a scaffold main script for running GUI threads alongside scaffolded SignalProcessor values.
"""
import threading
from SignalProcessorScaffold import SigProcessorScaffold as sp

class ProtectedBuffer:
	"""
	Wraps a buffer variable for inter-thread communication and a mutex
	"""
	def __init__(self):
		self._buffer = float()
		self._lock = threading.Lock()
	
	def get(self):
		"""
		returns current value in buffer.
		If lock is acquired, waits for it to be released.
		"""
		self._lock.acquire()
		ret = self._buffer
		self._lock.release()
		return ret
	
	def set(self,value):
		"""
		value - new value for the buffer.
		If lock is acquired, waits for it to be released.
		"""
		self._lock.acquire()
		self._buffer = value
		self._lock.release()

#Construct global ProtectedBuffer to use for inter-thread communication
buffer = ProtectedBuffer()

#Function for the signal thread; simulates the signal processor
def signal_thread():
	sig = sp()
	while True:	#Production code and later testing need to add a way of breaking out of this loop
		buffer.set(sig.wait_and_read())

#Fuction for the front-end thread; consumes output from the signal thread
def main():
	#current function is entierly a placeholder
	while True: #Actual testing main function needs to have a way to exit
		print(buffer.get())

if __name__=="__main__":
	#construct the thread objects
	t1 = threading.Thread(target=signal_thread)
	t2 = threading.Thread(target=main)

	#start threads
	t1.start()
	t2.start()

	#wait for threads to end
	#placeholder functions currently do not terminate, but ones used in testing should
	t1.join()
	t2.join()