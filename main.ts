#!/usr/bin/env -S node
/**
 * news-image-01 — "Sum up 13 November 2026 world news in one image"
 *
 * Copies the finished entry image (entry.png, 1024x1024, sitting next to
 * this script) to the make.fun output directory and names it entry.png.
 *
 *   MAKEFUN_OUTPUT_DIR=out node main.ts     # -> out/entry.png
 *   node main.ts                            # -> /output/entry.png
 *
 * Node 22, standard library only. No network access, no image processing,
 * no randomness: the same entry.png in always produces the same bytes out.
 * The program never creates directories — the output directory is expected
 * to exist already (the grader may run it from a read-only location).
 */

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const source = new URL('./entry.png', import.meta.url);
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const destination = join(outputDir, 'entry.png');

copyFileSync(source, destination);

console.log(`Copied entry.png -> ${destination}`);
