#!/usr/bin/env python3
"""Static checks for a strategy deck (references/deck-standard.md §8).

Usage:
    python3 check_deck.py deck.html

Prints PASS / FAIL / WARN per check; exit code 1 if any check fails. It checks what can be
checked without a browser: the cover, titles, footnotes, exhibit keys, leftover
placeholders, codes, emoji and inline source tags. Overflow is checked by render_deck.js;
whether a cold reader understands each slide is checked by the cold-reader agent.

Standard library only.
"""
import html
import re
import signal
import sys
from pathlib import Path

CODE = re.compile(r"\b[A-Z]{1,3}[0-9]{1,2}\b")
GPU_LIKE = re.compile(r"^((A|H|B|L|T|V|P|G|M|K)[0-9]{2,3}|L4|T4)$")  # A100, L4… are names
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⭕]")
CHART = re.compile(r'<svg\b|class="bars"|class="hb"')
results = []


def report(status, where, check, detail=""):
    results.append(status)
    print(f"{status:<5} {where:<10} {check}{(': ' + detail) if detail else ''}")


def text(fragment):
    fragment = re.sub(r"<(style|script)\b.*?</\1>", "", fragment, flags=re.S)
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def by_class(cls, fragment):
    """Text of the first element whose class list contains cls."""
    m = re.search(rf'<(\w+)\b[^>]*class="(?:[^"]*\s)?{cls}(?:\s[^"]*)?"[^>]*>(.*?)</\1>', fragment, re.S)
    return text(m.group(2)) if m else ""


def by_tag(tag, fragment):
    m = re.search(rf"<{tag}\b[^>]*>(.*?)</{tag}>", fragment, re.S)
    return text(m.group(1)) if m else ""


def codes(s):
    return sorted({c for c in CODE.findall(s) if not GPU_LIKE.match(c)})


def check_cover(cls, cover):
    if "cover" not in cls.split():
        report("FAIL", "slide 1", "cover", 'the first slide must be the cover (class "slide cover")')
        return
    q = by_class("q", cover)
    report("PASS" if "?" in q else "FAIL", "slide 1", "cover question", q[:90] or "missing (.q, phrased as a question)")
    for part, label in (("trigger", "why now"), ("product", "what the product is")):
        t = by_class(part, cover)
        report("PASS" if len(t.split()) >= 5 else "FAIL", "slide 1", f"cover {label}", t[:90] or f"missing (.{part})")
    found = codes(text(cover))
    if found:
        report("FAIL", "slide 1", "codes on cover", ", ".join(found))


def check_slide(where, body):
    h1 = by_tag("h1", body)
    n = len(h1.split())
    if not h1:
        report("FAIL", where, "action title", "missing <h1>")
    elif n > 20:
        report("FAIL", where, "title words", f"{n} (≤20): {h1[:80]}")
    elif n < 8:
        report("WARN", where, "title words", f"{n}: is it a full-sentence claim? {h1}")
    found = codes(h1 + " " + by_class("subhead", body))
    if found:
        report("FAIL", where, "codes in title", ", ".join(found))
    src = by_class("src", body)
    report("PASS" if src.startswith("Source:") else "FAIL", where, "footnote",
           "ok" if src.startswith("Source:") else "missing 'Source:' footnote (.foot .src)")
    if CHART.search(body):
        if 'class="exhibit-title"' not in body:
            report("FAIL", where, "exhibit title", "chart without .exhibit-title (what, unit, scale)")
        if 'class="how"' not in body:
            report("FAIL", where, "how to read", "scores, balls or charts need a .how line")
    core = re.sub(r'<div class="(?:tracker|foot)\b.*?</div>\s*(?:</div>)?', "", body, flags=re.S)
    words = len(text(core).split())
    if words > 260:
        report("WARN", where, "slide words", f"{words} without tracker and footnote (aim for 100–200)")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1]).read_text()
    slides = re.findall(r'<section\b[^>]*class="([^"]*\bslide\b[^"]*)"[^>]*>(.*?)</section>', src, re.S)
    if not slides:
        sys.exit('no <section class="slide"> found')
    check_cover(*slides[0])
    main_slides = 1
    for i, (cls, body) in enumerate(slides[1:], start=2):
        main_slides += by_class("tag", body) != "Backup"
        check_slide(f"slide {i}", body)

    visible = text(src)
    report("PASS" if 9 <= main_slides <= 16 else "WARN", "(deck)", "main slides",
           f"{main_slides} including the cover (aim for 8–15 plus the cover)")
    left = re.findall(r"<[^<>]{2,60}>", visible)
    report("PASS" if not left else "FAIL", "(deck)", "placeholders", ", ".join(left[:5]) if left else "none")
    for label, pat in (("emoji", EMOJI), ("inline source tags", re.compile(r"\[[A-Z]{1,2}\d+[^\]]*\]")),
                       ("Lens lines", re.compile(r"\bLens:"))):
        hits = pat.findall(visible)
        report("PASS" if not hits else "FAIL", "(deck)", label, ", ".join(hits[:5]) if hits else "none")

    fails = results.count("FAIL")
    print(f"\n{fails} failed · {results.count('WARN')} warnings · {results.count('PASS')} passed")
    print("Not checked here: overflow (render_deck.js), cold-reader understanding (agents/cold-reader.md).")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()
