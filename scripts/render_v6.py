import subprocess, os, sys
from concurrent.futures import ThreadPoolExecutor
M="work/p/"
SC="0:460:390:240"; SG="600:60:790:960"
XC="0:0:370:296"; XG="560:60:790:960"
RC="0:540:360:300"; RG="700:60:790:960"
QC="0:474:390:312"; QG="600:60:790:960"
SET=M+"setup.mp4"; END=M+"ending.mp4"; QB=M+"qb.mp4"; R3=M+"radio3.mp4"
def wrap(h):
    out=[];cur=""
    for w in h.split():
        if len(cur.replace("*",""))+len(w.replace("*",""))+1>21 and cur: out.append(cur);cur=w
        else: cur=(cur+" "+w).strip()
    out.append(cur); return "\\N".join(out)
J=[
(SET,40,70,SC,SG,"Reel25_Speed_Lester_50h","SPEED HAS BEEN UP *50 HOURS* AND CAN’T FIND LESTER"),
(END,132,200,SC,SG,"Reel26_Speed_sad_ending","SPEED’S REACTION TO GTA 6’S *SAD ENDING*"),
(QB,16,90,QC,QG,"Reel27_xQc_QB","XQC FOUND A FOOTBALL AND BECAME A *QB* IN GTA 6"),
(R3,163,200,RC,RG,"Reel28_xQc_crematory_ad","THIS GTA 6 RADIO AD IS *UNHINGED*"),
]
only=sys.argv[1:]
def run(j):
    src,s,e,c,g,o,h=j
    if only and not any(o.startswith(x) for x in only): return o,"skip",""
    env=dict(os.environ); env["LAYOUT"]="2"
    r=subprocess.run(["python3","scripts/viral_short.py",src,str(s),str(e),c,g,f"out/new2/{o}.mp4","-",wrap(h)],env=env,capture_output=True,text=True)
    return o,r.returncode,r.stderr[-200:]
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run,J): print(r,flush=True)
