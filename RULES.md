## UPDATE 2026-11-18 (Amer): HOOK-TEXT OBEN + KAMERA-QUALITAET
- Gore mali clickbait hook tekst (2 reda, Impact 60, bijelo, kljucna rijec zuta) = sta se desava + zasto gledati, npr. "KAI CAN'T EVEN *STEAL* A CAR IN GTA 6". Bez emojija (Impact ih ne prikazuje). Ovo PREPISUJE staro "nema naslova gore".
- Mala cam (<400 px sirine u izvoru): `LAYOUT=2` (cam 610 px visine + igra velika ispod). Velika cam (>=600 px): stari 50/50 layout. Skaliranje uvijek lanczos + hqdn3d + unsharp.
- Batch: `scripts/render_v4.py`. Fajlovi imenovani Reel1(kai), Reel2(streamer) u `out/REELS`.
- Naslov/opis kao kod viralnih: `[Streamer] + glagol (Finds Out/Reacts To/Went WRONG) + konkretna stvar + emoji`; opis = naslov + 3-4 hashtaga.

# >>> PRAVILA v2 (2026-11-17) — STREAMER KLIPOVI = OVO JE DEFAULT <<<
Izvor: 5 streamer shortsa sa 1,3M–3,2M views (Snickerly, KaiCenat_IsBack, iboclips, Zylok, Liutauras). Frameovi: `refs/c_*.jpg`.

**Brojke (refs):** 9–31 s, 60 fps, nova slika ~1,5 s. **ALI vazi KONTEKST pravilo ispod: 30–60 s sa cijelom pricom.**

## KONTEKST PRAVILA (Amer 2026-11-18) — OBAVEZNO, prije svega ostalog
1. **Duzina 30–60 s** (izuzetno 25 s ako je cijela prica unutra). 15 s = nista se ne desi = NE.
2. **Cijela prica: SETUP -> BUILD -> PAYOFF.** Klip pocinje recenicom koja uvodi temu
   ("In school, my friends hacked the school laptop..."), ne usred price. Gledalac bez ikakvog
   predznanja mora razumjeti o cemu se prica i zasto je smijesno/ludo.
3. **Zavrsava na payoffu** (punchline, reakcija, odgovor) — nikad usred recenice.
4. Prije sjecenja: puni transkript izvora (`work/<src>/transcript.txt`), oznaci start price i payoff.
5. Ako setup i payoff nisu jedan do drugog: 2 dijela spojena (jump cut), npr. najava + lista.
6. **Test "zasto postam ovo?"**: u jednoj recenici napisi sta se desava i zasto je zanimljivo.
   Ako ne mozes — klip se NE pravi.
7. Hook (prvi frame) i dalje najjaci moment/izjava, ali bez gubljenja konteksta.

## Layout
- **Streamer GORE 50% (1080x960), igra DOLJE 50% (1080x960).** Facecam je uvecan, lice je veliko i zauzima pola ekrana.
- NEMA naslova/boxa gore. Hook = najjaci vrisak/reakcija na **frame 1** (pocni klip usred reakcije). Naslov ide samo u YT title.
- Igra dolje zadrzava in-game titlove (mali bijeli, dno) – to je ok.

## Titlovi (najvaznije)
- **1 RIJEC** istovremeno, **Impact** (kondenzovani bold), ALL CAPS, ~110 px na 1080x1920.
- Pozicija: **tacno na spoju gornje i donje polovine (y=960), centrirano.**
- Bijelo + crni outline 9 px + sjena. Akcentne rijeci **zute `#FFD400`**, psovke **ljubicaste `#B400FF`** i cenzurisane `F***` / `SH*`.
- Akcije/zvukovi u zvjezdicama zelenom: `*SHOCKED*`, `*TRIPPING*`, `*3PM*`.
- Animacija: **pop** – rijec ulazi na 135% i u 90 ms pada na 100%. Bez fade-a.

## Pokret / "stalno se nesto desava"
- **Punch zoom** na lice na glasnim momentima, BLAG (+8%), samo gornja polovina. Bez shake/flash dok Amer ne odobri.
- Jump-cut: izbaci tisinu i "uhh", nikad > 1,5 s bez promjene.
- Opciono: neon/glow linija na spoju (Liutauras stil), motion blur na brzim rezovima.

