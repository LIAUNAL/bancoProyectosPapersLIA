"""Visual and functional QA of the Banco LIA 3D constellation tab (Playwright + system Chrome).

Usage (with the dashboard running, e.g. `bancoLIA ui --no-open`):
    uv run --with playwright --with pillow python tools/qa_constellation.py [http://localhost:8000/]
Screenshots go to a temporary folder printed at the end. Exit 1 if any check fails.
"""
import io, json, sys, tempfile
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000/"
OUT = Path(tempfile.mkdtemp(prefix="banco-lia-qa-"))
results = []

def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))

def bright_stats(png):
    im = Image.open(io.BytesIO(png)).convert("L")
    w, h = im.size
    px = im.load()
    xs = ys = n = 0
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            if px[x, y] > 90:
                xs += x; ys += y; n += 1
    tot = (w // 3 + 1) * (h // 3 + 1)
    return n / tot, (xs / n / w if n else -1), (ys / n / h if n else -1)

OVERLAP_JS = """(sel) => { const els=[...document.querySelectorAll(sel)].filter(e=>e.offsetParent!==null);
  const r=els.map(e=>[e.textContent.trim().slice(0,30), e.getBoundingClientRect()]); const bad=[];
  for(let i=0;i<r.length;i++)for(let j=i+1;j<r.length;j++){const a=r[i][1],b=r[j][1];
    if(a.left<b.right-1&&b.left<a.right-1&&a.top<b.bottom-1&&b.top<a.bottom-1) bad.push(r[i][0]+' x '+r[j][0]);}
  return bad; }"""
CLIP_JS = """(sel) => [...document.querySelectorAll(sel)].filter(e=>e.offsetParent!==null && (e.scrollWidth>e.clientWidth+1))
  .map(e=>e.tagName+':'+e.textContent.trim().slice(0,30))"""

def find_node(page, frame_el, step=14):
    box = frame_el.bounding_box()
    f = page.frames[1]
    sb = f.evaluate("() => { const r=document.getElementById('sky').getBoundingClientRect(); return [r.left,r.top,r.width,r.height]; }")
    ox, oy = box["x"] + sb[0], box["y"] + sb[1]
    for y in range(int(sb[3] * .2), int(sb[3] * .8), step):
        for x in range(int(sb[2] * .2), int(sb[2] * .8), step):
            page.mouse.move(ox + x, oy + y)
            vis = f.evaluate("() => { const t=document.querySelector('.atlas-tip'); return t && t.style.display==='block' ? t.textContent : null; }")
            if vis:
                return ox + x, oy + y, vis
    return None

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=False, args=["--window-position=4000,4000"])
    # The last case is a large display with the browser zoomed out to 50 %.
    for vw, vh, dpr in [(1440, 900, 1), (1280, 720, 1), (390, 844, 1), (5760, 3088, .5)]:
        tag = f"{vw}x{vh}@{dpr}"
        page = b.new_page(viewport={"width": vw, "height": vh}, device_scale_factor=dpr)
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: m.type == "error" and errors.append(m.text))
        page.goto(BASE + "#constelacion")
        page.wait_for_timeout(3500)
        frame_el = page.locator("#frame3d")
        f = page.frames[1]
        fb = frame_el.bounding_box()
        check(f"{tag} iframe visible in first screen", fb and fb["y"] < vh * .45 and fb["height"] > 400, f"y={fb and round(fb['y'])} h={fb and round(fb['height'])}")
        sb = f.evaluate("() => { const r=document.getElementById('sky').getBoundingClientRect(); return [r.left,r.top,r.width,r.height]; }")
        check(f"{tag} sky starts near top of frame", sb[1] < 200 if vw > 500 else sb[1] < 300, f"sky top={round(sb[1])} h={round(sb[3])}")
        check(f"{tag} sky taller than 330px", sb[3] > 330, str(round(sb[3])))
        check(f"{tag} sky not taller than 1.3x its width", sb[3] <= sb[2] * 1.3 or vw < 500, f"{round(sb[2])}x{round(sb[3])}")
        f.evaluate("() => viewer.rotate(false)")
        page.wait_for_timeout(400)
        shot = frame_el.screenshot()
        frac, cx, cy = bright_stats(f.locator("#sky").screenshot())
        check(f"{tag} graph drawn (bright pixels)", frac > 0.01, f"{frac:.3f}")
        check(f"{tag} graph centred", .3 < cx < .7 and .25 < cy < .75, f"cx={cx:.2f} cy={cy:.2f}")
        open(OUT / f"sky_{tag}.png", "wb").write(shot)
        labels = f.evaluate("() => document.querySelectorAll('.atlas-tip').length")
        tipvis = f.evaluate("() => { const t=document.querySelector('.atlas-tip'); return t.style.display + ' ' + t.textContent; }")
        check(f"{tag} no tooltip shown at rest", tipvis.split(" ")[0] in ("none", ""), tipvis)
        check(f"{tag} single tooltip element", labels == 1, str(labels))
        check(f"{tag} toolbar controls do not overlap", not f.evaluate(OVERLAP_JS, "#toolbar > *"), str(f.evaluate(OVERLAP_JS, "#toolbar > *")))
        check(f"{tag} toolbar text not clipped", not f.evaluate(CLIP_JS, "#toolbar button, #toolbar select"), str(f.evaluate(CLIP_JS, "#toolbar button, #toolbar select")))
        check(f"{tag} no horizontal scroll in frame", f.evaluate("() => document.documentElement.scrollWidth <= innerWidth + 1"))
        hit = find_node(page, frame_el)
        check(f"{tag} hover shows short label", hit and 3 < len(hit[2]) <= 90, hit and hit[2])
        if hit:
            tb = f.evaluate("() => { const t=document.querySelector('.atlas-tip').getBoundingClientRect(), s=document.getElementById('sky').getBoundingClientRect(); return [t.left-s.left, s.right-t.right, t.top-s.top, t.width]; }")
            check(f"{tag} hover label inside sky", min(tb[:3]) >= 0, str([round(v) for v in tb]))
            page.mouse.click(hit[0], hit[1])
            page.wait_for_timeout(600)
            side = f.evaluate("""() => { const s=document.getElementById('side'); const r=s.getBoundingClientRect();
              return {open:s.classList.contains('open'), h3:(s.querySelector('h3')||{}).textContent, top:s.querySelectorAll('ol li').length,
                      sel: selected, keep: selectedKeep && selectedKeep.size, w:r.width, h:r.height, sx:s.scrollWidth-s.clientWidth}; }""")
            check(f"{tag} click opens panel with main info", side["open"] and side["h3"], json.dumps(side, ensure_ascii=False)[:160])
            check(f"{tag} panel lists top 5", side["top"] == 5, str(side["top"]))
            skyh = f.evaluate("() => document.getElementById('sky').getBoundingClientRect().height")
            check(f"{tag} sky keeps >=250px with panel open", skyh >= 250, str(round(skyh)))
            check(f"{tag} click lights node + connections", side["keep"] and side["keep"] > 9, str(side["keep"]))
            check(f"{tag} panel has no horizontal overflow", side["sx"] <= 1, str(side["sx"]))
            check(f"{tag} panel sections do not overlap", not f.evaluate(OVERLAP_JS, "#side h3, #side h4, #side p, #side li"), "")
            page.screenshot(path=OUT / f"selected_{tag}.png")
            # related item navigation
            f.locator("#side ol li button").first.click()
            page.wait_for_timeout(1500)
            sel2 = f.evaluate("() => selected")
            check(f"{tag} top-5 entry selects that system", sel2 and sel2.endswith(".sun") and sel2 != side["sel"], str(sel2))
            page.keyboard.press("Escape")
            check(f"{tag} Escape closes panel", not f.evaluate("() => document.getElementById('side').classList.contains('open')"))
        # controls
        f.locator("#autorotate").click(); on1 = f.evaluate("() => viewer.rotating()")
        f.locator("#autorotate").click(); on2 = f.evaluate("() => viewer.rotating()")
        check(f"{tag} rotation toggles", on1 != on2, f"{on1}->{on2}")
        f.locator("#grouplayout").click(); page.wait_for_timeout(1500)
        check(f"{tag} group layout on", f.evaluate("() => viewer.layout()") == "groups")
        page.screenshot(path=OUT / f"groups_{tag}.png")
        f.locator("#grouplayout").click(); page.wait_for_timeout(1500)
        check(f"{tag} group layout off", f.evaluate("() => viewer.layout()") == "sky")
        f.select_option("#famselect", index=2)
        check(f"{tag} cluster filter applies", f.evaluate("() => activeFam") is not None)
        f.fill("#find", "A060"); f.press("#find", "Enter"); page.wait_for_timeout(300)
        check(f"{tag} search selects A060", f.evaluate("() => selected") == "A060.sun")
        f.locator("#zoomreset").click()
        check(f"{tag} reset clears selection and filter", f.evaluate("() => selected === null && activeFam === null"))
        for bid in ["zoomin", "zoomout", "spinleft", "spinright", "tiltup", "tiltdown"]:
            f.locator("#" + bid).click()
        check(f"{tag} no JS errors", not errors, "; ".join(errors)[:200])
        page.close()
    b.close()

fails = [r for r in results if not r[1]]
for name, ok, detail in results:
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
print(f"\n{len(results) - len(fails)}/{len(results)} passed · screenshots in {OUT}")
sys.exit(1 if fails else 0)
