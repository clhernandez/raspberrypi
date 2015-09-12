import RPi.GPIO as GPIO
import time, sys

dot=0.2
line=dot*3
word=line*3
port=12
CODE={'':'',"'":'.----.', '(':'-.--.-', ')':'-.--.-', ',':'--..--', '-':'-....-', '.':'.-.-.-', '/':'-..-.', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ':':'---...', ';':'-.-.-.', '?':'..--..', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '_':'..--.-', ' ': ' '}
GPIO.setmode(GPIO.BOARD)
text=""

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
		sendCode(char)
		pass


def sendCode(t):
	if(t!=word):
		GPIO.output(port ,1)
		time.sleep(t)
		GPIO.output(port, 0)
		time.sleep(dot)
	else:
		time.sleep(word)

GPIO.setup(port, GPIO.OUT)
if(len(sys.argv)>1):
	for x in xrange(1, len(sys.argv)):
		text += sys.argv[x] +" "

	text = text[0:len(text)-1]
else:
	text = "Raspberrypi morsecodder"
transmitCode(toMorse(text))
GPIO.cleanup()
