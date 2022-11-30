"""
This is a scaffold main script for running GUI threads alongside scaffolded SignalProcessor values.
"""
import threading
from SignalProcessorScaffold import SigProcessorScaffold as sp
from FFT_Scaffold import FFT_Scaffold as FFT_sp

import tkinder.Windows.Interface as Interface

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
signal_buffer = ProtectedBuffer()
target_buffer = ProtectedBuffer()
kill_signal = ProtectedBuffer()
kill_signal.set(-1.0)

#Function for the signal thread; simulates the signal processor
def signal_thread():
	sig = FFT_sp()
	while kill_signal.get() < 0:
		signal_buffer.set(sig.wait_and_read())

def trainer_thread():
	target = sp(2000,(261.63,1046.5))
	while kill_signal.get() < 0:
		target_buffer.set(target.wait_and_read())

#Fuction for the front-end thread; consumes output from the signal thread
def main():
	Interface.create_welcome_window(signal_buffer,target_buffer)

if __name__=="__main__":
	#construct the thread object(s)
	t1 = threading.Thread(target=signal_thread)
	t2 = threading.Thread(target=trainer_thread)

	#start thread(s)
	t1.start()
	t2.start()

	#run UUT
	main()

	#after UUT returns, wait for threads to end
	kill_signal.set(1.0)
	t1.join()
	t2.join()