"""
TOK Logo Generator — drives Adobe Illustrator via COM automation.
Creates a professional vector logo with personality, saves as .ai, .png, and .svg.
"""
import win32com.client
import os
import time

LOGO_DIR = r"C:\Gab\work\Tiktok Managing Agency\logo"
OUTPUT_AI = os.path.join(LOGO_DIR, "TOK_Logo_v3.ai")
OUTPUT_PNG = os.path.join(LOGO_DIR, "TOK_Logo_v3.png")
OUTPUT_SVG = os.path.join(LOGO_DIR, "TOK_Logo_v3.svg")

def rgb(r, g, b):
    """Create an Illustrator RGBColor via COM."""
    color = win32com.client.Dispatch("Illustrator.RGBColor")
    color.Red = r
    color.Green = g
    color.Blue = b
    return color

def make_rect(doc, x, y, w, h, fill_color, stroke_color=None, stroke_width=0):
    rect = doc.PathItems.Rectangle(y, x, w, h)
    rect.Filled = True
    rect.FillColor = fill_color
    if stroke_color:
        rect.Stroked = True
        rect.StrokeColor = stroke_color
        rect.StrokeWidth = stroke_width
    else:
        rect.Stroked = False
    return rect

def make_line(doc, x1, y1, x2, y2, color, width=2):
    path = doc.PathItems.Add()
    p1 = path.PathPoints.Add()
    p1.Anchor = [x1, y1]
    p1.LeftDirection = [x1, y1]
    p1.RightDirection = [x1, y1]
    p2 = path.PathPoints.Add()
    p2.Anchor = [x2, y2]
    p2.LeftDirection = [x2, y2]
    p2.RightDirection = [x2, y2]
    path.Closed = False
    path.Filled = False
    path.Stroked = True
    path.StrokeColor = color
    path.StrokeWidth = width
    return path

def make_ellipse(doc, top, left, width, height, fill_color):
    ell = doc.PathItems.Ellipse(top, left, width, height)
    ell.Filled = True
    ell.FillColor = fill_color
    ell.Stroked = False
    return ell

def make_text(doc, text, x, y, size, fill_color, stroke_color=None, stroke_width=0, font_name="ArialBlack"):
    ti = doc.TextFrames.Add()
    ti.Contents = text
    ti.Position = [x, y]
    attr = ti.TextRange.CharacterAttributes
    attr.Size = size
    attr.FillColor = fill_color
    if stroke_color:
        attr.StrokeColor = stroke_color
        attr.StrokeWidth = stroke_width
    else:
        nc = win32com.client.Dispatch("Illustrator.NoColor")
        attr.StrokeColor = nc
    try:
        attr.TextFont = app.TextFonts.GetByName(font_name)
    except:
        pass
    return ti

def make_diamond(doc, cx, cy, radius, color, width=3):
    """Create a diamond shape using individual path points."""
    path = doc.PathItems.Add()
    # Use PathPoints API
    points = [
        (cx, cy + radius),
        (cx + radius, cy),
        (cx, cy - radius),
        (cx - radius, cy)
    ]
    for px, py in points:
        pp = path.PathPoints.Add()
        pp.Anchor = [px, py]
        pp.LeftDirection = [px, py]
        pp.RightDirection = [px, py]
    path.Closed = True
    path.Filled = False
    path.Stroked = True
    path.StrokeColor = color
    path.StrokeWidth = width
    return path

print("Starting Illustrator COM...")
# Use gencache for early binding — gives us proper type library with correct member names
app = win32com.client.gencache.EnsureDispatch("Illustrator.Application")
try:
    app.Visible = False
except:
    pass

print("Creating document...")
doc = app.Documents.Add(2, 600, 600)  # 2 = RGB color space

# Colors
print("Setting up colors...")
bg_color = rgb(10, 10, 15)
cyan = rgb(37, 244, 238)
pink = rgb(254, 44, 85)
white = rgb(255, 255, 255)
gold = rgb(255, 215, 0)
no_color = win32com.client.Dispatch("Illustrator.NoColor")

# === BACKGROUND ===
print("Creating background...")
make_rect(doc, 0, 0, 600, 600, bg_color)

# === DIAMOND BORDER ===
print("Creating diamond border...")
make_diamond(doc, 300, 300, 260, cyan, 3)
make_diamond(doc, 300, 300, 245, pink, 1)

# === CORNER ACCENTS ===
print("Creating corner accents...")
# Top-left
make_line(doc, 80, 80, 120, 80, cyan, 2)
make_line(doc, 80, 80, 80, 120, cyan, 2)
# Top-right
make_line(doc, 480, 80, 520, 80, pink, 2)
make_line(doc, 520, 80, 520, 120, pink, 2)
# Bottom-left
make_line(doc, 80, 480, 80, 520, pink, 2)
make_line(doc, 80, 520, 120, 520, pink, 2)
# Bottom-right
make_line(doc, 520, 480, 520, 520, cyan, 2)
make_line(doc, 480, 520, 520, 520, cyan, 2)

