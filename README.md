# The World in One Day — 13 November 2026

**The entry image:** [`entry.png`](entry.png) — 1024 × 1024 px PNG, 481,506 bytes.
SHA-256 `5cb1649ebccdebe8d9fdcaaa6a6ac5bd018beb469161f9e5b7ce5ebd8f025234`.

## The image

A single newspaper front page, sized for a feed thumbnail but built to be read
like a broadsheet. Aged newsprint background, a black serif masthead across the
top reading **13 NOVEMBER 2026**, a thin red rule beneath it and the sub-masthead
**THE WORLD IN ONE DAY**. Under the flag sits a two-column, three-row grid of six
illustrated panels — each one a story that broke on 13 November 2026, each with a
red headline bar pinned to its foot, the eye running top-left to bottom-right.

1. **HORMUZ ON EDGE** — A tanker and a naval escort cut through the Strait of
   Hormuz while a great column of black smoke and fire rises from a strike on
   the far shore. Iran says it hit a US radar site in Bahrain; the Gulf is on
   edge again, and a fifth of the world's oil moves through the water in the
   frame.
2. **EU JOINS UKRAINE TALKS** — Around a long table, figures shake hands with the
   EU, Ukrainian, US and Russian flags above them — Zelensky meeting the US
   envoys with Europe brought in from the sidelines to a seat at the table: a
   Ukrainian drone's night strike on a Russian warship in the Gulf of Finland
   is the argument made in the meantime.
3. **MICROSOFT DOWN WORLDWIDE** — Three silhouetted operators under rows of
   monitors, each screen flashing a red warning, a broken cloud, an outage. The
   world's calendars, mailboxes replaying and cloud consoles all going dark at
   the same hour.
4. **NVIDIA CHIEF RESIGNS** — A vast processor chip on a plinth, and a figure
   walking out of the room with a packed box. The Nvidia CEO Huang, summoned by
   the US Senate Banking Committee, stepping down as the story of the day.
5. **POPE IN PERU** — The Pope in white under a sunburst, greeted by a crowd with
   raised arms and fluttering flags in Lima, the colonial tower and the Andes
   behind.
6. **SENATE LEADERSHIP FIGHT** — Two dark-suited figures facing off in front of
   the US Capitol, flags flanking them. The fight over who leads the US Senate,
   staged where the gavels are.

## Sources

All six stories were first reported on **13 November 2026**, drawn from:

- **BBC World**
- **Al Jazeera**
- **Just Security**
- **Open Chronicle**
- **SatRecon**
- **Zark News**

## How to run

Requires Node.js 22 (standard library only; the program does no network I/O).

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png  (directory must exist)
node main.ts                          # writes /output/entry.png (the default)
```

`main.ts` copies `entry.png` — the file sitting beside the script — to
`MAKEFUN_OUTPUT_DIR` (default `/output`) under the name `entry.png`, using
`copyFileSync` and `join`. It is byte-for-byte deterministic and never calls
`mkdir`/`mkdirSync`, so it works when the program's own directory is read-only.

## Verification performed

- Ran `MAKEFUN_OUTPUT_DIR=out node main.ts` twice, into two fresh `out/`
  directories. `sha256sum out/entry.png` was identical on both runs and equal to
  the source hash `5cb1649ebccdebe8d9fdcaaa6a6ac5bd018beb469161f9e5b7ce5ebd8f025234`.
- Read-only simulation: copied the repo files into a temp directory, `chmod`
  that directory read-only, pointed `MAKEFUN_OUTPUT_DIR` at a separate writable
  temp directory — exit code `0`, output hash unchanged.
- The `MAKEFUN_OUTPUT_DIR` fallback was changed to nullish coalescing (`??`)
  and re-verified with two fresh-dir runs: both outputs byte-identical and
  equal to the source hash above.
- Output PNG checked: `file` reports
  `PNG image data, 1024 x 1024, 8-bit colormap, non-interlaced`; 481,506 bytes
  (under 1 MiB).
- No `mkdir` / `mkdirSync` anywhere in `main.ts`; the only imports are
  `copyFileSync` from `node:fs` and `join` from `node:path` — nothing that
  touches the network.

## License

MIT — see [`LICENSE`](LICENSE). SPDX-License-Identifier: MIT.
