import RPi.GPIO as GPIO
import time

dot=0.1
line=dot*3
word=line*3
CODE={'':'',"'":'.----.', '(':'-.--.-', ')':'-.--.-', ',':'--..--', '-':'-....-', '.':'.-.-.-', '/':'-..-.', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ':':'---...', ';':'-.-.-.', '?':'..--..', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '_':'..--.-', ' ': ' '}

def toMorse(txt):
	txt = txt.upper()
	morse = ""
	for x in xrange(0, len(txt)):
		morse += CODE[txt[x]]
		pass
	return morse
def transmitCode(morse):
	print morse
	char =""
	for x in xrange(0, len(morse)):
		if(morse[x]=="."):
			char = dot
		else:
			if(morse[x]=="-"):
				char = line;
			else:
				char = word
		print char
		sendCode(char)
		pass


def sendCode(t):
	if(t!=word):
		GPIO.output(port ,1)
		time.sleep(t)
		GPIO.oputput(port, 0)
	else:
		time.sleep(t)


txt = "Raspberrypi morsecodder"
transmitCode(toMorse(txt))
GPIO.cleanup()