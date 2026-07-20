#!/usr/bin/env python3
"""Minimal CI check for the calculator suite.

Runs against a single-file HTML calculator (default: index.html).

Hard failures (exit 1) -- structural regressions only:
  - file missing
  - unbalanced HTML block tags
  - broken inline <script> JS (node --check, else brace-balance fallback)

Advisory items (non-blocking unless --strict): design-system compliance
  - external/network deps (fontshare/googleapis/cdn/http)
  - half-width '(mm)' (should be （毫米）)
  - 'mm²' (should be m²/ft² dual-units)
  - shared forest-green tokens present
  - base font >= 15px

Keep this script identical across all three repos. Flip to --strict in the
workflow once harmonization PRs are merged (see TASKS T8).
"""
import sys, re, os, shutil, subprocess, tempfile

BLOCK_TAGS = ["html", "head", "body", "style", "script", "div", "section",
              "form", "table", "main", "header", "footer"]
SHARED_VALUES = ["#2d5a4a", "#4a8c73", "#f4f1ec", "#2c2926", "#234839"]
LEGACY_VALUES = ["#01696f", "#0f172a", "#38bdf8", "#fbbf24"]  # teal / dark-slate / neon — pre-harmony


def main():
    args = sys.argv[1:]
    path = "index.html"
    strict = False
    for a in args:
        if a == "--strict":
            strict = True
        elif not a.startswith("-"):
            path = a

    fails, advisories = [], []

    if not os.path.exists(path):
        print(f"FAIL: {path} not found")
        sys.exit(1)
    src = open(path, encoding="utf-8").read()

    # --- advisory: design-system compliance ---
    ext = re.findall(r'https?://|@import|fontshare|googleapis|cdn\.', src, re.I)
    if ext:
        advisories.append("external/network references: " + ", ".join(sorted(set(ext))))
    if "(mm)" in src:
        advisories.append("half-width '(mm)' present (use （毫米）)")
    if "mm²" in src:
        advisories.append("'mm²' present (use m²/ft² dual-units)")
    # shared palette by VALUE (repos may name the CSS var differently)
    present = {v for v in SHARED_VALUES if v in src}
    if len(present) < len(SHARED_VALUES):
        advisories.append("shared forest-green palette incomplete: missing " +
                          ", ".join(v for v in SHARED_VALUES if v not in present))
    legacy = [v for v in LEGACY_VALUES if v in src]
    if legacy:
        advisories.append("legacy divergent color present (pre-harmony): " + ", ".join(legacy))
    m = re.search(r'font-size:\s*([0-9.]+)px', src)
    if m and float(m.group(1)) < 15:
        advisories.append("base font %spx < 15px" % m.group(1))

    # --- hard: HTML tag balance ---
    for t in BLOCK_TAGS:
        o = len(re.findall(r"<%s[ >\s]" % t, src))
        c = len(re.findall(r"</%s>" % t, src))
        if o != c:
            fails.append("tag imbalance <%s>: %d open / %d close" % (t, o, c))

    # --- hard: inline script JS parses ---
    scripts = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', src, re.S)
    if not scripts:
        fails.append("no inline <script> found")
    else:
        js = "\n".join(scripts)
        node = shutil.which("node")
        if node:
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tf:
                tf.write(js)
                tmp = tf.name
            r = subprocess.run([node, "--check", tmp], capture_output=True, text=True)
            os.unlink(tmp)
            if r.returncode != 0:
                fails.append("JS syntax error (node --check):\n" + (r.stderr.strip() or "unknown"))
        else:
            # fallback brace balance (no node available)
            depth = {"(": 0, "[": 0, "{": 0}
            close = {")": "(", "]": "[", "}": "{"}
            instr = False
            q = None
            for i, ch in enumerate(js):
                if instr:
                    if ch == q:
                        instr = False
                        q = None
                    continue
                if ch in "\"'`":
                    instr = True
                    q = ch
                    continue
                if ch in depth:
                    depth[ch] += 1
                elif ch in close:
                    if depth[close[ch]] <= 0:
                        fails.append("unbalanced '%s' near pos %d" % (ch, i))
                        break
                    depth[close[ch]] -= 1
            if not fails and any(depth.values()):
                fails.append("brace imbalance (fallback): " + str(depth))

    # --- report ---
    print("== CI check: %s ==" % path)
    print("[structural] %s" % ("PASS" if not fails else "FAIL"))
    for f in fails:
        print("  - " + f)
    print("[design-system] %s" % ("clean" if not advisories else "%d advisory item(s)" % len(advisories)))
    for a in advisories:
        print("  ~ " + a)

    if fails:
        print("RESULT: FAIL")
        sys.exit(1)
    if advisories and strict:
        print("RESULT: FAIL (strict)")
        sys.exit(1)
    print("RESULT: PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
