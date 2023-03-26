import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import time
import sys


# Create engine
engine = pyttsx3.init('sapi5')

# Get the different voices available
voices = engine.getProperty('voices')
# print(voices)

# Set the voice of engine
engine.setProperty('voice', voices[0].id)


# A function to speak when audio input is given
def speak(audio_input):
	engine.say(audio_input)
	engine.runAndWait()


# A function whishes when I open
def wishMe():
	hour = int(datetime.datetime.now().hour)

	if hour >= 0 and hour < 12:
		speak('Good morning')
	elif hour >= 12 and hour <= 18:
		speak('Good afternoon')
	else:
		speak('Good evening')
	time_now = datetime.datetime.now().strftime('%H:%M:%S')
	speak(f'Now the time is {time_now}')


# Take audio as input and returns the string
def audio2string():
	mic = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		mic.pause_threshold = 1
		audio = mic.listen(source)

	try:
		print('Recognizing...')
		query = mic.recognize_google(audio, language='en-in')
		# print(f'User: {query}')
	except Exception as e:
		# print(e)
		print('Say that again please')
		return "None"

	return query


if __name__ == '__main__':
	speak('Hello, I am Jarvis, Mayura is my master.')
	speak('How may I help you?')
	wishMe()
	condition = True

	while condition:
		query = audio2string().lower()

		if 'quit' in query:
			condition = False
			break
		elif 'wait' in query:
			time_list = query.split(' ')
			wait_index = time_list.index('wait')
			time_sec = int(time_list[wait_index + 1])
			time.sleep(time_sec)

		if 'wikipedia' in query:
			speak('Searching in wikipedia...')
			query = query.replace('wikipedia', '')
			results = query.summary(query, sentences=2)
			speak('According to wikipedia')
			speak(results)
			# print(results)
		elif 'open youtube' in query:
			webbrowser.open('youtube.com')
		elif 'open stack overflow' in query:
			webbrowser.open('stackoverflow.com')
		elif 'open google' in query:
			webbrowser.open('google.com')
		elif 'the time' in query:
			time_now = datetime.datetime.now().strftime('%H:%M:%S')
			speak(f'Now the time is {time_now}')
		elif 'play music' in query:
			music_dir = 'Path to songs list'
			songs = os.listdir(music_dir)
			number = random.randint(0, len(songs) - 1)
		elif 'chat gpt' in query:
			webbrowser.open('https://chat.openai.com/chat')
		elif 'open jarvis location':
			os.startfile('C:\\Mayura\\Programming\\Projects\\Python')
		elif 'open windows explorer' in query:
			os.startfile('C:/')
		elif 'open' in query:
			name_idx = query.find('open') + 5
			query_list = query.split(' ')
			open_index = query_list.index('open')
			name = query_list[open_index + 1]
			webbrowser.open(f'{name}.com')
		