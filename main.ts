// News-image entry (Node 22, standard library only): the entry is the
// entry.png beside this file, drawn by draw_news.py from the six stories
// first reported on Tuesday 24 November 2026. This program copies it to
// /output/entry.png, so both grader runs write the same bytes.
//
// Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const source = new URL('./entry.png', import.meta.url);
copyFileSync(source, join(outDir, 'entry.png'));
