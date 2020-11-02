import shutil
import string
import re
from gtts import gTTS
from moviepy.editor import *


fps = 24

#Getting the text and splitting into list to create different 
f = open('keywords2.txt','r')
keywords = f.read();

#Splitting to create a list of keywords. Each keyword is seperated using a comma.
keyword_list = keywords.split(',')
print(len(keyword_list))


fr = open('paras2.txt','r')
content = fr.read()

#Each description of the keyword is alreday in order and speerated by a colon.
sentences = content.split(':')
print("creating "+str(len(sentences))+" audio files ")
no_of_clips = len(keyword_list)

#Creation of Audio Files
for i in range(0,no_of_clips):
  #gtts - Google Text To Speech module accepts text, language and speed as arguments to generate text to speech audio files.
  tts = gTTS(text=sentences[i], lang='en', slow=False)
  #These audio files are saved in a folder named Audio.
  tts.save('./Audio'+'/'+str(i)+'.mp3')
  print ('\n',sentences[i],'\n')
  print ("created audio file no: "+ str(i+1))


#Declaration of all the lists to be used for clips of different types.
list_clip_text = []
list_clip_audio = []
list_clip_title = []
list_clip_video = []

#Setting a background clip.
background = ImageClip('./Pictures2/back.png').set_duration(0.1).set_fps(fps)
list_clip_video.append(background)

#no audio clip for the start of the video.
noaudio = AudioFileClip('./Audio/silent.mp3').subclip(0,0.1)
list_clip_audio.append(noaudio)

#Generating Video Clips which which then be combined into a video
for i in range (0, no_of_clips):
	#Audio files are fetched
	next_aclip = AudioFileClip('./Audio/'+str(i)+'.mp3')
	print("Audio Clip No "+str(i)+" is being appended")
	#Audio files are put into a list.
	list_clip_audio.append(next_aclip)
	print("Audio Clip No "+str(i)+" attached")

	#Title Text Clip is created to label the pictures.
	next_tclip_title = TextClip(keyword_list[i],font='Courier-Bold',fontsize=500,color='white',bg_color='black',stroke_width=30).set_pos('top').set_duration(next_aclip.duration).resize(height = 20)
	
	#Image clip with same duration as the audio clip to maintain synchronised transition between video clips
	img_clip = ImageClip('./Pictures2/'+str(i)+'.png').set_duration(next_aclip.duration).set_fps(24).set_pos('center').resize(height = 300)

	#All those image and text clips are added to list one by one.
	list_clip_video.append(img_clip)
	print("Video clip for "+keyword_list[i]+" generated");
	list_clip_title.append(next_tclip_title)

#joining those files
aclip = concatenate_audioclips(list_clip_audio)
vclip = concatenate_videoclips(list_clip_video)
titleclip = concatenate_videoclips(list_clip_title)

#Compbining and arranging all these clips
result = CompositeVideoClip([titleclip.set_position('top'),vclip.set_position('center')] ,size = (720,460)).set_audio(aclip)

result.resize(height = 1080)

#Writing the file into current directory
result.write_videofile('main.mp4',codec = "libx264",fps=fps)
#print("Video size: "+ result.size)





