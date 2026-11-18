# Viral streamer short (BEZ sintetickih SFX - Amer 2026-11-17) (stil iz RULES.md v2): streamer GORE 50%, igra DOLJE 50%,
# 1 rijec Impact na spoju, pop animacija, punch-zoom + shake + flash + boom na glasnim momentima.
# Usage: python3 viral_short.py SRC START END CAM(x:y:w:h) GAME(x:y:w:h) OUT.mp4
import sys, subprocess, numpy as np, os, re
from faster_whisper import WhisperModel

src, S, E, cam, game, out = sys.argv[1:7]
GS = sys.argv[7] if len(sys.argv) > 7 and sys.argv[7] not in ("", "-") else None
HOOK = sys.argv[8] if len(sys.argv) > 8 else ""  # clickbait tekst gore (\\N = novi red; *RIJEC* = zuto)  # opc: igra dolje iz drugog trenutka (b-roll)
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
LAYOUT2 = os.environ.get("LAYOUT") == "2"; CAPY = 830 if LAYOUT2 else 960
SWEAR = re.compile(r"(fuck|shit|damn|bitch|hell|ass|nigg)", re.I)
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
    ev.append(f"Dialogue: 0,{tt(w.start)},{tt(end)},W,,0,0,0,,{{\\pos(540,{CAPY})\\c{col}\\fscx135\\fscy135\\t(0,90,\\fscx100\\fscy100)}}{txt}")
hk = re.sub(r"\*(.+?)\*", r"{\\c&H00D4FF&}\1{\\c&HFFFFFF&}", HOOK.replace("\\N", "\\N"))
if HOOK: ev.append(f"Dialogue: 0,0:00:00.00,{tt(D)},H,,0,0,0,,{{\\pos(540,{40 if LAYOUT2 else 150})\\an8}}{hk}")
ass = f"""[Script Info]
PlayResX: 1080
PlayResY: 1920
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: H,Impact,60,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,1,0,1,6,3,8,0,0,0,1
Style: W,Impact,112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,1,0,1,9,4,5,0,0,0,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
""" + "\n".join(ev) + "\n"
open(f"{work}/c.ass", "w").write(ass)

# zoom/shake/flash izrazi
Z = "+".join(f"0.08*exp(-5*(t-{p:.2f}))*gte(t,{p:.2f})" for p in peaks) or "0"
SH = "0" or "+".join(f"18*sin(t*90)*exp(-14*(t-{p:.2f}))*gte(t,{p:.2f})" for p in peaks) or "0"
FL = "0" or "+".join(f"0.22*exp(-16*(t-{p:.2f}))*gte(t,{p:.2f})" for p in peaks) or "0"
ZI = Z.replace("t,", "it,").replace("(t-", "(it-")
cx, cy, cw, ch = cam.split(":"); gx, gy, gw, gh = game.split(":")
if LAYOUT2:
    # cam 610px visine (manje povecanje = ostrije), igra velika ispod, hook gore
    fc = (f"[0:v]crop={cw}:{ch}:{cx}:{cy},hqdn3d=2:2:5:5,split[c1][c2];"
          f"[c1]scale=1080:610:force_original_aspect_ratio=increase:flags=bilinear,crop=1080:610,boxblur=30:5[cbg];"
          f"[c2]scale=-2:610:flags=lanczos,unsharp=5:5:0.9[cfg];[cbg][cfg]overlay=(W-w)/2:0[cam];"
          f"[{1 if GS else 0}:v]crop={gw}:{gh}:{gx}:{gy},hqdn3d=1:1:3:3,split[g1][g2];"
          f"[g1]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=40:5,eq=brightness=-0.3[bg];"
          f"[g2]scale=2160:2240:flags=lanczos,zoompan=z='1.0+{ZI}':d=1:x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':s=1080x1120:fps=60,unsharp=5:5:0.7[gm];"
          f"[bg][gm]overlay=0:800[b1];[b1][cam]overlay=0:190,fps=60,ass={work}/c.ass:fontsdir=/System/Library/Fonts/Supplemental[v];")
else:
    fc = (f"[0:v]crop={cw}:{ch}:{cx}:{cy},hqdn3d=2:2:5:5,scale=2160:1920:flags=lanczos,"
          f"zoompan=z='1.03+{ZI}':d=1:x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':s=1080x960:fps=60,unsharp=7:7:1.3:5:5:0.0[top];"
          f"[{1 if GS else 0}:v]crop={gw}:{gh}:{gx}:{gy},scale=1080:960:flags=lanczos,fps=60,unsharp=5:5:0.6[bot];"
          f"[top][bot]vstack,fps=60,ass={work}/c.ass:fontsdir=/System/Library/Fonts/Supplemental[v];")
fc += "[0:a]anull[a]"
subprocess.run([FF, "-nostdin", "-v", "error", "-y", "-ss", str(S), "-t", str(D), "-i", src] + (["-ss", GS, "-t", str(D), "-i", src] if GS else []) + ["-filter_complex", fc,
                "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print(out, "| punch:", [round(p, 1) for p in peaks])
