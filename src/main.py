#!/usr/bin/env python

import re
import json
import rospy
import requests
import actionlib
import subprocess

from voice.msg import TextAction, TextGoal, TextResult

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_google_translate_token(text):

    TOKEN_SERVER_URL = "http://localhost:3000/"

    r = requests.get(TOKEN_SERVER_URL + text)

    if r.status_code == 200:
        return json.loads(r.text)['value']
    else:
        raise "Token server is down."

def play_mp3(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()

def say(text):

    response = requests.get('https://translate.google.com/translate_tts?ie=UTF-8&q=' + text + '&tl=en&total=' + str(len(text)) + '&idx=0&textlen=5&tk=' + get_google_translate_token(text) + '&client=t&prev=input', headers=headers)

    print('Downloading %s...' % (text))

    with open(str(hash(text)) +'.mp3', 'wb') as fo:

        for chunk in response.iter_content(4096):
            fo.write(chunk)

    play_mp3(str(hash(text)) + '.mp3')

def text_to_speech(goal):
    say(goal.text)
    server.set_succeeded(TextResult('I did it, look at me!'))

rospy.init_node('voice')
server = actionlib.SimpleActionServer('text_to_speech', TextAction, text_to_speech, False)

server.start()
rospy.spin()
