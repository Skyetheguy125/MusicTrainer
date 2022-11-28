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
	if freq > 0:
		n = int(round(12*log2(freq/440),0))
	else:
		n = -1
	return n

def cent_deviation(freq, note):
	"""
	freq - frequency in Hz
	The reference note as an integer number of semitones above A440
	Returns deviation between frequency and reference note in cents
	"""
	if freq > 0:
		c = (12*log2(freq/440)-note)*100
	else:
		c = -1
	return c

def octave(note):
	"""
	note - reference note as an integer number of semitones above A440
	Returns the octave number of the note in Scientific Pitch Notation
	"""
	return floor((note+69)/12)-1

def note_lookup(note, accid={}, *, oct=False):
	"""
	note - reference note as an integer number of semitones above A440
	accid - a dictionary specifying which name a note should use if it has two aliases. Entries of the form "<non-default alias>": True
	oct (keyword-only) - Enable octave mode (disabled by default)
	returns the name of the note as a string. X-sharp -> X#, X-flat -> Xb
	preference for default alias is no accidental > flat > sharp
	"""
	LUT = [
		"A",	#0
		"A-sharp" if accid.get("A-sharp") else "B-flat",	#1
		"C-flat" if accid.get("C-flat") else "B",	#2
		"C",	#3
		"C-sharp" if accid.get("C-sharp") else "D-flat",	#4
		"D",	#5
		"D-sharp" if accid.get("D-sharp") else "E-flat",	#6
		"F-flat" if accid.get("F-flat") else "E",	#7
		"F",	#8
		"F-sharp" if accid.get("F-sharp") else "G-flat",	#9
		"G",	#10
		"G-sharp" if accid.get("G-sharp") else "A-flat"]	#11
	
	if not oct:	
		return LUT[note%12]
	else:
		return LUT[note%12]+str(octave(note))

if __name__=="__main__":
	print("Music & Math")