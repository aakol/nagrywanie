import pyaudio
import wave
import struct
import string
import random


CHUNK = 1024

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
wyjscie = ()
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()
print(len(frames),"START")
#print(frames[0])
danesy = []
im = 0.01
m = 0
z=0
for j in range(len(frames)):
    
    danesy=frames[j]
    #print(len(danesy))
    for i in range(10):
        im=im+0.01
        #print (im)
        
        try:
            while True:
                m=random.randint(0,4096)
                z=random.randint(0,4096)
                #if danesy[m]>5 or danesy[m]<25 :
                    #z=0.5
                    #break
                    
                    #m=random.randint(0,4096)
                #if danesy[m]>200:
                    #z=1
                break
            #print(len(danesy))
            #print(danesy[i])
            #print(danesy[m])
            wyjscie=wyjscie+((float(im),float(danesy[m]/100),float(0)),(float(im),float(0),float(danesy[z]/100)),)
        except:
            continue
#print(danesy[99])

plik = open('pliczek', 'w')
plik.writelines(str(wyjscie))
plik.close()

print(len(wyjscie),"KONIEC")
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()