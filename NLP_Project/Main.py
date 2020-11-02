import os
import sys
import shutil
import getopt
import string
import re
from gtts import gTTS
from moviepy.editor import *
import numpy as np


fps = 24

#Getting the text and splitting into list to create different.
f = open('keywords.txt','r')
keywords = f.read();

#Each keyword is seperated using a comma.
keyword_list = keywords.split(',')
print(len(keyword_list))

fr = open('paras.txt','r')
content = fr.read()

#Each description of the keyword is alreday in order and speerated by a colon.
sentences = content.split(':')

#Creation of Audio Files

print("creating "+str(len(sentences))+" audio files ")
for i in range(0,6):
#gtts - Google Text To Speech module accepts text, language and speed as arguments to generate text to speech audio files.
  tts = gTTS(text=sentences[i], lang='en', slow=False)
#These audio files are saved in a folder named Audio.
  tts.save('./Audio'+'/'+str(i)+'.mp3')
  print ('\n',sentences[i],'\n')
  print ("created "+ str(i)+ " audio file")

#The images could not be fetched from the internet thus this is a list of names of images already downloaded.
img_file_names = ['0.png','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg']

#These lists contain the object which would then be combined to form a full video clip
list_clip_text = []
list_clip_audio = []
list_clip_title = []
list_clip_video = []
no_images = len(img_file_names)
background = ImageClip('./Pictures/back.jpg').set_duration(0.1).set_fps(fps)
list_clip_video.append(background)
noaudio = AudioFileClip('./Audio/silent.mp3').subclip(0,0.1)
list_clip_audio.append(noaudio)

for i in range (0, 6):
	#Fetching audio files.
	next_aclip = AudioFileClip('./Audio/'+str(i)+'.mp3')
	print("Audio Clip No "+str(i)+" is being appended")
	#Adding those files into the list.
	list_clip_audio.append(next_aclip)
	print("Audio Clip No "+str(i)+" attached")
	#TextClip creates a video clip with text only. 
	next_tclip = TextClip(sentences[i],font='Courier-Bold',fontsize=200,color='white',bg_color='black',stroke_width=30).set_pos('bottom').set_duration(next_aclip.duration).resize(width = 1080)
	next_tclip_title = TextClip(keyword_list[i],font='Courier-Bold',fontsize=200,color='white',bg_color='black',stroke_width=30).set_pos('top').set_duration(next_aclip.duration).resize(height=20)
	#full_text = CompositeVideoClip([next_tclip_title,next_tclip])
	#img_clip = ImageClip('./Pictures/'+img_file_names[i]).set_duration(next_aclip.duration).set_fps(fps).set_pos('center').crossfadein(0.5)
	#list_clip_video.append(img_clip)
	#print("Video clip for "+img+" generated");
	list_clip_text.append(next_tclip)
	list_clip_title.append(next_tclip_title)
aclip = concatenate_audioclips(list_clip_audio)
#vclip = concatenate_videoclips(list_clip_video).set_pos('center')
tclip = concatenate_videoclips(list_clip_text).set_pos('bottom')
titleclip = concatenate_videoclips(list_clip_title).set_pos('top')
result = CompositeVideoClip([titleclip,tclip]).set_audio(aclip)
#result.ipython_display(width = 480, fps = fps, maxduration= 3600)
#video_list,append(result)
#result.resize(height = 1080)
result.write_videofile('main.mp4',fps=fps)
#print("Video size: "+ result.size)





