from PIL import Image, ImageDraw, ImageFont

BLEU  = "#002C6A"
SABLE = "#F8D99B"
SABLE_FONCE = "#E0B96E"
BLANC = "#FFFFFF"

W, H   = 1200, 627
MARGIN = 72

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REG  = "/System/Library/Fonts/Supplemental/Arial.ttf"

ROOT = "/Users/macbookproi9/Desktop/SWT-AI-Agent/swt-marketing-team"
OUT  = f"{ROOT}/output/visuals/2026-07-20-linkedin-crm-surdimensionne.png"

img  = Image.new("RGB", (W, H), BLEU)
draw = ImageDraw.Draw(img)

# --- Bloc logo, en-tete haut gauche (acquis A1 de exemples.md) ---
logo = Image.open(f"{ROOT}/shared/assets/Color logo.png").convert("RGBA")
LOGO_H = 64
lw = round(logo.width * LOGO_H / logo.height)
logo = logo.resize((lw, LOGO_H), Image.LANCZOS)
img.paste(logo, (MARGIN, MARGIN), logo)

f_mark = ImageFont.truetype(BOLD, 27)
gap = lw // 2  # espacement = moitie de la largeur du monogramme (brand-kit § 3)
draw.text((MARGIN + lw + gap, MARGIN + LOGO_H / 2), "Sunwise Talents",
          font=f_mark, fill=BLANC, anchor="lm")

# --- Bloc titre, ancre en bas, compact (acquis A2 : deux niveaux) ---
f_small = ImageFont.truetype(REG, 40)
f_big   = ImageFont.truetype(BOLD, 96)

NBSP = " "   # espace insecable (la fine U+202F manque dans Arial) avant le « ? »
APOS = "’"   # apostrophe typographique
small_txt = f"Est-ce que l{APOS}outil peut le faire{NBSP}?"
big_txt   = "Mauvaise question."

# descente reelle de la grande ligne, pour que le jambage du « q »
# reste dans la zone de securite de 72 px
_, big_descent = f_big.getmetrics()
baseline_big = H - MARGIN - big_descent

asc_big = draw.textbbox((0, 0), big_txt, font=f_big, anchor="ls")[1]
top_big = baseline_big + asc_big

baseline_small = top_big - 30
asc_small = draw.textbbox((0, 0), small_txt, font=f_small, anchor="ls")[1]
top_small = baseline_small + asc_small

draw.text((MARGIN, baseline_big), big_txt, font=f_big, fill=SABLE, anchor="ls")
draw.text((MARGIN, baseline_small), small_txt, font=f_small, fill=BLANC, anchor="ls")

# --- Filet sable fonce, rattache au bloc titre ---
filet_y = top_small - 34
draw.line([(MARGIN, filet_y), (MARGIN + 96, filet_y)], fill=SABLE_FONCE, width=3)

img.save(OUT)
print("OK", OUT, img.size)
print("bas du jambage :", baseline_big + big_descent, "/ limite", H - MARGIN)
print("haut du filet  :", filet_y)
