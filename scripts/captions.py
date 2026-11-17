# Word-by-word ASS titlovi, stil A (bijelo + zuta keyword, crni outline). Usage: captions.py in.mp4 out.ass
import sys
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
segs, _ = WhisperModel("small", compute_type="int8").transcribe(src, word_timestamps=True)
words = [w for s in segs for w in s.words]
def t(x): return f"{int(x//3600)}:{int(x%3600//60):02}:{x%60:05.2f}"
hdr = """[Script Info]
PlayResX: 1080
PlayResY: 1920
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: A,Montserrat ExtraBold,86,&H00FFFFFF,&H0000E6FF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,7,3,5,60,60,0,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
L = []
for i in range(0, len(words), 2):
    g = words[i:i+2]
    txt = " ".join(("{\\c&H00E6FF&}" + w.word.strip().upper() + "{\\c&HFFFFFF&}") if (i//2) % 2 == 0 and j == len(g)-1 else w.word.strip().upper() for j, w in enumerate(g))
    L.append(f"Dialogue: 0,{t(g[0].start)},{t(g[-1].end)},A,,0,0,0,,{{\\fscx80\\fscy80\\t(0,80,\\fscx100\\fscy100)}}{txt}")
open(out, "w").write(hdr + "\n".join(L) + "\n")