## Zvuk
- SAMO original audio streamera. **NIKAD sinteticki/generisani SFX** (Amer: "random zvukovi", 2026-11-17). Pravi SFX samo ako Amer da fajlove.

## Izvor (bitno za kvalitet)
- Igra/trailer dolje mora biti CIST i jasan (center crop bez overlaya, chata, brojaca) – gledalac mora vidjeti na sta streamer reaguje.
- Najbolji izvor = streamerov VOD gdje je facecam velik. Mala kamera preko trailera = mutno lice.
- Age-restricted videi: ne koristimo Amerove cookies.

## Naslov
- `[Streamer] [glagol] [GTA 6 stvar]! 😭` – npr. "Kai Cenat Got Hyped For 6 Stars In GTA 6! 😭🔥", "Jynxzi Finds Out GTA VI is 200GB! 💀😭". Emoji 😭💀🔥 na kraju (u naslovu DA, za razliku od opisa).

## Alat
`python3 scripts/viral_short.py SRC START END CAM_x:y:w:h GAME_x:y:w:h out.mp4`
(CAM i GAME crop moraju biti omjer 9:8; punch/flash/boom automatski po glasnoci.)

---

# GTA VI Clipping — PRAVILA (citaj prije svakog klipa)

Izvor: analiza 6 referentnih shortsa (2026-11-17). Frame-stripovi u `refs/`.

## 1. Sta je radilo (brojke)
| Video | Kanal (subs) | Views | Duzina | Format |
|---|---|---|---|---|
| The GTA 6 Situation | Runtime Caffeine (5k) | **4.7M** | 59s | Drama/news, crna pozadina, motion-text, clanci |
| GTA 6 vs GTA 5 graphics | Captain GTA 6 (3k) | **6.9M** | 21s | Split-screen poredjenje 5 vs 6 |
| Don't make these mistakes day 1 | SeagullBro (84k) | 938k | 61s | Lista "3 greske", gameplay b-roll + VO |
| Your Morality Matters in GTA 6 | ABTW (9k) | 524k | 75s | Explainer + UI kartice (case file, citati) |
| How long to complete GTA 6 | Cervice (72) | 16k | 41s | Brojke + animirani bar chart |
| Jynxzi reacts (streamer clip) | Clip Vault (14) | 17k | 12s | Facecam gore / gameplay dolje |

**Zakljucak:** mali kanali (3k–5k subs) dobili 5–7M → algoritam gura TEMU, ne kanal. Najjace: **kontroverza/drama** i **vizuelno poredjenje 5 vs 6**.

## 2. Hook (prvih 1–2 s) — OBAVEZNO
- Prva recenica = cijela poenta + tenzija. Primjeri koji su radili:
  - "GTA 6 could be the first GTA game that's not a GTA game."
  - "Do not make these 3 mistakes on your first day in GTA 6."
  - "GTA 6 versus GTA 5 graphics." (+ odmah split-screen)
- Frame 1 = akcija + tekst na ekranu. Nikad logo/intro/crni ekran.
- Formule: "Do NOT…", "X is BROKEN", "Nobody noticed…", "GTA 6 tracks your…", "[Streamer] just found…", "This changes everything".

## 3. Titlovi (stil)
**Stil A – default (SeagullBro / Jynxzi):** 1–3 rijeci, word-by-word, centrirano (~45–55% visine).
- Font: **Arial Black** (Montserrat variable izlazi tanak u libass), ALL CAPS, 80 px; hook box gore bijeli 74 px prve 3.5 s na 1080x1920.
- Boja: bijela; **kljucna rijec zuta `#FFE600`** (svaka 2–3 rijec). Crni outline 6–8 px + mekana sjena.
- Za streamer klipove: zuta/zelena highlight na emotivnim rijecima (OH MY GOD, NO WAY).

**Stil B – Komika (Captain GTA 6):** 1 rijec, **Komika Axis/Bangers**, zuta `#FFE81A`, debeli crni outline, + zelena strelica `#22FF22` na kljucni momenat.

