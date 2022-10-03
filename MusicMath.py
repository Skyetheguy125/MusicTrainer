"""
This is a common utility for containing all music-specific mathematical operations.
Please include docstrings and use clear naming conventions, as other group members will likely be reüsing your methods.
"""
from numpy import log2, round

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

def note_lookup(note):
	"""
	note - reference note as an integer number of semitones above A440
	returns the name of the note as a string. X-sharp -> X#, X-flat -> Xb
	"""
	LUT = {
		0:	"A",
		1:	"A#/Bb",
		2:	"B",
		3:	"C",
		4:	"C#/Db",
		5:	"D",
		6:	"D#/Eb",
		7:	"E",
		8:	"F",
		9:	"F#/Gb",
		10:	"G",
		11:	"G#/Ab"
	}
	return LUT[note%12]

if __name__=="__main__":
	print("Music & Math")