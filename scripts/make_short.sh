#!/bin/bash
# Usage: make_short.sh URL START END "HOOK TEXT" [layout: full|split] [cam: x:y:w:h]
# Primjer: make_short.sh https://youtu.be/xyz 00:12:03 00:12:31 "SPEED CRASHED INTO A GATOR" split 1500:60:400:300
set -e
URL=$1; S=$2; E=$3; HOOK=$4; LAYOUT=${5:-full}; CAM=${6:-}
OUT=out; mkdir -p $OUT work; N=$(date +%s)
yt-dlp -q -f "bv*[height<=1080]+ba/b" --download-sections "*$S-$E" --force-keyframes-at-cuts -o "work/$N.%(ext)s" --merge-output-format mp4 "$URL"
IN=work/$N.mp4
# titlovi (faster-whisper: pip install faster-whisper)
python3 "$(dirname $0)/captions.py" "$IN" "work/$N.ass"
if [ "$LAYOUT" = split ] && [ -n "$CAM" ]; then
  IFS=: read cx cy cw ch <<< "$CAM"
  VF="[0:v]crop=$cw:$ch:$cx:$cy,scale=1080:720[cam];[0:v]crop=ih*9/16*1.2:ih,scale=1080:1200[g];[cam][g]vstack[v];[v]ass=work/$N.ass[o]"
else
  VF="[0:v]scale=-2:1920,crop=1080:1920,ass=work/$N.ass[o]"
fi
ffmpeg -y -v error -i $IN -filter_complex "$VF" -map "[o]" -map 0:a -c:v libx264 -crf 18 -preset fast -c:a aac -b:a 192k "$OUT/short_$N.mp4"
echo "$OUT/short_$N.mp4  | hook: $HOOK"
