import subprocess, os, sys
from concurrent.futures import ThreadPoolExecutor
M="work/m/"; SP=M+"speed2.mp4"; XQ=M+"xqc.mp4"; RA=M+"radio1.mp4"; R2=M+"radio2.mp4"
SC="0:460:390:240"; SG="600:60:790:960"
XC="0:0:370:296"; XG="560:60:790:960"
RC="0:540:366:294"; RG="700:60:790:960"
def wrap(h):
    out=[];cur=""
    for w in h.split():
        if len(cur.replace("*",""))+len(w.replace("*",""))+1>21 and cur: out.append(cur);cur=w
        else: cur=(cur+" "+w).strip()
    out.append(cur); return "\\N".join(out)
J=[
(SP,0,40,SC,SG,"Reel17_Speed_GTA6_is_here","SPEED’S REACTION WHEN *GTA 6* FINALLY LOADS"),
(SP,253,308,SC,SG,"Reel18_Speed_first_robbery","SPEED’S *FIRST* ROBBERY IN GTA 6 GOES WRONG"),
(SP,486,535,SC,SG,"Reel19_Speed_yacht_rant","GTA 6 SHOWS YOU *THIS* IN THE FIRST 10 MINUTES"),
(SP,674,726,SC,SG,"Reel20_Speed_coca_cola_plane","GTA 6 MISSION: A PLANE DROPPING *COCA-COLA*"),
(SP,770,806,SC,SG,"Reel21_Speed_son","SPEED FOUND OUT HE HAS A *SON* IN GTA 6"),
(SP,859,893,SC,SG,"Reel22_Speed_crocodiles","GTA 6 HAS *CROCODILES* AND SPEED IS DONE"),
(SP,1572,1632,SC,SG,"Reel23_Speed_cant_fly","SPEED CAN’T *FLY* A PLANE IN GTA 6"),
(RA,24,96,RC,RG,"Reel24_xQc_radio_CTE","XQC CRIES LAUGHING AT THE GTA 6 *RADIO* HOST"),
]
only=sys.argv[1:]
def run(j):
    src,s,e,c,g,o,h=j
    if only and not any(o.startswith(x) for x in only): return o,"skip",""
    env=dict(os.environ); env["LAYOUT"]="2"
    r=subprocess.run(["python3","scripts/viral_short.py",src,str(s),str(e),c,g,f"out/new/{o}.mp4","-",wrap(h)],env=env,capture_output=True,text=True)
    return o,r.returncode,r.stderr[-200:]
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run,J): print(r,flush=True)
