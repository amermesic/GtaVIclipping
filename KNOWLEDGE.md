# GTA Kingpin Clips - sve znanje (stanje 2026-11-24)

Kanal: **GTA Kingpin Clips** (@GTAKingpinClips), samo GTA 6 clipovi velikih streamera (Kai Cenat, IShowSpeed, xQc, TGG...). Amer objavljuje sam, nista se ne uploada automatski.

## Radni tok (od izvora do reela)
1. **Naci izvore**: YouTube pretraga (`scripts` -> ys.py scraper: `results?search_query=..&sp=CAISAhAB` = zadnji upload; `EgJAAQ%3D%3D` = live). Birati najsvjezije i najgledanije.
2. **Skinuti**: `yt-dlp --cookies-from-browser chrome -f "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[height<=1080]" --merge-output-format mp4`. Bez cookiesa YouTube vrati "Sign in to confirm you're not a bot" nakon puno skidanja. Cookies se koriste samo uz Amerovo izricito odobrenje (macOS Keychain prozor).
3. **Transkribovati**: faster-whisper small int8 (`tr.py`), pa citati transkript i birati momente (setup -> payoff, 30-70 s).
4. **Renderovati**: `scripts/viral_short.py` (LAYOUT=2) kroz `render_v5.py` / `render_v6.py` (posao = izvor, start, end, cam crop, game crop, ime, hook tekst).
5. **Provjera**: izvuci 1 kadar po videu i pogledaj (tekst gore, cam, gameplay, titlovi).
6. **Naslov + opis**: `Titel_und_Beschreibung.txt` (naslov, opis = isti naslov + 3 hashtaga).

## Layout (LAYOUT=2)
- 1080x1920. Cam 610 px visine gore (y=0), igra 1080x1310 ispod (y=610).
- Hook tekst: Impact 88, bijeli, outline 10, zuta kljucna rijec (`*RIJEC*`), pop animacija, pozicija (540,140), max 21 znak po redu, **bez emojija** (Impact ih ne renderuje).
- Titlovi: 1 rijec, Impact 112, na spoju (y=700), zuta za hype/glasne, ljubicasta za psovke (cenzurisano), pop animacija.
- Bez sintetickih SFX, samo originalni zvuk.
- Klip bez kamere (gameplay only): blur pozadina + igra u sredini + hook tekst gore + "GTA KINGPIN CLIPS" dolje (Reel15/16/29).

## Crop geometrija izvora (1920x1080)
| Izvor | Cam | Igra |
|---|---|---|
| IShowSpeed (VOD/live) | `0:460:390:240` | `600:60:790:960` |
| xQc VOD | `0:0:370:296` | `560:60:790:960` |
| xQc Clips (radio) | `0:540:360:300` | `700:60:790:960` |
| xQc QB clip | `0:474:390:312` | `600:60:790:960` |
| Kai live/VOD | `510:280:900:800` | `420:60:1080:960` |
| TGG | `18:275:211:210` | `500:0:593:720` |
Cam izvor je mali (~250-390 px) pa se mora povecati; zato je cam 610 px visine (manje povecanje = ostrije).

## Pravila izbora
- Klip mora imati kontekst: setup -> payoff, 30-60 s (15 s je premalo, "fali kontekst").
- Naslov kao konkurencija: `[Streamer] + glagol (Finds Out / Cries / Went WRONG) + konkretna stvar + emoji`. Opis = naslov + 3 hashtaga (`#streamer #gta6 #shorts`).
- Svaki klip: tekst gore u zoni kamere (ne u posebnoj traci), velik i upadljiv.
- Samo REELS folder (`out/REELS`), stari render obrisati kad se napravi novi.
- Imenovanje: Reel1, Reel2... po rednom broju.

## Windows / novi kompjuter
Skripte su pisane na Macu. Za Windows: ffmpeg iz PATH-a (ne `brew`), `fontsdir=C\\:/Windows/Fonts` u ass filteru (escape dvotacke), `$env:LAYOUT="2"` u PowerShellu, `python` umjesto `python3`. Svi naslovi su u TITLES.md.

## Sta je do sada napravljeno
Reel1-16 (Kai, TGG, Speed, bug kompilacija, 13 years), Reel17-24 (Speed VOD + xQc radio), Reel25-29 (Speed Lester, sad ending, xQc QB, radio oglas, streamer viralna slika). Mp4 fajlovi nisu u repou (.gitignore), samo skripte i znanje.

## Analiza kanala (2026-11-22)
- 24 videa, 0-5 pregleda po videu, 0 pretplatnika, kanal star par dana.
- Format je isti kao kod konkurencije; razlog nema pregleda: nova kanal bez publike, zasicena tema (svi klipuju iste streamere), reused content, previse objava odjednom.
- Preporuka: 2-3 videa dnevno, najjaci momenti, Instagram kao glavni kanal (tamo ide bolje nego TikTok/YouTube), pratiti "Gledano naspram preskoceno" i prosjecno gledanje u Studiju.
- Dupli upload (Bugs) obrisati.

## Rizici
- Reused content (Reel15, 16, 26, 29 su tudji edit/gameplay sa nasim tekstom).
- Nagi sadrzaj u igri (Reel19) = age-restriction. Radio sa eksplicitnim sadrzajem izbjegavati.
- Pravila platforme: nista se ne uploada automatski, lozinke se ne unose.
