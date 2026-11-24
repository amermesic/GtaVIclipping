# Transkripcija sa vremenima. Usage: python3 tr.py video.mp4 > video.txt
import sys,subprocess,numpy as np
from faster_whisper import WhisperModel
pcm=subprocess.run(["ffmpeg","-v","0","-i",sys.argv[1],"-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout
a=np.frombuffer(pcm,np.int16).astype(np.float32)/32768
for s in WhisperModel("small",compute_type="int8").transcribe(a)[0]: print(f"{s.start:6.1f}-{s.end:6.1f} {s.text}")