**Stil C – News motion (Runtime Caffeine / Cervice):** crna/tamna pozadina `#1E1E1E`, Montserrat Black Italic, crvena `#E03C3C` za drama rijeci ("IT GETS WORSE"), screenshot clanaka sa highlightom, GTA logoi, zvjezdice wanted-level. Brojke velike narandzaste `#FFA21A` gradient + bar chartovi.

Watermark/credit dolje: "Credits @kanal" ili "clip from twitch.tv/x" – siva 60% opacity.

## 4. Montaza
- Nova slika svakih **1–2 s** (b-roll mijenja se na svaku recenicu).
- Svaka recenica = vizual koji to doslovno pokazuje (broj → animirani broj, poredjenje → split).
- Duzina: **20–35 s** za clip/poredjenje, **55–60 s** za explainer. Loop: zadnja recenica se veze na prvu.
- Bez muzike preko VO (ili jedva cujna), SFX whoosh na rezove.
- Streamer layout 9:16: **facecam gore 35–40%**, gameplay dolje, naslov-box gore (bijeli box, crni tekst, "HE HIT EVERY SINGLE ONE").

## 5. Naslov / opis / tagovi
- Naslov: < 60 znakova, tvrdnja ili upozorenje, "GTA 6" na pocetku. Npr. `GTA 6 Versus GTA 5 graphics comparison`, `The GTA 6 Situation`, `Kai Cenat's FIRST 5 minutes in GTA 6`.
- Opis: red 1 = 1 recenica koja ponavlja hook; red 2 = credit (twitch/yt link streamera); pa `#gta6 #gtavi #shorts`. Bez emojija.
- Tagovi: gta 6, gta vi, grand theft auto 6, gta 6 gameplay, ime streamera, gta 6 vs gta 5, rockstar games.

## 6. Teme (prioritet za launch 19.11.2026)
1. **Streameri prvi put igraju** (Kai Cenat, IShowSpeed, xQc, Jynxzi, Caseoh, Adin Ross, Kick/Twitch) – reakcije, padovi, smijesni momenti, bugovi.
2. **GTA 5 vs GTA 6** (grafika, fizika, policija, NPC, voda, auti).
3. **"Stvari koje sada mozes a u GTA 5 nisi"** – 1 feature po shortu.
4. **Easter eggs / skriveni detalji / secreti** prvih dana.
5. **Greske/savjeti za prvi dan**, money glitch (bez varanja online), najbolji auto/oruzje.
6. Drama/news (review score, server down, cijena, PC verzija).

## 7. Monetizacija (iskreno)
- YPP: 1.000 subs + **10M Shorts views / 90 dana** (ili 4.000 h). Shorts RPM je nizak (~$0.03–0.10 / 1k views). 10M views ≈ $300–1.000.
- **Reused content**: cisti re-upload tudjeg strima = YouTube ODBIJA monetizaciju. Uvijek: vlastiti titlovi + hook tekst + rezanje + kontekst/komentar (VO ili tekst). Uvijek credit streameru.
- Brze pare od clipanja: **clipping kampanje** (Whop "Content Rewards", Clipping.net, streamerovi Discord clip programi) – placaju $1–3 / 1k views, i to direktno za Kai/Speed/Kick streamere. Postaj clipper tamo + objavi i na svom kanalu.
- Volumen: 3–6 shortsa dnevno prvih 14 dana, isti klip na YT + TikTok + IG Reels.
- Igra je Rockstar IP: gameplay clipovi OK (Rockstar to tolerise), ali bez leakova/pirata.

## 8. Workflow (Claude radi)
1. Amer posalje link (YT/Twitch/Kick VOD) ili Claude trazi trending (`agent-reach`, yt-dlp search "gta 6 kai cenat").
2. `scripts/find_moments.sh` – skini audio + titl, nadji vrhove glasnoce/smijeha/vriska → kandidati timestamps.
3. Claude bira 3–5 najboljih (hook u 1. sekundi!).
4. `scripts/make_short.sh URL START END "HOOK TEXT"` → 1080x1920, facecam/gameplay, titlovi stil A.
5. Claude QA: hook frame 1, titl sync, credit, duzina.
6. Amer objavljuje (Claude ne uploaduje bez potvrde).
