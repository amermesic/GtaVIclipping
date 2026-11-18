import subprocess, os, textwrap
from concurrent.futures import ThreadPoolExecutor
K="work/kai/src.mp4"; S="work/speed/src.mp4"; KL="work/live/kai_a.mp4"; TL="work/live/tgg.mp4"
KC="510:280:900:800"; KG="420:60:1080:960"; KT="40:425:250:222"; KG2="420:60:792:960"; SC="40:430:640:569"; SG="905:20:770:684"
LC="0:432:392:222"; LG="440:0:890:1080"; TC="18:275:211:210"; TG="500:0:593:720"
# (src,start,end,cam,game,out,gs,layout,hook)
J=[
(S,113,150,SC,SG,"s_keanu_kfc","-",1,"SPEED PAUSED THE GTA 6 TRAILER AND FOUND *KFC*"),
(K,344.5,402.5,KC,KG,"k_school_laptop","46",1,"KAI’S FRIENDS *HACKED* THE SCHOOL LAPTOP TO PLAY GTA"),
(S,186,224.3,SC,SG,"s_xbox","-",1,"WHY SPEED WILL *NEVER* PLAY GTA 6 ON XBOX"),
(K,429,471.5,KC,KG,"k_lizard_squad","60",1,"THE DAY HACKERS MADE EVERYONE A *BILLIONAIRE* IN GTA 5"),
(S,66,108.5,SC,SG,"s_who_is_that_workout","-",1,"SPEED FOUND OUT YOU CAN *WORK OUT* IN GTA 6"),
(K,237.5,279.5,KC,KG,"k_vice_city","50",1,"KAI *NEVER* PLAYED THE GTA STORY"),
(S,0,50,SC,SG,"s_trailer_start","-",1,"SPEED’S *REAL* REACTION TO THE FINAL GTA 6 TRAILER"),
(K,194,223.5,KC,KG,"p1","100",1,"KAI WILL PLAY *EVERY GTA* BEFORE GTA 6"),
(K,497.5,524.3,KC,KG,"p2","130",1,"KAI WILL PLAY *EVERY GTA* BEFORE GTA 6"),
(K,23.9,44,KT,KG2,"p3","-",2,"KAI WAS *SCARED* TO WATCH THE GTA 6 TRAILER"),
(K,127.5,146,KT,KG2,"p4","-",2,"KAI WAS *SCARED* TO WATCH THE GTA 6 TRAILER"),
(KL,384,443,LC,LG,"live1_kai_cant_steal","-",2,"KAI CAN’T EVEN *STEAL* A CAR IN GTA 6"),
(KL,1170,1230,LC,LG,"live2_kai_first_fight","-",2,"KAI’S *FIRST FIGHT* IN GTA 6 GOES WRONG"),
(KL,1350,1410,LC,LG,"live3_kai_npc_chase","-",2,"GTA 6 NPCS *CHASE* KAI FOR NO REASON"),
(TL,425,485,TC,TG,"live4_tgg_dive","-",2,"THIS GTA 6 DIVE TOUR GOES *WRONG*"),
(TL,556,612,TC,TG,"live5_tgg_treasure","-",2,"GTA 6’S *WEIRDEST* TREASURE HUNTER"),
]
def wrap(h):
    plain=h.replace("*",""); 
    lines=textwrap.wrap(plain,26); 
    # vrati *..* oznake: wrap po rijecima originala
    words=h.split(); out=[];cur=""
    for w in words:
        if len(cur.replace("*",""))+len(w.replace("*",""))+1>21 and cur: out.append(cur);cur=w
        else: cur=(cur+" "+w).strip()
    out.append(cur); return "\\N".join(out)
def run(j):
    src,s,e,c,g,o,gs,lay,h=j
    env=dict(os.environ); 
    if lay==2: env["LAYOUT"]="2"
    r=subprocess.run(["python3","scripts/viral_short.py",src,str(s),str(e),c,g,f"out/v4/{o}.mp4",gs,wrap(h)],env=env,capture_output=True,text=True)
    return o,r.returncode,r.stderr[-200:]
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run,J): print(r,flush=True)
def cat2(a,b,o):
    subprocess.run(["ffmpeg","-nostdin","-v","error","-y","-i",f"out/v4/{a}.mp4","-i",f"out/v4/{b}.mp4","-filter_complex","[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]","-map","[v]","-map","[a]","-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-movflags","+faststart",f"out/v4/{o}.mp4"],check=True)
cat2("p1","p2","k_every_gta"); cat2("p3","p4","k_trailer_reaction")
for n in ["p1","p2","p3","p4"]: os.remove(f"out/v4/{n}.mp4")
subprocess.run("rm -rf out/v4/*_work",shell=True)
print("DONE")
