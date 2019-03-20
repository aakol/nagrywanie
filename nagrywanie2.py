import pyaudio
import wave
import string
import time
import struct

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
#RATE = 44100
RATE = 2000
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"
wyjscie = ()
p = pyaudio.PyAudio()

print("NAGRYWANIE ZA: 3")
time.sleep(1)

print("NAGRYWANIE ZA: 2")
time.sleep(1)

print("NAGRYWANIE ZA: 1")
time.sleep(1)
print("*************** NAGRYWANIE ******************")

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []
frames2 = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    #print(data)
    
    frames.append(data)
    data_int = struct.unpack(str(len(data))+'b',data)
    frames2.append(data_int)
    #print (data_int)
stream.stop_stream()
stream.close()
p.terminate()
print("KONIEC NAGRANIA")
print(len(frames),"LINI--PRZETWARZAM DANE")
#print(len(frames[0]))

print("ZAPIS DO PLIKU")
try:
    plik = open('pliczek1', 'w')
except:
    print("nie otworzyl sie!!!!")

  
k=0
#dodatni = True
#plikq = False   
    #print(len(frames2))
for i in range(len(frames2)):
        
    #print(len(frames2[i]))
 
    for k in frames2[i]:
        #plik.write(str(k)+",")
        
        if (k<0):
            k=k*-1
            plik.write(str(k)+",")
            #dodatni=False
        #else:
           # plik.write(str(k)+",")
                    
        #if (dodatni==False):
               # if (plikq == False):
                        
                   # k=k*-1
                   # plik.write(str(k)+",")
                    #plikq = True
                #elif (plikq == True):
                   # plik.write(str(k)+",")
                        
                        
                    
       # elif (dodatni==True):
             #   plik.write(str(k))
                
        
            
            
        
       
plik.close()
    

print("START ZAPISU DO PLIKU DZWIĘKOWEGO")
try:
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    #print(frames)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("KONIEC ZAPISU...OPERACJE ZAKONCZONE POMYSLNIE")
except:
    print("BŁĄD ZAPISU- nie bedzie pliku dzwiękowego")
print("******DZIĘKUJĘ ZA SKORZYSTANIE Z PROGRAMU MIŁEGO DNIA*****") 