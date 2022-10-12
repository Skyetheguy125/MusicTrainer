"""
This is a common utility for containing all music-specific mathematical operations.
Please include docstrings and use clear naming conventions, as other group members will likely be reüsing your methods.
"""
from numpy import log2, round
from math import floor

def closest_note(freq):
	"""
	freq - frequency in Hz
	returns an integer representing the closest reference note to freq as the number of semitones above A440
	"""
	#fn = f0*2**(n/12)
	n = int(round(12*log2(freq/440),0))
	return n

def cent_deviation(freq, note):
	"""
	freq - frequency in Hz
	The reference note as an integer number of semitones above A440
	Returns deviation between frequency and reference note in cents
	"""
	c = (12*log2(freq/440)-note)*100
	return c

def octave(note):
	"""
	note - reference note as an integer number of semitones above A440
	Returns the octave number of the note in Scientific Pitch Notation
	"""
	return floor((note+69)/12)-1

def note_lookup(note, *, oct=False):
	"""
	note - reference note as an integer number of semitones above A440
	oct (keyword-only) - Enable octave mode (disabled by default)
	returns the name of the note as a string. X-sharp -> X#, X-flat -> Xb
	"""
	LUT = ["A",	#0
		"A#/Bb",	#1
		"B",	#2
		"C",	#3
		"C#/Db",	#4
		"D",	#5
		"D#/Eb",	#6
		"E",	#7
		"F",	#8
		"F#/Gb",	#9
		"G",	#10
		"G#/Ab"]	#11
	if not oct:	
		return LUT[note%12]
	else:
		return LUT[note%12]+str(octave(note))

if __name__=="__main__":
	print("Music & Math")