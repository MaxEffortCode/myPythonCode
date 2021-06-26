import pyautogui
import time
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def test():
	im1 = pyautogui.screenshot()
	pix1 = im1.getpixel((384,216))
	pix2 = im1.getpixel((384*2,216*2))
	pix3 = im1.getpixel((384*3,216*3))
	pix4 = im1.getpixel((384*4,216*4))
	pix5 = im1.getpixel(((384*5)-1,(216*5)-1))
	print(pix1,pix2,pix3,pix4,pix5)





#https://www.geeksforgeeks.org/python-speech-recognition-on-large-audio-files/


#TODO CREATE A FUNCTION THAT TAKES IN AUDIO AND MAKES A WAV FILE AND REWRITES OVER IT EVERY 30 SECONDS

#TODO MAKE SETNIFMENTAL ANALISIS ON WORDS
#OR MAYBE JUST CRAWN THROUGH GUINUSS TO DOWNLOAD LRYICS OF SONG
def silence_based_conversion(path): 

	song = AudioSegment.from_wav(path)
	fh = open("reconized.txt", "w+")

	chunks = split_on_silence(song, min_silence_len=2500, silence_thresh = -32) #for clear audio do 2500, -32
	print(chunks)

	try:
		os.mkdir('audio_chunks')
	except(FileExistsError):
		print("file exists ln 30")

	os.chdir('audio_chunks')

	i=0

	for chunk in chunks:


		chunk_silent = AudioSegment.silent(duration = 1000)
		audio_chunk = chunk_silent + chunk + chunk_silent
		
		print(f"saving chunk{i}.wav")
		print("saving chunk{0}.wav".format(i))
		
		audio_chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")
		filename = 'chunk' + str(i)+'.wav'
		print(f'Processing chunk {i}')
		
		file = filename

		r = sr.Recognizer()

		with sr.AudioFile(file) as source:
			audio_listened = r.listen(source) 

		try:
			rec = r.recognize_google(audio_listened)
			fh.write(rec+". ")

		except sr.UnknownValueError:
			print("Could not understand audio")

		except sr.RequestError as e:
			print("Could not request results. check your internet connection")

		i += 1

	os.chdir('..')

if __name__ == '__main__': 

	for x in range(0,100):
		test()
		time.sleep(.5)
	print('Enter the audio file path') 

	path = input()

	silence_based_conversion(path) 


  			

