#!/bin/bash
# Usage: find_moments.sh URL  -> top 15 najglasnijih trenutaka (vrisak/smijeh) kao kandidati
set -e; mkdir -p work
yt-dlp -q -f ba -x --audio-format wav -o "work/a.%(ext)s" "$1"
ffmpeg -v error -i work/a.wav -af "astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=work/rms.txt" -f null - 
python3 - <<'P'
import re
ts=[];cur=None
for l in open("work/rms.txt"):
    m=re.search(r"pts_time:([\d.]+)",l)
    if m: cur=float(m.group(1))
    m=re.search(r"RMS_level=(-?[\d.]+)",l)
    if m and cur is not None: ts.append((float(m.group(1)),cur))
ts.sort(reverse=True); picked=[]
for v,t in ts:
    if all(abs(t-p)>45 for p in picked): picked.append(t)
    if len(picked)==15: break
for t in sorted(picked): print(f"{int(t//3600):02}:{int(t%3600//60):02}:{int(t%60):02}  -> klip od {max(0,t-15):.0f}s do {t+15:.0f}s")
P
