# Viral streamer short (stil iz RULES.md v2): streamer GORE 50%, igra DOLJE 50%,
# 1 rijec Impact na spoju, pop animacija, punch-zoom + shake + flash + boom na glasnim momentima.
# Usage: python3 viral_short.py SRC START END CAM(x:y:w:h) GAME(x:y:w:h) OUT.mp4
import sys, subprocess, numpy as np, os, re
from faster_whisper import WhisperModel

src, S, E, cam, game, out = sys.argv[1:7]
S, E = float(S), float(E); D = E - S
FF = subprocess.run(["brew", "--prefix", "ffmpeg-full"], capture_output=True, text=True).stdout.strip() + "/bin/ffmpeg"
if not os.path.exists(FF): FF = "ffmpeg"
work = os.path.splitext(out)[0] + "_work"; os.makedirs(work, exist_ok=True)

# audio + loudness peaks (punch momenti)
pcm = subprocess.run([FF, "-v", "0", "-ss", str(S), "-t", str(D), "-i", src, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
win = 1600  # 0.1 s
rms = np.array([np.sqrt(np.mean(a[i:i+win]**2)) for i in range(0, len(a) - win, win)])
thr = np.percentile(rms, 88); peaks = []
for i in np.argsort(-rms):
    t = i * 0.1
    if rms[i] < thr: break
    if all(abs(t - p) > 1.6 for p in peaks): peaks.append(t)
peaks = sorted(peaks)[:12]

# titlovi: 1 rijec, pop, boja po glasnoci / tipu rijeci
words = [w for s in WhisperModel("small", compute_type="int8").transcribe(a, word_timestamps=True)[0] for w in s.words]
SWEAR = re.compile(r"(fuck|shit|damn|bitch|hell|ass)", re.I)
HYPE = {"GOD", "WHAT", "NO", "YES", "BRO", "GTA", "SIX", "6", "WAIT", "NAH", "WHY", "XBOX", "PLAYSTATION", "KFC", "KEANU", "REEVES", "LIT"}
def tt(x): return f"{int(x//3600)}:{int(x%3600//60):02}:{x%60:05.2f}"
ev = []
for i, w in enumerate(words):
    txt = re.sub(r"[^\w'?!]", "", w.word).upper()
    if not txt: continue
    if SWEAR.search(txt): txt = txt[0] + "*" * (len(txt) - 1); col = "&HFF00B4&"  # ljubicasta
    elif txt.strip("?!") in HYPE or any(abs(w.start - p) < 0.35 for p in peaks): col = "&H00D4FF&"  # zuta
    else: col = "&HFFFFFF&"
    end = max(w.end, w.start + 0.25)
    if i + 1 < len(words): end = min(end + 0.15, words[i+1].start)
    ev.append(f"Dialogue: 0,{tt(w.start)},{tt(end)},W,,0,0,0,,{{\\pos(540,960)\\c{col}\\fscx135\\fscy135\\t(0,90,\\fscx100\\fscy100)}}{txt}")
ass = f"""[Script Info]
PlayResX: 1080
PlayResY: 1920
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: W,Impact,112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,1,0,1,9,4,5,0,0,0,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
""" + "\n".join(ev) + "\n"
open(f"{work}/c.ass", "w").write(ass)

# zoom/shake/flash izrazi
Z = "+".join(f"0.16*exp(-6*(t-{p:.2f}))*gte(t,{p:.2f})" for p in peaks) or "0"
SH = "+".join(f"18*sin(t*90)*exp(-14*(t-{p:.2f}))*gte(t,{p:.2f})" for p in peaks) or "0"
FL = "+".join(f"0.22*exp(-16*(t-{p:.2f}))*gte(t,{p:.2f})" for p in peaks) or "0"
cx, cy, cw, ch = cam.split(":"); gx, gy, gw, gh = game.split(":")
fc = (f"[0:v]crop={cw}:{ch}:{cx}:{cy},scale=w='trunc(1080*(1.04+{Z})/2)*2':h='trunc(960*(1.04+{Z})/2)*2':eval=frame,"
      f"crop=1080:960:x='(iw-1080)/2+({SH})':y='(ih-960)/2',eq=brightness='{FL}':eval=frame[top];"
      f"[0:v]crop={gw}:{gh}:{gx}:{gy},scale=w='trunc(1080*(1+0.5*({Z}))/2)*2':h='trunc(960*(1+0.5*({Z}))/2)*2':eval=frame,crop=1080:960[bot];"
      f"[top][bot]vstack,fps=60,ass={work}/c.ass:fontsdir=/System/Library/Fonts/Supplemental[v];")
# boom SFX na punch momentima
boom = "+".join(f"gte(t,{p:.2f})*sin(2*PI*(55+80*exp(-12*(t-{p:.2f})))*(t-{p:.2f}))*exp(-7*(t-{p:.2f}))" for p in peaks) or "0"
fc += f"aevalsrc='0.55*({boom})':s=48000:d={D:.2f}[sfx];[0:a]aresample=48000[ma];[ma][sfx]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]"
subprocess.run([FF, "-nostdin", "-v", "error", "-y", "-ss", str(S), "-t", str(D), "-i", src, "-filter_complex", fc,
                "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print(out, "| punch:", [round(p, 1) for p in peaks])
