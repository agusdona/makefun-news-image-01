# news-image-01 — Round 3: "Friday 13 November 2026"

make.fun bounty entry (program/v1): a newspaper front page picturing
the world's news in one picture — 28 stories, 6 continents, all
reported on Friday 13 November 2026.

## The image

1024x1024 PNG. 12 illustrated lead stories (numbered, region-tagged,
headline + deck), 16 more stories in the "ALSO ON FRIDAY 13 NOVEMBER"
list, and a sources footer. The 12 illustrations are flat editorial
panels; the page is composed deterministically from them.

## Run

```sh
python3 main.py
```

Writes the image to `/output/entry.png` (the grader provides `/output`;
no directories are created). Standard library only, no network,
deterministic: every run writes identical bytes.

## Stories

Lead stories (illustrated):

1. [US] FAA Grounds All Flights — Nationwide telecom failure cancels
   5,000 departures; officials confirm no attack.
2. [Middle East] Iran-US Radar Dispute — Tehran claims strike on
   Bahrain radar; US denies hit, reports two drones downed.
3. [Asia] Trump, Xi, Putin APEC Summit — Historic three-way talks
   confirmed for next week in Shenzhen, China.
4. [Science] SpaceX Starship Reaches Orbit — Flight 15 successful;
   26 Starlink satellites deployed.
5. [US] Tanker-Cruise Ship Collision — New Orleans collision; 32 in
   hospital, all passengers accounted for.
6. [Americas] Pope Leo XIV in Peru — 500,000 gather for papal Mass
   in Chiclayo.
7. [Finance] Nvidia Crisis — Stock dips below $4 trillion; CEO Huang
   resigns amid Senate summons.
8. [Europe] Kyiv Hospital Inferno — Russian drone strike sets
   facility ablaze; 30 evacuated.
9. [Europe] EU Ukraine Peace Push — Dublin summit picks UK, France,
   Germany, Italy, Poland.
10. [Middle East] Strike on Nasser Hospital — Khan Younis facility
    hit in Gaza; 6 fatalities.
11. [Asia] Assam Bus-Truck Collision — Fatal crash in India kills 24.
12. [Tech] Microsoft Outage Persists — Outlook and Teams largely
    inaccessible for second day.

Also on Friday 13 November:

13. Turkey and Qatar sign mutual defence pact.
14. Iran claims LNG tanker struck mine in Hormuz.
15. UN reports 340,000 displaced by Yemen conflict.
16. Moscow car bomb wounds ex-aide of Ukraine ex-PM.
17. PM Takaichi plans first China visit for APEC.
18. Pakistan army reports 74 militants killed in raids.
19. North Korea unveils first new national flag since 1948.
20. Building collapse near Nairobi kills 6.
21. Nigeria officially ends Ebola watch, zero new cases.
22. Suspected drones sighted over RAF Lakenheath.
23. US producer prices surge 6.5% over 12 months.
24. Lauren Boebert loses Colorado House seat.
25. Space Shuttle Endeavour displayed upright in LA.
26. U2 releases album featuring Dolly Parton's last vocal.
27. Pochettino officially named Manchester United manager.
28. Japan defeats South Korea 9-5 in Tokyo baseball.

Sources: AP, Reuters, AFP, Al Jazeera, BBC, CNN, Vatican News,
Space.com. Pictures are illustrations, not news photographs.
