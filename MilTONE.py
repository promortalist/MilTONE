from gtts import gTTS
import os
import sys
import re
#reload(sys)
#sys.setdefaultencoding('utf8')

def pentacostal(macaria):
   tts = gTTS(macaria, lang='en')
   tts.save("thus_spoke_ahriman.mp3")
   os.system("play thus_spoke_ahriman.mp3  speed 0.7 chorus 0.6 0.5 25 0.7 5 10 -t  ")


def pentacostal_pl(macaria):
  tts = gTTS(macaria, lang='pl')
  tts.save("thus_spoke_ahriman.mp3")
  os.system("play thus_spoke_ahriman.mp3  speed 0.7 chorus 0.6 0.5 25 0.7 5 10 -t  ")

def pentacostal2_pl(macaria,emotion):
  tts = gTTS(macaria, lang='pl')
  tts.save("thus_spoke_ahriman.mp3")
  os.system("sox thus_spoke_ahriman.mp3 ahriman.mp3 speed 0.7 chorus 0.6 0.5 25 0.7 5 10 -t")
  if (emotion == "sadness"):
   os.system("sox ahriman.mp3 -n stat 2>&1| grep Length | awk '{print$3}' | xargs -I{} sox rain.mp3 emotion.mp3 trim 0 {}")
  elif (emotion == "anger"):
   os.system("sox ahriman.mp3 -n stat 2>&1| grep Length | awk '{print$3}' | xargs -I{} sox storm.mp3 emotion.mp3 trim 0 {}")
  elif (emotion == "fear"):
   os.system("sox ahriman.mp3 -n stat 2>&1| grep Length | awk '{print$3}' | xargs -I{} sox windy.mp3 emotion.mp3 trim 0 {}")
  elif (emotion == "joy"):
   os.system("sox ahriman.mp3 -n stat 2>&1| grep Length | awk '{print$3}' | xargs -I{} sox ocean.mp3 emotion.mp3 trim 0 {}")
  elif (emotion == "surprise"):
   os.system("sox ahriman.mp3 -n stat 2>&1| grep Length | awk '{print$3}' | xargs -I{} sox rain.mp3 emotion.mp3 trim 0 {}")
  elif (emotion == "disgust"):
   os.system("sox ahriman.mp3 -n stat 2>&1| grep Length | awk '{print$3}' | xargs -I{} sox rain.mp3 emotion.mp3 trim 0 {}")
  else:
   print("Nierozpoznany parametr. Emocja neutralna.")
  os.system("ffmpeg -y -i ahriman.mp3 -i emotion.mp3 -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 ahriman2.mp3")
  os.system("play ahriman2.mp3")


def septuaginta_pl(macaria):
    milton = open('macaria','r')
    satan = milton.readlines()
    pure_satan = re.sub(r"('|\\n|;)","", satan2)
    tts = gTTS(pure_satan, lang='pl')
    tts.save("thus_spoke_ahriman.mp3")
    os.system("play thus_spoke_ahriman.mp3  speed 0.7 chorus 0.6 0.5 25 0.7 5 10 -t  ")

if __name__ == '__main__':
  pentacostal(macaria)
  septuaginta(macaria)
  pentacostal_pl(macaria)
  septuaginta_pl(macaria)

