# YouTube pretraga bez API-ja. Usage: python3 ys.py "GTA 6 Kai Cenat" "CAISAhAB"
# sp: CAISAhAB = zadnji upload, EgJAAQ%3D%3D = live, EgIQAQ%3D%3D = samo videi
import sys,json,re,subprocess,urllib.parse
q,sp=sys.argv[1],sys.argv[2]
h=subprocess.run(["curl","-s","-A","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36","-H","Accept-Language: en","https://www.youtube.com/results?search_query="+urllib.parse.quote(q)+"&sp="+sp],capture_output=True,text=True).stdout
m=re.search(r'var ytInitialData = (\{.*?\});</script>',h)
d=json.loads(m.group(1))
def walk(o):
    if isinstance(o,dict):
        if 'videoRenderer' in o: yield o['videoRenderer']
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
g=lambda r,k:(r.get(k,{}).get('simpleText') or ''.join(x['text'] for x in r.get(k,{}).get('runs',[])))
for r in walk(d):
    print(r['videoId'],'|',g(r,'ownerText')[:25],'|',g(r,'title')[:70],'|',g(r,'publishedTimeText'),'|',g(r,'lengthText') or 'LIVE','|',g(r,'viewCountText')[:22])