# === TIKTOK MUSIC NOTE ===
print("Creating TikTok music note...")
# Note head (pink shadow)
make_ellipse(doc, 215, 338, 30, 22, pink)
# Note head (cyan main)
make_ellipse(doc, 215, 335, 30, 22, cyan)

# Note stem (pink shadow)
stem_pink = doc.PathItems.Add()
sp1 = stem_pink.PathPoints.Add()
sp1.Anchor = [358, 200]; sp1.LeftDirection = [358, 200]; sp1.RightDirection = [358, 200]
sp2 = stem_pink.PathPoints.Add()
sp2.Anchor = [358, 135]; sp2.LeftDirection = [358, 135]; sp2.RightDirection = [358, 135]
stem_pink.Closed = False
stem_pink.Filled = False
stem_pink.Stroked = True
stem_pink.StrokeColor = pink
stem_pink.StrokeWidth = 8

# Note stem (cyan main)
stem_cyan = doc.PathItems.Add()
sc1 = stem_cyan.PathPoints.Add()
sc1.Anchor = [355, 200]; sc1.LeftDirection = [355, 200]; sc1.RightDirection = [355, 200]
sc2 = stem_cyan.PathPoints.Add()
sc2.Anchor = [355, 135]; sc2.LeftDirection = [355, 135]; sc2.RightDirection = [355, 135]
stem_cyan.Closed = False
stem_cyan.Filled = False
stem_cyan.Stroked = True
stem_cyan.StrokeColor = cyan
stem_cyan.StrokeWidth = 8

# Note flag (triangle)
flag = doc.PathItems.Add()
fp1 = flag.PathPoints.Add()
fp1.Anchor = [355, 135]; fp1.LeftDirection = [355, 135]; fp1.RightDirection = [355, 135]
fp2 = flag.PathPoints.Add()
fp2.Anchor = [380, 125]; fp2.LeftDirection = [380, 125]; fp2.RightDirection = [380, 125]
fp3 = flag.PathPoints.Add()
fp3.Anchor = [380, 155]; fp3.LeftDirection = [380, 155]; fp3.RightDirection = [380, 155]
flag.Closed = True
flag.Filled = True
flag.FillColor = cyan
flag.Stroked = False

# === TOK TEXT — 3 LAYERS FOR GLITCH/GLOW EFFECT ===
print("Creating TOK text layers...")
# Cyan offset (shifted left)
make_text(doc, "TOK", 155, 410, 180, cyan)
# Pink offset (shifted right)
make_text(doc, "TOK", 175, 410, 180, pink)
# Main white text with pink outline
make_text(doc, "TOK", 165, 410, 180, white, pink, 3)

# === TAGLINE ===
print("Creating tagline...")
make_text(doc, "T I K T O K   A G E N C Y", 175, 460, 22, cyan, font_name="Arial-BoldMT")

# === DECORATIVE DOTS ===
print("Creating decorative dots...")
dots = [
    (200, 490, 4, cyan),
    (220, 490, 3, pink),
    (238, 490, 2, white),
    (382, 490, 2, white),
    (400, 490, 3, pink),
    (420, 490, 4, cyan),
]
for x, y, r, color in dots:
    make_ellipse(doc, y + r, x - r, r * 2, r * 2, color)

# === SAVE ===
print(f"Saving AI file to {OUTPUT_AI}...")
save_opts = win32com.client.Dispatch("Illustrator.IllustratorSaveOptions")
save_opts.Compatibility = 25  # ILLUSTRATOR2024
doc.SaveAs(OUTPUT_AI, save_opts)

# Export PNG (4x scale)
print(f"Exporting PNG to {OUTPUT_PNG}...")
png_opts = win32com.client.Dispatch("Illustrator.ExportOptionsPNG24")
png_opts.HorizontalScale = 4.0
png_opts.VerticalScale = 4.0
png_opts.AntiAliasing = True
png_opts.Transparency = False
png_opts.ArtBoardClipping = True
doc.ExportFile(OUTPUT_PNG, 5, png_opts)  # 5 = PNG24 export type

# Export SVG
print(f"Exporting SVG to {OUTPUT_SVG}...")
svg_opts = win32com.client.Dispatch("Illustrator.ExportOptionsSVG")
svg_opts.Compatibility = 25
doc.ExportFile(OUTPUT_SVG, 3, svg_opts)  # 3 = SVG export type

print("\n=== DONE! ===")
print(f"Files created:")
print(f"  AI:  {OUTPUT_AI}")
print(f"  PNG: {OUTPUT_PNG}")
print(f"  SVG: {OUTPUT_SVG}")
