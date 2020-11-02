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

#Getting the text and splitting into list to create different 
f = open('keywords.txt','r')
keywords = f.read();
keyword_list = keywords.split(',')
print(len(keyword_list))
fr = open('paras.txt','r')
content = fr.read()
sentences = content.split(':')
print("creating "+str(len(sentences))+" audio files ")
for i in range(0,3):
  tts = gTTS(text=sentences[i], lang='en', slow=False)
  tts.save('./Audio'+'/'+str(i)+'.mp3')
  print ('\n',sentences[i],'\n')
  print ("created "+ str(i)+ " audio file")


img_file_names = ['0.png','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg']


list_clip_text = []
list_clip_audio = []
list_clip_title = []
list_clip_video = []
no_images = len(img_file_names)
background = ImageClip('./Pictures/back.png').set_duration(0.1).set_fps(fps)
list_clip_video.append(background)
noaudio = AudioFileClip('./Audio/silent.mp3').subclip(0,0.1)
list_clip_audio.append(noaudio)

for i in range (0, 3):
	next_aclip = AudioFileClip('./Audio/'+str(i)+'.mp3')
	print("Audio Clip No "+str(i)+" is being appended")
	list_clip_audio.append(next_aclip)
	print("Audio Clip No "+str(i)+" attached")
	next_tclip = TextClip(sentences[i],font='Courier-Bold',fontsize=200,color='white',bg_color='black',stroke_width=30).set_pos('bottom').set_duration(next_aclip.duration)#.resize(width = 1080)
	next_tclip_title = TextClip(keyword_list[i],font='Courier-Bold',fontsize=500,color='white',bg_color='black',stroke_width=30).set_pos('top').set_duration(next_aclip.duration).resize(height = 20)
	#full_text = CompositeVideoClip([next_tclip_title,next_tclip])
	img_clip = ImageClip('./Pictures/'+img_file_names[i]).set_duration(next_aclip.duration).set_fps(24).set_pos('center').resize(height=100)
	#c1 = VideoClip([next_tclip]).set_pos('bottom')
	#c2 = VideoClip([next_tclip_title]).set_pos('top')
	#c3 = VideoClip([img_clip]).set_pos('center')
	#c = CompositeVideoClip(c1,c2,img_clip)

	list_clip_video.append(img_clip)
	print("Video clip for "+img_file_names[i]+" generated");
	list_clip_text.append(next_tclip)
	list_clip_title.append(next_tclip_title)
aclip = concatenate_audioclips(list_clip_audio)
vclip = concatenate_videoclips(list_clip_video)
tclip = concatenate_videoclips(list_clip_text).set_pos('bottom')
titleclip = concatenate_videoclips(list_clip_title).set_pos('top')
#inter_result = CompositeVideoClip([titleclip,vclip])
result = CompositeVideoClip([vclip.set_position('center'),titleclip.set_position('top')], size = (1920,1080)).set_audio(aclip)
#result.ipython_display(width = 480, fps = fps, maxduration= 3600)
#video_list,append(result)
#result.resize(height = 1080)
result.write_videofile('main.mp4',fps=fps)
#print("Video size: "+ result.size)





