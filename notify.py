import winsound
import time
import sys

secs = int(sys.argv[1])
while True:
	winsound.PlaySound("pushup.wav",winsound.SND_FILENAME)
	time.sleep(secs)